import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/sales-100daysofchallenge/sales_10000_randomized.csv')



quantity_max = df['quantity'].max()
quantity_min = df['quantity'].min()

twentyFive = (quantity_max - quantity_min) * 0.25 + quantity_min
fifty = (quantity_max - quantity_min) * 0.5 + quantity_min
seventyFive = (quantity_max - quantity_min) * 0.75 + quantity_min

df_0_25 = df[df["quantity"] <= twentyFive]
df_25_50 = df[(df["quantity"] > twentyFive) & (df["quantity"] <= fifty)]
df_50_75 = df[(df["quantity"] > fifty) & (df["quantity"] <= seventyFive)]
df_75_100 = df[df["quantity"] > seventyFive]

quantity_counts = {
    f"0-25%({quantity_min}-{twentyFive})": len(df_0_25),
    f"25-50%({twentyFive}-{fifty})": len(df_25_50),
    f"50-75%({fifty}-{seventyFive})": len(df_50_75),
    f"75-100%({seventyFive}-{quantity_max})": len(df_75_100)
}

print('------Quantity Counts-----')
print(quantity_counts)

price_max = df['price'].max()
price_min = df['price'].min()

twentyFive = (price_max - price_min) * 0.25 + price_min
fifty = (price_max - price_min) * 0.50 + price_min
seventyFive = (price_max - price_min) * 0.75 + price_min

df_0_25 = df[df["price"] <= twentyFive]
df_25_50 = df[(df["price"] > twentyFive) & (df["price"] <= fifty)]
df_50_75 = df[(df["price"] > fifty) & (df["price"] <= seventyFive)]
df_75_100 = df[df["price"] > seventyFive]

price_counts = {
    f"0-25%({price_min}-{twentyFive})": len(df_0_25),
    f"25-50%({twentyFive}-{fifty})": len(df_25_50),
    f"50-75%({fifty}-{seventyFive})": len(df_50_75),
    f"75-100%({seventyFive}-{price_max})": len(df_75_100)
}

print('\n-----------Price Counts-----')
print(price_counts)

print('\n------describe-----------')
print(df.describe())



