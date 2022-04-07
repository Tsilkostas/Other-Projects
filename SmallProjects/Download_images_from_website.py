from selenium import webdriver
import requests as rq 
import os 
from bs4 import BeautifulSoup 
import time 

path= input("Enter Path : ")

url=input("Enter URL : ")

output="output"

def get_url(path, url):
    driver =webdriver.Chrome(executable_path= r"{}".format(path))
    driver.get(url)
    print("loading.....")
    res=driver.execute_script("return document.documentElement.outerHTML")
    return res


def get_img_links(res):
    soup=BeautifulSoup(res, "lxlml")
    imglinks=soup.find_all("img", src=True)
    return imglinks
