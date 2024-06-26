'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 10, 2D arrays in NumPy

Data from https://archive.ics.uci.edu/ml/datasets/Bank+Marketing


Input variables:
    
# bank client data:----------------------------------------------------------
1 - age (numeric)
2 - job : type of job (categorical: 'admin.','blue-collar','entrepreneur',
     'housemaid','management','retired','self-employed','services','student',
     'technician','unemployed','unknown')
3 - marital : marital status (categorical: 'divorced','married','single',
            'unknown'; note: 'divorced' means divorced or widowed)
4 - education (categorical: 'basic.4y','basic.6y','basic.9y','high.school',
              'illiterate','professional.course','university.degree','unknown')
5 - default: has credit in default? (categorical: 'no','yes','unknown')
6 - housing: has housing loan? (categorical: 'no','yes','unknown')
7 - loan: has personal loan? (categorical: 'no','yes','unknown')
# related with the last contact of the current campaign:
8 - contact: contact communication type (categorical: 'cellular','telephone')
9 - month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 
            'nov', 'dec')
10 - day_of_week: last contact day of the week (categorical: 
                                'mon','tue','wed','thu','fri')
11 - duration: last contact duration, in seconds (numeric). 
      Important note: this attribute highly affects the output target 
      (e.g., if duration=0 then y='no'). Yet, the duration is not known 
      before a call is performed. Also, after the end of the call y 
      is obviously known. Thus, this input should only be included 
      for benchmark purposes and should be discarded if the intention 
      is to have a realistic predictive model.
      
      
# other attributes:----------------------------------------------------------
12 - campaign: number of contacts performed during this campaign and for this
      client (numeric, includes last contact)
13 - pdays: number of days that passed by after the client was last contacted
     from a previous campaign (numeric; 999 means client was not previously 
                                contacted)
14 - previous: number of contacts performed before this campaign and for 
     this client (numeric)
15 - poutcome: outcome of the previous marketing campaign (categorical: 
     'failure','nonexistent','success')
    
# social and economic context attributes-------------------------------------
16 - emp.var.rate: employment variation rate - quarterly indicator (numeric)
17 - cons.price.idx: consumer price index - monthly indicator (numeric)
18 - cons.conf.idx: consumer confidence index - monthly indicator (numeric)
19 - euribor3m: euribor 3 month rate - daily indicator (numeric)
20 - nr.employed: number of employees - quarterly indicator (numeric)

Output variable (desired target):-------------------------------------------
21 - y - has the client subscribed a term deposit? (binary: 'yes','no')

'''

# all import statements
import numpy as np
import pandas as pd  # Pandas package https://pandas.pydata.org/

#-------------------------------------------------------------------
# 

# import the data as a dataframe using Pandas
url1 = 'bank-additional-full.csv'
#df1 = pd.read_csv(url1,header=0)
df1 = pd.read_csv(url1,delimiter=';',header=0)

# extract the values from the dataframe as an array
arr_bank = df1.values 


#--------------------------------------------------------------------
# what are all of the job types?

# set is a unordered collection of distinct items 
# converting to a set removes duplicates

jobs_column = arr_bank[:,1]

jobs_set = set(jobs_column)

jobs_list = list(jobs_set)


contact_column = arr_bank[:,7]

contact_set = set(contact_column)


#--------------------------------------------------------------------
# sorting by a particular column by sorting indices

# sort the array by age (first column)

sorted_age_ind = np.argsort(arr_bank[:,0])

arr_bank_sorted_age = arr_bank[sorted_age_ind,:]


# sort by consumer price index (column 16)

sorted_cpi_ind = np.argsort(arr_bank[:,16])

arr_bank_sorted_cpi = arr_bank[sorted_cpi_ind,:]


#--------------------------------------------------------------------
# find people between ages 20 and 25 using masks

mask_age_20p = arr_bank[:,0] >= 20

mask_age_u25 = arr_bank[:,0] <= 25

mask_age_20to25 = np.logical_and(mask_age_20p,mask_age_u25)

arr_bank_age_20to25 = arr_bank[mask_age_20to25,:]


#--------------------------------------------------------------------
# find people under 20 or over 55 using masks

mask_age_u20 = arr_bank[:,0] <= 20

mask_age_55p = arr_bank[:,0] >= 55

mask_age_u20or55p = np.logical_or(mask_age_u20,mask_age_55p)

arr_bank_age_u20or55p = arr_bank[mask_age_u20or55p,:]


#--------------------------------------------------------------------
# find people strictly under 20 or strictly over 25  (not including 20 or 25)

mask_age_u20or25p = np.logical_not(mask_age_20to25)

arr_bank_u20or25p = arr_bank[mask_age_u20or25p,:]


#--------------------------------------------------------------------
# find people who are either students or under 25 but not both

mask_students = arr_bank[:,1] == 'student'

mask_students_xor_u25 = np.logical_xor(mask_students,mask_age_u25)

arr_bank_students_xor_u25 = arr_bank[mask_students_xor_u25,:]


#--------------------------------------------------------------------
# how many people are either students or under 25 but not both?

num_students_xor_u25 = np.sum(mask_students_xor_u25)






