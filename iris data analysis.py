#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[58]:


iris=sns.load_dataset('tips')


# In[57]:


iris.head()
# tip is dependent feaature on ...like independt features smoker,day,size etc
#it means, if tip increases then independent features also increases


# In[10]:


iris.describe()


# In[11]:


iris.corr()
#here correleation done only between int and float not in categories


# In[12]:
566


# one kind of showing visualzation of iris.corr()
sns.heatmap(iris.corr())


# In[15]:


#join plot helps to find bivariant analysis
#sns.joinplot(x='tip',y='total_bill',data=iris,kind='hex')


# In[16]:


#visualing in pairplot format
sns.pairplot(iris)


# In[17]:


sns.pairplot(iris,hue='sex')


# In[18]:


sns.pairplot(iris,hue='size')


# In[19]:


sns.pairplot(iris,hue='smoker')


# In[35]:


#dist plot
sns.displot(iris['tip'])


# In[33]:


sns.displot(iris['tip'],kde=False,bins=20)


# In[38]:


#categorial plots(1.boxplot,2.violonplot,3.countplot,4.barplot)
#countplot
sns.countplot('sex',data=iris)


# In[43]:


#barplot
sns.barplot(x='total_bill',y='sex',data=iris)


# In[47]:


#box plot
sns.boxplot(x='smoker',y='total_bill',data=iris)


# In[52]:


sns.boxplot(data=iris,orient='v')


# In[55]:


#violin plot
sns.violinplot(x='total_bill',y='day',data=iris,palette='rainbow')


# In[ ]:




