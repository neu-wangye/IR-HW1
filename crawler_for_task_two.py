import time
import enchant
  
import urllib, urllib2   
from bs4 import BeautifulSoup  
  
import sys  
reload(sys)  
sys.setdefaultencoding("utf8")  
#for UnicodeEncodeError  
  

FINAL_URL_HASH_SET = set()     #Set to make sure that url do not direct to duplicate pages
PREFIX = "https://en.wikipedia.org"
FILE_NAME = "URLs for task two"  
URL_MAX = 1000
DEPTH_MAX = 6
NEXT_LEVEL = []
currentNumOfUrl = 0

def SaveFile(content, filename):
    f=open(filename.replace('/', '**') + ".txt","a")  
    f.write(str(content)+"\n")  
    f.close()  


def SpideWiki(url, keyword):  
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
    headers={'User-Agent':user_agent}  
    try:  
        request=urllib2.Request(url, headers=headers)  
        response=urllib2.urlopen(request)
        final_url = response.geturl()
        if final_url in FINAL_URL_HASH_SET:          #if the final url have already been visited, ignore it.
            return
        FINAL_URL_HASH_SET.add(final_url)            #save the final url to avoid duplicate
        global currentNumOfUrl
        wikiHtml=response.read().decode('utf-8')
        #SaveFile(wikiHtml, url)         #Save the downloaded document       
        SaveFile(url, FILE_NAME)     
        currentNumOfUrl += 1
        html=BeautifulSoup(str(wikiHtml),"lxml")  
        div=html.find(name='div', id='mw-content-text')  
        ps=div.find_all('a')
        for p in ps:  
            pText=p.get('href')
            anchor_text = p.get_text()
            if pText is not None and ":" not in pText and "/wiki/" in pText and "#" not in pText: 
                pText = PREFIX + pText
                if URL_Keyword_Match(keyword, pText) or Text_Keyword_Match(keyword, anchor_text): # check whether key word could be matched against anchor text or text in th URL
                    NEXT_LEVEL.append(pText)

    except urllib2.URLError, e:  
        if hasattr(e,"code"):  
            print e.code  
        if hasattr(e,"reason"):  
            print e.reason  

def Crawler(seed, keyword):
    currentLevel = []
    global currentNumOfUrl
    global NEXT_LEVEL
    currentLevel.append(seed)
    curDepth = 1
    while currentLevel:
        for url in currentLevel:
            if  currentNumOfUrl < URL_MAX and curDepth <= DEPTH_MAX:
                SpideWiki(url, keyword)
                time.sleep(1)

            else:
                print ("Maximum reached %dth depth"%(curDepth))
                return
        currentLevel = NEXT_LEVEL
        NEXT_LEVEL = []
        curDepth += 1


def URL_Keyword_Match(keyword, url):
    word_after_processing = url.lower()[len(PREFIX) + 6:]    # remove the prefix and "/wiki/" from url
    if keyword not in word_after_processing:                 # url without keyword should be removed
        return False
    else:
        word_split = word_after_processing.split('_')        #process the text with "_"
        checker = enchant.Dict("en_US")
        for word in word_split:
            if cmp(word[0 : len(keyword)], keyword) is 0 and checker.check(word):
                return True
        return False        


def Text_Keyword_Match(keyword, text):
    if keyword not in text:                 # url without keyword should be removed
        return False
    else:
        word_split = text.split(' ')        #process the text with " "
        checker = enchant.Dict("en_US")
        for word in word_split:
            if cmp(word[0 : len(keyword)], keyword) is 0 and checker.check(word):
                return True
        return False        
