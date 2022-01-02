from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import copy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import os
import re
import requests


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

	

# service = Service(executable_path="./chromedriver")
# wd = webdriver.Chrome(service=service,options=options)
# wd.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# wd.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

linkGlobal="https://www.wuxiaworld.com"

def generateTxt(chap,title,path):
    f = open(path+"/"+title+".txt", "a")
    f.write(chap)
    f.close()

def getChapter(link,path):
    
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    #wd.get(link)
    title=""
    chap=""
    
    #chap=wd.find_element(By.ID,"chapter-outer").text
    chap=soup.find(id="chapter-outer").text
    #title=wd.find_element(By.CSS_SELECTOR,".caption.clearfix").find_element(By.TAG_NAME,"h4").text
    title=soup.find(class_="caption clearfix").find("h4").text  
    
    newTitle=re.sub('[^a-zA-Z0-9 \n\.]', '', title)
    print(title)
    data=[]

    
    generateTxt(chap,newTitle,path)
 



def getChapters(link):
    r = requests.get(link)
    #wd.get(link)
    data=[]
    #soup = BeautifulSoup(wd.page_source, 'html.parser')
    soup = BeautifulSoup(r.text, 'html.parser')

    #d=wd.find_element(By.CLASS_NAME,'chapter-item').find_elements(By.TAG_NAME,"a")
    #title=wd.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[4]/div/div/div[1]/div[1]/div[2]/div/h2").text 
    title=soup.find(class_="novel-body").find("h2").text
    newTitle=re.sub('[^a-zA-Z0-9 \n\.]', '', title)
    
    path = "./"+newTitle

    isExist = os.path.exists(path)
    if not isExist:  
        os.makedirs(path)
        print(f"Pasta {newTitle} criada")

    
    
    
    p=soup.find_all(class_="chapter-item")
    print(title)
    
    for var in p:
        data.append({'id':len(data)+1,'title':var.text,'link':linkGlobal+var.find("a").get('href')})
        #print(data[-1]["link"])
        
        getChapter(data[-1]["link"],path)     
    #wd.close()

getChapters("https://www.wuxiaworld.com/novel/second-life-ranker")
getChapters("https://www.wuxiaworld.com/novel/overgeared")
getChapters("https://www.wuxiaworld.com/novel/against-the-gods")
getChapters("https://www.wuxiaworld.com/novel/the-godsfall-chronicles")
getChapters("https://www.wuxiaworld.com/novel/city-of-sin")
getChapters("https://www.wuxiaworld.com/novel/rebirth-of-the-thief-who-roamed-the-world")
getChapters("https://www.wuxiaworld.com/novel/renegade-immortal")
getChapters("https://www.wuxiaworld.com/novel/monarch-of-evernight")
getChapters("https://www.wuxiaworld.com/novel/seoul-stations-necromancer")
getChapters("https://www.wuxiaworld.com/novel/tomb-raider-king")
