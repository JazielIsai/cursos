

import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"Aemet2022.csv",index_col=0,encoding="latin-1")


# Wrap by Province
df1=df.groupby('provincia').mean()
print(df1)
# Graph by bar
df1.plot(kind='bar',stacked = True)
plt.show()

df2=df.sort_values(by='TempMax', ascending=False)[['provincia','TempMax']].head(30)
print(df2)

df2.plot(kind='bar',stacked = True)
plt.show()
