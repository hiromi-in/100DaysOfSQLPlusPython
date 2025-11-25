import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/sales-100daysofchallenge/sales_10000_randomized.csv')

print(f"The number of customers: {len(df.groupby('customer_id'))}")
print(f"The number of customers by country: \n{df.groupby('country')['customer_id'].nunique()}")