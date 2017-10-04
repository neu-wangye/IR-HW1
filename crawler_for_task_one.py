import time
  
import urllib, urllib2  
from bs4 import BeautifulSoup  
  
import sys  
reload(sys)  
sys.setdefaultencoding("utf8")  
#for UnicodeEncodeError  
  

FINAL_URL_HASH_SET = set()     #Set to make sure that url do not direct to duplicate pages
PREFIX = "https://en.wikipedia.org" # Prefix to form a url
FILE_NAME = "URLs for task one"   # File name to store urls
URL_MAX = 1000                      #Max urls that could be stored
DEPTH_MAX = 6                       #Max depth that crawl. In that function, The seed page is the first url and counts for depth1
NEXT_LEVEL = []                     #Queue used to store url of the next depths
currentNumOfUrl = 0                 #Num of URLs that have already been stored

def SaveFile(content, filename):
    """
        Save urls and downloaded document

        Args:
            content: content need to be stored
            filename: the name of the txt file

    """
    f=open(filename.replace('/', '**') + ".txt","a")  
    f.write(str(content)+"\n")  
    f.close()  

def SpideWiki(url):  
    """
        The main part of the crawler, parse the html of given urls and get the urls that could be used

        Args:
            url: the url need to be crawled

    """
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
        currentNumOfUrl += 1
        wikiHtml=response.read().decode('utf-8')
        #SaveFile(wikiHtml, url)         #Save the downloaded document
        SaveFile(url, FILE_NAME)  
        html=BeautifulSoup(str(wikiHtml),"lxml")  
        div=html.find(name='div', id='mw-content-text')  
        ps=div.find_all('a')
        for p in ps:  
            pText=p.get('href')
            if pText is not None and ":" not in pText and "/wiki/" in pText: 
                pText = PREFIX + pText
                NEXT_LEVEL.append(pText)
                
    except urllib2.URLError, e:  
        if hasattr(e,"code"):  
            print e.code  
        if hasattr(e,"reason"):  
            print e.reason  

def Crawler(url):
    """
        Start the crawler from the seed url and using BFS to finish it

        Args:
            urls: The seed url

    """
    currentLevel = []       
    global currentNumOfUrl
    global NEXT_LEVEL
    currentLevel.append(url)
    curDepth = 1
    while currentLevel:
        for url in currentLevel:
            if  currentNumOfUrl < URL_MAX and curDepth <= DEPTH_MAX:   #Check whether we have reached the boundary
                SpideWiki(url)

            else:
                print ("Maximum reached %dth depth"%(curDepth))   #Report the depth reached when finishing
                return
        currentLevel = NEXT_LEVEL       #Moving to next depth
        NEXT_LEVEL = []
        curDepth += 1                


