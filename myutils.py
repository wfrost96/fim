import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def get_stock_on_date(stock, mydate):
    csv_file = "./stock/" + stock + ".L.csv"

    df = pd.read_csv(csv_file)

    mydata = df.loc[(df['Date'] == mydate)]

    open = mydata.Open.item()
    close = mydata.Close.item()
    high = mydata.High.item()
    low = mydata.Low.item()

    return open, close, high, low

myrange = 10
def get_date_range(mydate):
    date = datetime.strptime(mydate, "%Y-%m-%d")

    earlier_date_list = []
    for i in range(14):
        earlier_date = (date - timedelta(days=i)).date()
        earlier_date_day = earlier_date.weekday()
        if earlier_date_day != 5 and earlier_date_day != 6:
            earlier_date_list.append(earlier_date_day)
            if len(earlier_date_list) == myrange:
                start_date = earlier_date
                break

    later_date_list = []
    for i in range(14):
        later_date = (date + timedelta(days=i)).date()
        later_date_day = later_date.weekday()
        if later_date_day != 5 and later_date_day != 6:
            later_date_list.append(later_date_day)
            if len(later_date_list) == myrange:
                end_date = later_date
                break

    return start_date, end_date

def get_earlier_date(mydate, days):
    days += 1
    date = datetime.strptime(mydate, "%Y-%m-%d")

    earlier_date_list = []
    for i in range(14):
        earlier_date = (date - timedelta(days=i)).date()
        earlier_date_day = earlier_date.weekday()
        if earlier_date_day != 5 and earlier_date_day != 6:
            earlier_date_list.append(earlier_date_day)
            if len(earlier_date_list) == days:
                start_date = earlier_date
                break
    return earlier_date

def get_later_date(mydate, days):
    days += 1
    date = datetime.strptime(mydate, "%Y-%m-%d")

    later_date_list = []
    for i in range(30):
        later_date = (date + timedelta(days=i)).date()
        later_date_day = later_date.weekday()
        if later_date_day != 5 and later_date_day != 6:
            later_date_list.append(later_date_day)
            if len(later_date_list) == days:
                start_date = later_date
                break
    return later_date

def plot_highlight_square(stock, mydate): #buy/sell on mydate, based on analysis of earlier 4 days
    open1, close1, high1, low1 = get_stock_on_date(stock, str(get_earlier_date(mydate, 4)))
    open2, close2, high2, low2 = get_stock_on_date(stock, str(get_earlier_date(mydate, 3)))
    open3, close3, high3, low3 = get_stock_on_date(stock, str(get_earlier_date(mydate, 2)))
    open4, close4, high4, low4 = get_stock_on_date(stock, str(get_earlier_date(mydate, 1)))

    highs = [high1, high2, high3, high4]
    highest = max(highs)

    lows = [low1, low2, low3, low4]
    lowest = min(lows)

    x_value = myrange - 1.5, myrange - 1.5 #0.5 covers mydate, which is buy/sell. we want the four days before
    y_value = highest*1.01, lowest*0.99
    plt.plot(x_value, y_value, color='purple', linewidth = 1)

    x_value = myrange - 5.5, myrange - 5.5
    y_value = highest*1.01, lowest*0.99
    plt.plot(x_value, y_value, color='purple', linewidth = 1)

    x_value = myrange - 1.5, myrange - 5.5
    y_value = highest*1.01, highest*1.01
    plt.plot(x_value, y_value, color='purple', linewidth = 1)

    x_value = myrange - 1.5, myrange - 5.5
    y_value = lowest*0.99, lowest*0.99
    plt.plot(x_value, y_value, color='purple', linewidth = 1)
    return
