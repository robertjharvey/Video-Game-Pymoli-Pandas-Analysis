#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[2]:


purchase_data.head()


# In[13]:


total_players = len(purchase_data['SN'].value_counts())
total_players


# In[15]:


unique_games = len(purchase_data['Item ID'].value_counts())
unique_games


# In[16]:


total_revenue = purchase_data['Price'].sum()
total_revenue


# In[27]:


number_purchases = len(purchase_data['Purchase ID'].value_counts())
number_purchases


# In[28]:


average_price = total_revenue / number_purchases
average_price


# In[31]:


summary_info = {'Number of Unique Items' : [unique_games],
             'Average Price' : [average_price],
             'Number of Purchases' : [number_purchases],
             'Total Revenue' : [total_revenue]}
summary_info_table = pd.DataFrame(summary_info)
display(summary_info_table)


# In[ ]:




