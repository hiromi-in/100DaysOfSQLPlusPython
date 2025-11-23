import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/sales-100daysofchallenge/sales_10000.csv')
print(df)
print(df.describe())
print(df.info())
print(df.columns)
print(df['product_category'].value_counts())

plt.subplot(1, 2, 1)
plt.hist(df['price'])
plt.xlabel('Price')

plt.subplot(1, 2, 2)
plt.hist(df['quantity'])
plt.xlabel('Quantity')
