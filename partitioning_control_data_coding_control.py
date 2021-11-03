#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
import pyreadstat
import numpy as np

df, meta = pyreadstat.read_sav("C:/Users/nelakurti.1/Downloads/Mutation coding.sav")

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

# In[7]:

ExtractedCDS_counts = df.groupby(['MutationDescription', 'ExtractedCDS'])[['ExtractedCDS']].count()
print(ExtractedCDS_counts)
ExtractedCDS_counts.to_csv("C:/Users/nelakurti.1/Downloads/ExtractedCDS_counts.csv")

# In[11]:

df.OG_AA.unique()
OG_AA_counts = df.groupby(['MutationDescription', 'OG_AA'])[['OG_AA']].count()
print(OG_AA_counts)
OG_AA_counts.to_csv("C:/Users/nelakurti.1/Downloads/OG_AA_counts.csv")

# In[15]:

df['Mutated_AA'] = np.where((df['Mutated_AA'] == 'OG_AA'), #Identifies the case to apply to
                           df['OG_AA'],      #This is the value that is inserted
                           df['Mutated_AA'])      #This is the column that is affected
df.head()

# In[16]:

MutatedAA_counts = df.groupby(['MutationDescription', 'Mutated_AA'])[['Mutated_AA']].count()
print(MutatedAA_counts)
MutatedAA_counts.to_csv("C:/Users/nelakurti.1/Downloads/MutatedAA_counts.csv")

