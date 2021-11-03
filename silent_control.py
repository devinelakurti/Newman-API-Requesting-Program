#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import pyreadstat

df, meta = pyreadstat.read_sav("C:/Users/nelakurti.1/Downloads/Mutation coding.sav") #creates a pandas dataframe

ap=(df['MutationDescription'].values == '')
count = np.count_nonzero(ap)
print(count)
[i for i, x in enumerate(ap) if x] #BEFORE
df.head()

df['ExtractedCDS'] = df['MutationCDS'].str[-3:] #extracts _>_ from MutationCDS to ExtractedDS
df['OG_AA'] = df['MutationAA'].str[2:] # extracts the characters after p. in MutationAA
df['OG_AA'] = df['OG_AA'].str.replace('\d+', '') #removes any and all digits in the extracted verison of MutationAA
df['Mutated_AA'] = df['OG_AA'].str[-1:] #seperates the two digits
df['OG_AA'] = df['OG_AA'].str[:-1] #seperates the two digits

ap=(df['MutationDescription'].values == '')
count = np.count_nonzero(ap)
print(count)
[i for i, x in enumerate(ap) if x] #AFTER
df.head()

# In[5]:

Silent = df[df['Mutated_AA'] == '=']
Silent_counts = Silent.groupby(['MutationDescription', 'OG_AA'])[['OG_AA']].count()
print(Silent_counts)
Silent_counts.to_csv("C:/Users/nelakurti.1/Downloads/SilentAA_counts.csv")

# In[ ]:

