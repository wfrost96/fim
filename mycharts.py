import matplotlib.pyplot as plt
import pandas as pd
from basic_funcs import *

stock = "WIZZ"
start_date = "2019-02-25"
end_date = "2019-03-10"

def get_candle_plot(stock, start_date, end_date):
    csv_file = "./stock/" + stock + ".L.csv"

    df = pd.read_csv(csv_file)

    days = df.Date

    start_date = str(start_date)
    end_date = str(end_date)
    mydays = df.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    plot_points = []
    for index, row in mydays.iterrows():
        points = []
        points.append(row.Date)
        points.append(row.Open)
        points.append(row.Close)
        points.append(row.High)
        points.append(row.Low)
        if num(row.Close) >= num(row.Open):
            color = "green"
        else:
            color = "red"
        points.append(color)
        plot_points.append(points)

    for i in range(len(plot_points)):
        item = plot_points[i]

        x_value = i, i #item[0] if you want to use date
        y_value = item[1], item[2]
        plt.plot(x_value, y_value, color = item[5], linewidth = 8)

        #high/low
        x_value = i, i
        y_value = item[3], item[4]
        plt.plot(x_value, y_value, color = item[5], linewidth = 2)

    #make x axis pretty
    plt.xlabel('Date')
    plt.xticks(rotation=30, ha='right')
    #make y axis pretty
    plt.ylabel('Price')

    ax = plt.subplot()
    ax.grid()

    plt.title(stock, fontsize=20)
    plt.tight_layout()
    #plt.show()

    return plt.tight_layout()

#get_candle_plot(stock, start_date, end_date)
