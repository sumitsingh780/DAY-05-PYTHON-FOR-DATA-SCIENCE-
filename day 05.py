#!/usr/bin/env python
# coding: utf-8

# # DAY 05 OF 100 DAYS CHALLENGE 

# # SEABORN LIBRARY

# In[1]:


pip install seaborn


# In[2]:


import seaborn as sns


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


x1 = [2,3,4,6,7,8]
y1 = [9,8,7,6,5,4]
plt.plot(x1,y1)
plt.show()


# In[5]:


x1 = [2,3,4,6,7,8]
y1 = [9,8,7,6,5,4]
sns.lineplot(x = x1 ,y =y1)
plt.show()


# In[6]:


import pandas as pd


# In[7]:


var = [2,22,33,44,55,66]
var1 = [9,8,7,6,5,4]
df=pd.DataFrame({ "var": var, "var1":var1})
sns.lineplot(x ='var',y = 'var1',data=df)
plt.show()


# In[8]:


df1=sns.load_dataset('penguins')


# In[9]:


df1


# In[10]:


sns.lineplot(x = "bill_length_mm",y ="bill_depth_mm",data = df1)
plt.show()


# In[11]:


sns.lineplot(x = "bill_length_mm",y ="bill_depth_mm",data = df1,hue="sex")
plt.show()


# In[12]:


sns.lineplot(x = "bill_length_mm",y ="bill_depth_mm",data = df1)
plt.grid()
plt.title("data")
plt.show()


# # bar plot in seaborn library

# In[15]:


df1


# In[16]:


df1["island"]


# In[26]:


c=[ 'r','g','b']
sns.barplot(x =df1.flipper_length_mm ,y =df1.sex ,color = 'c')
plt.show()


# In[25]:


sns.barplot(x =df1.island ,y =df1.bill_length_mm )
plt.grid()
plt.show()


# In[29]:


sns.barplot(x =df1.island ,y =df1.bill_length_mm ,data = df1 ,hue = "sex")
plt.show()


# # order parameter

# In[31]:


order1 = ["Dream",'Torgersen','Biscoe island']
sns.barplot(x =df1.island ,y =df1.bill_length_mm ,data = df1 ,hue = "sex", order =order1)
plt.show()


# # HUE ORDER

# In[36]:


sns.barplot(x =df1.island ,y =df1.bill_length_mm ,data = df1 ,hue = "sex",hue_order = ["female",'male'])
plt.show()


# In[39]:


sns.histplot(x = "sex",y ='body_mass_g',data =df1,hue ='sex')
plt.show()


# In[43]:


sns.histplot(x = "sex",y ='body_mass_g',data =df1,hue ='sex')
plt.title("ANALYSIS BY SUMIT SINGH")
plt.show()


# In[44]:


sns.displot(df1["flipper_length_mm"])
plt.show()


# In[48]:


sns.displot(df1["flipper_length_mm"],bins=[170,180,190,200,210,220,230],color  ='r')
plt.show()


# In[ ]:




