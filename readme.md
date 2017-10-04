# README for Homework

## 1. Setup
1. The whole home work was written in python 2.7, so python 2.7 is needed. 
   If you don't have it, please visit the following link and choose python 2.7 for your platform 
   > https://www.python.org/downloads/release/python-2714/

   Further more, since this web crawler using several third party libraries. I strongly recommend you use "pip" to install them.
   The following link will help you install pip
   > https://pip.pypa.io/en/stable/installing/

2. Before run the crawler, you may need install the following external libraries.
    > beautifulsoup4:https://pypi.python.org/pypi/beautifulsoup4<br> 
    lxml: https://pypi.python.org/pypi/lxml/4.0.0 <br> 
    pyenchant: https://pypi.python.org/pypi/pyenchant/1.6.11
    
    If you have installed "pip", I have already put all of them in requirement.txt, you could just run the following code in your command. Otherwise, please using the above links to install these libraries.
    > pip install -r requirement.txt

## 2. Steps for running the crawler
1. Please change the directory to where the crawler file is located

2. run the following command to run task one
> python task_one.py
  
  if you want change the seed url, please open the task_one.py and then change the seed. 

3. run the following command to run task two
> python task_two.py

  if you want change the seed url or the keyword, please open the task_two.py and then change the seed or the keyword. 

## 3. Result
1. The result of task one will be stored in "URL for task one.txt" and that of task will be stored in "URL for task two.txt" <br>
It should be mentioned that the result of task two contains a single url, the seed url, which does not contains the keyword - "rain"

The maximum depth reached in task one is 2 and that in task two is 7(crawler stop as soon as reach depth 7)

I threat the depth according to the instructor's answer on Pizza
> https://piazza.com/class/j77oc0hzvkc3ot?cid=18

>Depth 0 is the seed url.<br>
Pages whose links are found on this page are depth 1.<br>
Pages whose links are found on any of the pages in depth 1 are depth 2 and so on


