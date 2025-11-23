import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/sales-100daysofchallenge/sales_10000_randomized.csv')
print(df['product_category'].value_counts())

plt.hist(df['product_category'])
plt.xlabel('Product Category')
plt.show()