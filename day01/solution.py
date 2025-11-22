import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/sales-100daysofchallenge/sales_10000.csv')
print(df)
print(df.describe())
print(df.info())