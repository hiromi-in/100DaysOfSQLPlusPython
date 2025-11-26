import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/sales-100daysofchallenge/sales_10000_randomized.csv')

#Revenue by product_ctegory
df["revenue"] = pd.to_numeric(df["price"] * df["quantity"])
print(df.groupby("product_category")["revenue"].sum())

#Revenue by product_name
print(df.groupby("product_name")["revenue"].sum())

#Revenue by country, product_category
print(df.groupby(["country","product_category"])["revenue"].sum())

#Revenue by week, then product_category
df['order_date'] = pd.to_datetime(df['order_date'])
weekly_revenue = df.groupby([pd.Grouper(key='order_date', freq='W-MON'),'product_category'])['revenue'].sum().reset_index()
weekly_revenue.rename(columns={'order_date': 'week_start'}, inplace=True)
print(weekly_revenue)

plt.figure(figsize=(20, 6), dpi=100)  
plt.bar(df['product_category'],df['revenue'])
plt.xlabel('Product Category')
plt.ylabel('Revenue')
plt.title('Revenue by Product Category')


plt.figure(figsize=(20, 6), dpi=100)  
plt.bar(df['product_name'],df['revenue'])
plt.xlabel('Product Name')
plt.ylabel('Revenue')
plt.title('Revenue by Product Name')

plt.show()
