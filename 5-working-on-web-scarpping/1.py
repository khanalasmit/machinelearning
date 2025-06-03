from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import math

driver=webdriver.Chrome()
#it explores the website of amazon
def amazon_bot(url,search_item):
    driver.get(url)
    time.sleep(20)
    send_to_search(search_item)

#send the search item to the search box in the web
def send_to_search(search_item):
    try:
        search_element=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,'twotabsearchtextbox'))
        )
        search_element.clear()
        search_element.send_keys(search_item)
        search_element.send_keys(Keys.RETURN)
        
    except:
        print('Error occured during search')
    if send_next_key():
        pass

def get_items():
    try:
        pass
    except:
        pass
    
    

#function to click on the next in the web driver in the webpage
def send_next_key():
    #give maximum time of 10 sec to load and search for the web page
    try:
        next_elemnet=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CLASS_NAME,'s-pagination-item'))
        )
        next_elemnet.send_keys(Keys.ENTER)
        next_elemnet.send_keys(Keys.ENTER)
        time.sleep(5)
        return True
    except:
        print("Erro occured during sending next key")
        return False
    
if __name__==amazon_bot('https://www.amazon.com','most expensive laptops'):
    amazon_bot()