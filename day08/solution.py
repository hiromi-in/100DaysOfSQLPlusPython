import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/sales-100daysofchallenge/sales_10000_randomized.csv')

df_january = df[(df['order_date'] >='2024-01-01') & (df['order_date'] <= '2024-01-31')].sort_values(['order_date', 'country', 'product_name', 'price'])

counts = df_january['product_name'].value_counts()

print(counts)
print(f'Total : {counts.sum()}')


plt.figure(figsize=(10,5))
bars = plt.bar(counts.index, counts.values)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,   # x position (center of bar)
        height,                            # y position (top of bar)
        str(height),                       # text (the count)
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.xticks(rotation=45)
plt.xlabel("Product_name")
plt.ylabel("Count")
plt.title("Number of Electronics Sales by Country")

plt.show()
