from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import copy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import os
import re



options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')

	

service = Service(executable_path="./chromedriver")
#wd = webdriver.Chrome("./chromedriver",options=options)
wd = webdriver.Chrome(service=service,options=options)
wd.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
wd.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

linkGlobal="https://readnovelfull.com"

def generateTxt(chap,title,path):
    f = open(path+"/"+title+".txt", "a")
    f.write(chap)
    f.close()

def getChapter(link,path):
    response="https://novelfull.com/the-second-coming-of-gluttony/chapter-1-prologue.html"
    wd.delete_all_cookies()
    
    wd.get(link)
    title=""
    chap=""
    try:
        chap=wd.find_element(By.ID,"chapter-content").text
    except:
        chap=wd.find_element(By.ID,"chr-content").text
    try:
        title=wd.find_element(By.CLASS_NAME,"chr-text").text
        
    except:
        title=wd.find_element(By.CLASS_NAME,"chapter-text").text

    newTitle=re.sub('[^a-zA-Z0-9 \n\.]', '', title)
    print(newTitle)
    data=[]

    
    generateTxt(chap,newTitle,path)
    wd.close()
    return chap
 



def getChapters(link):

    
    response="https://readnovelfull.com/the-second-coming-of-gluttony-novel.html"
    wd.get(link+"#tab-chapters-title")
    data=[]
    time.sleep(1)
    d=wd.find_element(By.CLASS_NAME,'panel-body').find_elements(By.TAG_NAME,"a")
    title=wd.find_element(By.XPATH,"//*[@class='col-xs-12 col-sm-8 col-md-8 desc']/h3").text 
    newTitle=re.sub('[^a-zA-Z0-9 \n\.]', '', title)

    path = "./"+newTitle

    isExist = os.path.exists(path)
    if not isExist:  
        os.makedirs(path)
        print(f"Pasta {newTitle} criada")

    
    soup = BeautifulSoup(wd.page_source, 'html.parser')
    
    p=soup.find(class_="tabbable light").find_all("a")

    for var in p:
        data.append({'id':len(data)+1,'title':var.text,'link':linkGlobal+var.get('href')})
        #print(data[-1]["title"])
        
        getChapter(data[-1]["link"],path)     
    

getChapters("https://readnovelfull.com/the-second-coming-of-gluttony-novel.html")
