#This program downloads CSVs of stock prices with data from a custom range of recent days. Hypothetically it will go back as far as 1970, unlike scrape_stock_recent.py that will only go back 50 ish days.

import datetime
import requests
from bs4 import BeautifulSoup
import pickle
import csv

import requests
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
from datetime import datetime, date, timedelta
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from ftse250 import *
#ftse250_list = ftse250_list[:5] #for testing

myerrors = []
for stock in ftse250_list:
    print(stock)

    link = "https://finance.yahoo.com/quote/" + stock + ".L/history?period1=1273142200&period2=1608249600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true" #two dates are 6th May 2010 (UK General Election) and 18th December 2020. TO DO: make most recent date the day today.
    #link = "https://uk.finance.yahoo.com/quote/" + stock + ".L/history?p=" + stock + ".L"

    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    #options.add_argument('--headless')
    driver = webdriver.Chrome("chromedriver", options=options)

    driver.get(link)
    try:
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[@download='" + stock + ".L.csv']").click()
        time.sleep(5)
    except:
        print("Error:", stock, link)
    driver.close()
