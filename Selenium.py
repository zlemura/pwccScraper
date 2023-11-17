from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup
from Listing import Listing
driver = webdriver.Edge('./msedgedriver.exe')

def open_auction_page(schedule_id):
    driver.get("https://www.pwccmarketplace.com/weekly-auction?auction_schedule_id=" + str(schedule_id) + "&category=soccer&sort_by=year_first")

def fetch_gridItemList():
    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "gridItemList"))
        ) #Retry every 10 seconds until element found.
    finally:
        gridItemList = driver.find_element(By.CLASS_NAME, "gridItemList")
    return gridItemList

def convert_gridItemList_to_Listing_list(gridItemList):
    #print(gridItemList.get_attribute('innerHTML'))
    separated_gridItemList = gridItemList.find_elements(By.CLASS_NAME,"d-flex.flex-column.justify-content-center.flex-1")

    Listing_list = []

    for item in separated_gridItemList:
        a_element = item.find_element(By.TAG_NAME, 'a')
        '''
        print(a_element.get_attribute('title'))
        print(a_element.get_attribute('href'))
        '''
        Listing_list.append(Listing(a_element.get_attribute('title'), a_element.get_attribute('href')))

    return Listing_list


def kill_driver():
    driver.close()