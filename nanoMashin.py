
import time
import copy
from bs4 import BeautifulSoup
import os
import re
import requests

	


linkGlobal="https://www.nanomashin.online/"

def generateTxt(chap,title,path):
    f = open(path+"/"+title+".txt", "a")
    f.write(chap)
    f.close()

def getChapter(link,path):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    title=""
    chap=""
    chap=soup.find(class_="pt-10 pb-8 text-gray-900 dark:text-gray-100 prose dark:prose-dark max-w-none text-lg").text
    title=soup.find(class_="text-3xl font-extrabold leading-9 tracking-tight text-gray-900 dark:text-gray-100 sm:text-4xl sm:leading-10 md:text-5xl md:leading-14").text  
    newTitle=re.sub('[^a-zA-Z0-9 \n\.]', '', title)
    print(newTitle)
    data=[]

    
    generateTxt(chap,newTitle,path)
 



def getChapters(link):

    ok=True
    page=1
    while ok:
        try:
            r = requests.get(link+"/page/"+str(page))
            data=[]
            
            
            soup = BeautifulSoup(r.text, 'html.parser')

            title=soup.find(class_="text-3xl font-extrabold leading-9 tracking-tight text-gray-900 dark:text-gray-100 sm:text-4xl sm:leading-10 md:text-6xl md:leading-14").text
            newTitle=re.sub('[^a-zA-Z0-9 \n\.]', '', title)
            
            path = "./"+newTitle
            print(title)
            isExist = os.path.exists(path)
            if not isExist:  
                os.makedirs(path)
                print(f"Pasta {newTitle} criada")

            
            
            
            try:
                p=soup.find_all("ul")[1].find_all("li")
            except:
                p=soup.find("ul").find_all("li")


            
            for var in p:
                data.append({'id':len(data)+1,'title':var.find("a").text,'link':linkGlobal+var.find("a").get('href')})
                print(data[-1]["link"])
                
                getChapter(data[-1]["link"],path) 
            page+=1       
        except:
            print("Acabou!")
            ok=False



getChapters("https://www.nanomashin.online/the-dark-magician-transmigrates-after-66666-years")
