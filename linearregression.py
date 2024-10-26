import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df = pd.read_csv('http://bit.ly/w-data')
df.head()


# In[8]:


plt.scatter(df['Hours'],df['Scores'])
plt.xlabel('Hours of study')
plt.ylabel('Percentage')
plt.title('Studied Hours')
plt.show()


# In[9]:


df.corr()


# In[ ]:




