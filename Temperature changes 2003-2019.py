#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing packages and opening csv file

import pandas as pd

df1 = pd.read_csv(r'G:\Python projects\pynb\GT_data1.csv')
df1


# # Data Manipulation for DataFrame 1

# In[2]:


# Finding correct indicies for data manipulation
df1.head(170)

df1.iloc[153:170]

# Redefining data to encompass required data
df1 = df1.iloc[153:170]

# Resetting Index
df1 = df1.reset_index(drop = True)

# Renaming comlumns
df1 = df1.rename(columns = {'Median temperature anomaly from 1961-1990 average':'Change'})

# Dropping Columns
df1 = df1.drop(columns = ['Entity', 'Code', 'Upper bound (95% CI)', 'Lower bound (95% CI)'])

df1


# # Data Manipulation for DataFrame 2

# In[3]:


# Opening Second dataset and defining dataframe

df2 = pd.read_csv(r'G:\Python projects\pynb\GT_data2.csv')
df2


# In[4]:


# finding correct indicies
df2.head(17)

# Redefining dataframe
df2 = df2.iloc[0:17]

# Renaming Columns
df2 = df2.rename(columns = {'Temp_change': 'Change'})

# Changing data type as date output was float
df2['Year'] = df2['Year'].astype('Int64')

df2


# # Merging df1 and df1 into new variable

# In[5]:


# Merging df1 and df2 into one table 
df3 = pd.merge(df1, df2, left_index = True, right_index = True)

# Dropping extra 'year' column
df3 = df3.drop(columns = ['Year_y'])

# Changing Temperature values to 2 decimal points
df3['Change_x'] = df3['Change_x'].apply(lambda x: float("{:.2f}".format(x)))

# renaming Columns
df3 = df3.rename(columns = {'Year_x': 'Year', 'Change_x': 'Temp_Data 1', 'Change_y':'Temp_Data 2'})
df3


# # Plotting Line Graph

# In[8]:


# importing matplot to chart graph
import matplotlib.pyplot as plt


# In[9]:


ax = df3.plot(x = "Year", y = ["Temp_Data 1", "Temp_Data 2"], title = "Temperature Changes between 2003-2019")
ax.set_xlabel("Year")
ax.set_ylabel("Temperature C")
plt.show()


# In[ ]:




