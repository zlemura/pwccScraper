from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup
import urllib.parse
from Listing import Listing

def open_auction_page(schedule_id):
    driver = webdriver.Edge('./msedgedriver.exe')
    driver.get("https://www.pwccmarketplace.com/weekly-auction?auction_schedule_id=" + str(schedule_id) + "&category=soccer&sort_by=year_first&page=1")
    return driver


def determine_page_limit(driver):
    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "goToPaginatorContainer.flex-center.w-100"))
        ) #Retry every 10 seconds until element found.
    finally:
        main_paginator_container = driver.find_element(By.CLASS_NAME, "goToPaginatorContainer.flex-center.w-100")
    flex_center = main_paginator_container.find_element(By.CLASS_NAME, "flex-center")
    a_flex_center = flex_center.find_elements(By.TAG_NAME, "a")
    page_limit = a_flex_center[len(a_flex_center) - 1].text

    return int(page_limit)


def fetch_gridItemList(driver):
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

def update_auction_page(driver, current_page, schedule_id):
    current_url = "https://www.pwccmarketplace.com/weekly-auction"
    current_url_params = {'auction_schedule_id': schedule_id, 'category': 'soccer', 'sort_by':'year', 'page': current_page}

    url_parts = urllib.parse.urlparse(current_url)
    query = dict(urllib.parse.parse_qsl(url_parts.query))
    query.update(current_url_params)

    new_url = url_parts._replace(query=urllib.parse.urlencode(query)).geturl()

    driver.get(new_url)

    return driver

def kill_driver(driver):
    driver.close()