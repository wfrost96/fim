#This program updates CSVs of stock prices with data from a custom range of recent days. It won't work for date ranges greater than 50 ish days. The program won't add data that already exists into the csv, and does this my checking for dates.

import datetime
import requests
from bs4 import BeautifulSoup
import csv
import re

def num(s):
    s = s.replace(",", "")
    try:
        return int(s)
    except ValueError:
        return float(s)

def get_date_today():
    date_today = datetime.datetime.utcnow()
    date_today_epoch = seconds_since_epoch(date_today)
    date_today_str = str(date_today_epoch)[:-7]
    return date_today, date_today_str

def get_earlier_date(date_today, mynum):
    earlier_date = date_today - datetime.timedelta(days=mynum)
    earlier_date_epoch = seconds_since_epoch(earlier_date)
    earlier_date_str = str(earlier_date_epoch)[:-7]
    return earlier_date, earlier_date_str

def seconds_since_epoch(date_today):
    seconds_since_epoch = date_today.timestamp()
    return seconds_since_epoch

def get_soup(stock):
    stock = stock + ".L"
    mylink = "https://uk.finance.yahoo.com/quote/" + stock + "/history?period1=" + earlier_date_str + "&period2=" + date_today_str + "&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"

    webpage = requests.get(mylink)
    soup = BeautifulSoup(webpage.content, "html.parser")
    return soup

def get_data(soup):
    data = soup.select("table[data-test='historical-prices'] > tbody > tr")
    stock_data = []
    stock_day = []
    for item in data:
        mydata = item.find_all(re.compile("(span)"))
        for i in range(len(mydata)):
            if i == 0:
                date_time_str = mydata[i].get_text()
                stock_date = datetime.datetime.strptime(date_time_str, '%d %b %Y').date()
                stock_day.append(stock_date)
            try:
                if i == 1:
                    stock_open = num(mydata[i].get_text())
                    stock_day.append(stock_open)
                if i == 2:
                    stock_high = num(mydata[i].get_text())
                    stock_day.append(stock_high)
                if i == 3:
                    stock_low = num(mydata[i].get_text())
                    stock_day.append(stock_low)
                if i == 4:
                    stock_close = num(mydata[i].get_text())
                    stock_day.append(stock_close)
                if i == 5:
                    stock_close_adj = num(mydata[i].get_text())
                    stock_day.append(stock_close_adj)
                if i == 6:
                    stock_volume = num(mydata[i].get_text())
                    stock_day.append(stock_volume)
                    stock_data.append(stock_day)
                    stock_day = []
            except:
                stock_day.append(mydata[i]) #nb this doesn't add to database because there's already a day for this data in there.
                stock_data.append(stock_day)
                stock_day = []

    stock_data = sorted(stock_data, key = lambda x: x[0]) #sort by date, oldest to newest(?)
    return stock_data

def update_csv(stock, stock_data):
    csv_file = "stock/" + stock + ".L.csv"

    #get dates already included
    mydates = []
    with open(csv_file, newline='') as csvfile:
         mystock = csv.reader(csvfile)
         for row in mystock:
             try:
                 mydates.append(row[0])
             except:
                 continue
    #print(mydates)

    #add any dates not already included
    with open(csv_file, 'a', newline='') as myfile:
         wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
         wr.writerow([]) #this irons out a bug which otherwise appends the first new row to the end of the last row.
         if mydates == []:
             wr.writerow(["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
         for i in range(len(stock_data)):
             mydate = stock_data[i][0].strftime("%Y-%m-%d")
             if mydate not in mydates:
                 wr.writerow(stock_data[i])

date_today, date_today_str = get_date_today()
earlier_date, earlier_date_str = get_earlier_date(date_today, 30) #num is num of days before

from ftse250 import *
ftse250_list = ftse250_list[100:250] #for testing
ftse250_list = ['QQ']

problem_list = []
for stock in ftse250_list:
    #try:
    soup = get_soup(stock)
    stock_data = []
    stock_data = get_data(soup)
    update_csv(stock, stock_data)
    print(stock, "successfully updated")
    #except:
    #    print("Problem with", stock)
    #    problem_list.append(stock)
print("Problem list:", problem_list)
#END OF FILE
