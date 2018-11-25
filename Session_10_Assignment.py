# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 19:29:13 2018

@author: Eliud Lelerai

"""

import numpy as np
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
df.info()
df.describe()
print(df.columns)


#1. Delete unnamed columns
 del df['Unnamed: 0']
 
#2. Show the distribution of male and female
Gender = pd.Categorical(df["Gender"])
Gender.describe()

#3. Show the top 5 most preferred names
sorted(df["Name"])[0:5]

#4. What is the median name occurence in the dataset

df_sorted_by_name=df.sort_values(by='Name')

df_sorted_by_name.describe()

median_name=df_sorted_by_name[df_sorted_by_name.Id==2.811921e+06]
   #The name is Kasey as given by median_name data above

#5. Distribution of male and female born count by states

pd.Categorical(df["Gender"])
pd.Categorical(df["State"])
pd.crosstab(df.State, df.Gender)