#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the dataset
df = pd.read_csv('customer_data.csv')


# In[3]:


df


# In[5]:


import pandas as pd

# Load the dataset
df = pd.read_csv('customer_data.csv')

# Data Cleaning

# Remove duplicate rows based on 'customer_id' (assuming 'customer_id' is a unique identifier)
df.drop_duplicates(subset=['customer_id'], keep='first', inplace=True)

# Fill missing values in 'purchases' with 0
df['purchases'].fillna(0, inplace=True)

# Calculate the average number of purchases for each gender
average_purchases_by_gender = df.groupby('gender')['purchases'].mean()

# Print the result
print(pd.DataFrame(average_purchases_by_gender))


# In[ ]:




