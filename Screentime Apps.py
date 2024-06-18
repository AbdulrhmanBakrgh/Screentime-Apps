#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[24]:


data = pd.read_csv('/Users/bakr/Downloads/Screentime-App-Details.csv')


# In[25]:


data


# In[26]:


data.isnull().sum()


# In[27]:


data.describe()


# In[28]:


#first look at the amount of usage of the apps:
figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
                title="Usage")
figure.show()


# In[29]:


#look at the number of notifications from the apps:
figure = px.bar(data_frame=data,
                x="Date" ,
                y ="Notifications" , 
                color="App" ,
                title="Notifications")
figure.show()


# In[30]:


#look at the number of times the apps opened:
figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
                title="Times Opened")
figure.show()


# In[31]:


figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()

