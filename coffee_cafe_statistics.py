#find average revenue, and profit for item categories
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#load CSV file to Python and create dataframe 
df = pd.read_csv("coffee_revenue_costs.csv")


#find sum, mean, maximum, minimum of revenue by item category
groupedr_sum = df.groupby("item_name")["weekly_item_revenue"].sum()
groupedr_mean = df.groupby("item_name")["weekly_item_revenue"].mean()
groupedr_max = df.groupby("item_name")["weekly_item_revenue"].max()
groupedr_min = df.groupby("item_name")["weekly_item_revenue"].min()

#find sum, mean, maximum, minimum of cost by item category
groupedc_sum = df.groupby("item_name")["weekly_item_cost"].sum()
groupedc_mean = df.groupby("item_name")["weekly_item_cost"].mean()
groupedc_max = df.groupby("item_name")["weekly_item_cost"].max()
groupedc_min = df.groupby("item_name")["weekly_item_cost"].min()

#find summed profit by item category 
profit_data = groupedr_sum.subtract(groupedc_sum)
print(f'summed profit data: {profit_data}\n\n')

#find mean profit by item category 
mean_profit_data = groupedr_mean.subtract(groupedc_mean)
print(f'mean profit data: {mean_profit_data}')

#find profit margin by item category (using summed profit and revenue)
profit_margin = profit_data/groupedr_sum
print(f'profit margin: {profit_margin}')

#create two plots side by side 
plt.subplot(1,2,1)

#create bar chart of mean profits by item category 
categories = df["item_name"].drop_duplicates()
category_array = categories.to_numpy()

mean_profit_array = mean_profit_data.to_numpy()

plt.bar(category_array, mean_profit_array, color = "green")
plt.xticks(rotation = 30, ha = 'right')
plt.title("Mean Profits By Item Category")
plt.xlabel("Item Categories")
plt.ylabel("Mean Profit ($)")

#create two plots side by side
plt.subplot(1,2,2)

#create scatter plot to see relationship between cost and mean profit
x = groupedc_mean.to_numpy()
y = mean_profit_data.to_numpy()
plt.scatter(x, y, color = "purple")
plt.title("Scatter Plot")
plt.xlabel("Mean Item Cost ($)")
plt.ylabel("Mean Profit ($)")

#calculate and display r^2 value
r2_value = round(r2_score(y,x),2)
plt.legend(plt.annotate(f'r^2 value = {r2_value}',xy = (21,89)))

#perform linear fit to show relationship between cost and mean profit
coeff = np.polyfit(x, y, 1)
function = np.poly1d(coeff)
plt.plot(x, function(x), linestyle = '-.',label = 'Linear Fit', color = 'orange')
plt.show()

