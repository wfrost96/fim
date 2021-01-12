import matplotlib.pyplot as plt
import pandas as pd

stock = "WIZZ.L"
csv_file = "./stock/" + stock + ".csv"

df = pd.read_csv(csv_file)

days = df.Date
open_price = df.Open
close_price = df.Close

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

i = 0
mylist = []
plot_points = []
#while True:
while i < 50:
    try:
        points = []
        points.append(df.Date[i])
        points.append(df.Open[i])
        points.append(df.Close[i])
        points.append(df.High[i])
        points.append(df.Low[i])
        if num(df.Close[i]) >= num(df.Open[i]):
            color = "green"
        else:
            color = "red"
        points.append(color)
        plot_points.append(points)

        i += 1
    except:
        break

for item in plot_points:
    #open/close
    x_value = item[0], item[0]
    y_value = item[1], item[2]
    plt.plot(x_value, y_value, color = item[5], linewidth = 8)

    #high/low
    x_value = item[0], item[0]
    y_value = item[3], item[4]
    plt.plot(x_value, y_value, color = item[5], linewidth = 2)

#make x axis pretty
plt.xlabel('Date')
plt.xticks(rotation=30, ha='right')
ax = plt.subplot()
for index, label in enumerate(ax.xaxis.get_ticklabels()):
    if index % 5 != 0:
        label.set_visible(False)

#make y axis pretty
plt.ylabel('Price')

plt.title(stock, fontsize=20)
plt.tight_layout()

#linear regression to get line of best fit


plt.show()
