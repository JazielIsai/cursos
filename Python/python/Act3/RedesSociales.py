# -*- coding: utf-8 -*-
"""
Created on Tue May  3 08:39:09 2022

@author: jhazy
"""

import pandas as pd
import matplotlib.pyplot as plt

fbk = ['Facebook', 2449, True, 2006]
twt = ['Twitter', 339, False, 2006]
ig = ['Instagram', 1000, True, 2010]
yt = ['YouTube', 2000, False, 2005]
lkn = ['LinkedIn', 663, False, 2003]
wsp = ['WhatsApp', 1600, True, 2009]

# List with data
list_rrss = [fbk, twt, ig, yt, lkn, wsp]

# create dataframe to partir of lists
df_rrss = pd.DataFrame(list_rrss, columns=['Name', 'Cant', 'ES_FBK', 'YEAR'])

df_rrss


# example basic
x = [1,2,3,4,5]
y = [1,8,27,64,125]

plt.plot(x,y)
plt.show()

# graph by plot
plt.plot(df_rrss['Name'], df_rrss['Cant'])
plt.show()

# graph by scatter
plt.scatter(df_rrss['Name'], df_rrss['Cant'])
plt.show()

# graph by bar
plt.bar(df_rrss['Name'], df_rrss['Cant'])
plt.show()

# graph of bar order
df_rrss_sort = df_rrss.sort_values('Cant', ascending=False)
plt.bar(df_rrss_sort['Name'], df_rrss_sort['Cant'])
plt.show()

# graph of bar order and by colors
df_rrss_sort = df_rrss.sort_values('Cant', ascending=False)
plt.bar(df_rrss_sort['Name'], df_rrss_sort['Cant'], color=['b', 'r', 'g', 'm', 'k', 'c'])
plt.show()


plt.pie(df_rrss['Cant'], labels=df_rrss['Name'])
plt.show()

df_rrss_sort = df_rrss.sort_values('Cant', ascending=False)

list_col_rrss = ['#3b5998', '#FF0000', '#25d366', '#Ba3ab9', '#0e76a8', '#00acee']
plt.title('Cantidad de usuarios por Red Social')
plt.pie(
        df_rrss_sort['Cant'], 
        labels=df_rrss_sort['Name'],
        colors=list_col_rrss,
        shadow=True,
        explode=[0,0.1,0,0.2,0,0.4],
        autopct='%1.1f%%'
        )
plt.show()
