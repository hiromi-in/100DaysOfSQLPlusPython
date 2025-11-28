#day06

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/sales-100daysofchallenge/sales_10000_randomized.csv')

print(df[df['country'] == 'USA'].describe())

#Number of orders from the US by item quantity
print(df[df['country'] == 'USA'].groupby('quantity')['country'].count())

#Number of orders from the US by product name
print(df[df['country'] == 'USA'].groupby('product_name')['country'].count().sort_values(ascending=False))

# Number of orders from the US in comparison of average
df_usa = df[df['country'] == 'USA']
avg_price = df_usa['price'].mean()

over_or_on_avg_count = (df_usa['price'] >= avg_price).sum()
under_avg_count      = (df_usa['price'] <  avg_price).sum()

result_df = pd.DataFrame({
    'over_or_on_avg_count': [over_or_on_avg_count],
    'under_avg_count': [under_avg_count],
    'avg_price': [avg_price]
})

print(result_df)
