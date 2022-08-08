#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing all required libraries 
import pandas as pd
import numpy as np
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


get_ipython().system('pip3 install plotly')


# In[7]:


import plotly.express as px


# In[8]:


plotly.__version__


# In[9]:


df = pd.read_csv("Netflix_data.csv")


# In[10]:


df.head() #To display first 5 rows


# In[11]:


df.tail() #To display last 5 rows


# In[12]:


df.shape #to display number of columns and rows


# In[13]:


#droping columns not relevant to our analysis
df = df.drop(['cast', 'director', 'duration', 'description'],axis = 1)


# In[14]:


df.describe() #


# In[15]:


df.info() #to check the datatypes of our columns


# In[16]:


df.isnull().values.any() #to check id there are empty values


# In[17]:


df.isna().sum()


# In[18]:


#to change datatype of date_added
df['date_added'] = pd.to_datetime(df['date_added'])
df['release_year'] = pd.to_numeric(df['release_year'])


# In[19]:


df.head()


# In[20]:


df.info() #recheck datatypes


# In[21]:



    #histogram shows that Netflix released content the most in 2018
px.histogram(df, x= 'release_year', color= 'type')


# In[44]:


import plotly.io as pio


# In[41]:


#histogram displays that Netflix adds content on the first month of the year which is January more than any other month
px.histogram(df, x= 'date_added', color = 'date_added_month') 


# In[24]:


#histogram displays that Netflix adds movies on the first day of the month more than any other day
px.histogram(df, x= 'Day_Added', color = 'Day_Added') 


# In[25]:


#histogram displays that Netflix adds content on FRIDAYs more than any other day
px.histogram(df, x= 'Day_of_Week', color = 'type') 


# In[26]:


#extract month from data added
df['date_added_month'] = df['date_added'].dt.month
df


# In[27]:


#count total values by type 
df.type.value_counts()


# In[28]:


g = df.groupby('type') #group by types 
g


# In[29]:


for type, type_df in g:
    print (type)
    print (type_df)


# In[30]:


moviess = g.get_group('Movie')
moviess


# In[31]:


#sort by descending order, top ratings for movies
px.histogram(moviess, x= 'rating', color = 'rating').update_xaxes(categoryorder = 'total descending')


# In[32]:


tv = g.get_group('TV Show')
tv


# In[33]:


#sort by descending order, top ratings for TV Shows
px.histogram(tv, x= 'rating', color = 'rating').update_xaxes(categoryorder = 'total descending')


# In[34]:


#Checking total count of content released by Netlix 
total = df.groupby('type').type.count()
total


# In[35]:


df.groupby(['type']).sum().plot(kind='pie', x = 'moviess', y = 'release_year', autopct='%1.0f%%') #demonstrated in pie chart


# In[36]:


sns.countplot(x = 'type', data = df)
plt.title("Count VS Type of Show")


# In[37]:


df['country'].value_counts().head(10)


# In[38]:


plt.figure(figsize = (12,6))
sns.countplot(y= 'country', order = df['country'].value_counts().index[0:10], data = df)
plt.title ('Content on Netflix grouped by Country')


# In[39]:


df.release_year.value_counts()[:10] #total count of content released by Netflix per year


# In[40]:


plt.figure(figsize = (12,8))
sns.countplot(y='listed_in', order = df['listed_in'].value_counts().index[0:20], data = df)
plt.title("most content released")


# In[ ]:





# In[ ]:




