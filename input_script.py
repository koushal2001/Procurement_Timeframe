#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import pickle


# In[7]:


filename = '/home/koushal/Downloads/Random_forest_model.sav'


# In[8]:


loaded_model = pickle.load(open(filename, 'rb'))


# In[10]:


input_cols = ["EST_COST_RANGE", "MODEOFTENDER", "METHOD_OF_PURCHASE", "FINANCIAL_POWER_CODE", "CFA_CODE", "CONCURRENCE_BY", "BUDGET_HEAD_CODE", "IS_PAC"]


# In[11]:


output_value=["TOTAL_DAYS_RANGES"]


# In[12]:


import sys


# In[17]:


input_val=sys.argv[1]
#convert input_val into a list from a string
df=pd.DataFrame(input_val)
df.columns=input_cols


# In[ ]:


cost_ranges = [(0, 1000000), (1000001, 2500000), (2500001, 5000000), (5000001, 10000000), (10000001, 50000000), (50000001, 100000000)]
cost_ranges_endcoding = ['0 - 10L', '10L - 25L', '25L - 50L', '50L - 1CR', '1CR - 5CR', '5CR - 10CR', '> 10CR']

def range_encoding(df, source_col_name, dest_col_name, ranges, encoding):
  ranges_result = []
  for val in df[iloc[0]]:
    flag = False
    for i in range(len(encoding) - 1):
      if ranges[i][0] <= val <= ranges[i][1]:
        ranges_result.append(encoding[i])
        flag = True
        break
    if not flag:
      ranges_result.append(encoding[len(encoding) - 1])

  df[dest_col_name] = ranges_result
  return df


####################################### TO BE DONE ######


# In[18]:


## call range encoding


# In[19]:


output=loaded_model.predict(df)


# In[ ]:


print(output)

