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
htmls=[]
#it explores the website of amazon
def amazon_bot(url,search_item):
    driver.get(url)
    time.sleep(20)
    send_to_search(search_item)
    html=get_items()
    htmls.append(html)
    #get the page html to parse from the web untill the next key is there
    while send_next_key():
        html=get_items()
        htmls.append(html)
    parse_pages()

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

def get_items():
    try:
        html=driver.page_source
        #print(html)
    except:
        print("Error in getting items")
    
    

#function to click on the next in the web driver in the webpage
def send_next_key():
    #give maximum time of 10 sec to load and search for the web page
    try:
        next_elemnet=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'a.s-pagination-next'))
        )
        next_elemnet.click()
        time.sleep(3)
        return True
    except:
        print("Error occured during sending next key")
        return False
    


#parsing the page to select the appropriate element
def parse_pages():
    print(len(htmls))
    #for html in htmls:
    #    page=BeautifulSoup(html,'html.parser')
    #    list_of_items=page.find_all('css_selector',{'div.a-spacing-top-small'})
    #    print(list_of_items)
if __name__==amazon_bot('https://www.amazon.com','most expensive laptops'):
    amazon_bot()