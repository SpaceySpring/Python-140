'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 9, 2D arrays in NumPy

'''

# all import statements
import numpy as np
import pandas as pd  # Pandas package https://pandas.pydata.org/

#-------------------------------------------------------------------
# array creation

# create a 2d array from a list of lists
a1 = np.array([[1,2],[3,4],[5,6]],dtype = float)

a2 = np.zeros((3,4),dtype=int)

a3 = np.ones((3,4),dtype=int)

a1_shape = np.shape(a1)

a1_len = len(a1) # how to find rows

_,c2=np.shape(a1) # both are how to find columes
c1=np.shape(a2)[1]

#--------------------------------------------------------------------
# access values

a1_2_0 = a1[2,0]

a1[2,0] = 7


#--------------------------------------------------------------------
# functions

a1_sum = np.sum(a1)

a1_sum_0 = np.sum(a1,axis=0) # sums columns of the array

a1_sum_1 = np.sum(a1,axis=1) # sums rows of the array

a1_max = np.max(a1)

a1_max_0 = np.max(a1,axis=0)

a1_max_1 = np.max(a1,axis=1)

a1_prod = np.prod(a1)

a1_prod_0 = np.prod(a1,axis=0)

a1_mean = np.mean(a1)

a1_mean_0 = np.mean(a1,axis = 0)


#-------------------------------------------------------------------
# slicing


a4 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],dtype = int)

a4_s1 = a4[0:4:2,:] # slicing rows, keep all columns

a4_s2 = a4[:,[1,2,0]] # slice with list

a4_s3 = a4[[0,1],:]


#-------------------------------------------------------------------
# import using pandas

# import data from a file as a dataframe
# file name : 'iris.data'
# header : None, 0,1,2,3... depending on how many rows the header is in the 
#                           file

# option 1 : from a file
#df1 = pd.read_csv('iris.data',header=None)

# option 2 : from a url (website)
url1 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df1 = pd.read_csv(url1,header=None)

# extract the values from the dataframe as an array
arr_iris = df1.values 

'''
column 0 : sepal length in cm
column 1 : sepal width in cm
column 2 : petal length in cm
column 3 : petal width in cm
column 4 : class: Iris Setosa, Iris Versicolour, Iris Virginica
'''

#---------

mask_setosa = arr_iris[:,4] == 'Iris-setosa'

arr_setosa = arr_iris[mask_setosa,:]

sepal_len_mean_setosa = np.mean(arr_setosa[:,0])

sepal_len_var_setosa = np.var(arr_setosa[:,0])

#----------

mask_versi = arr_iris[:,4] == 'Iris-versicolor'

arr_versi = arr_iris[mask_versi,:]

sepal_len_mean_versi = np.mean(arr_versi[:,0])

sepal_len_var_versi = np.var(arr_versi[:,0])

#----------

mask_virg = arr_iris[:,4] == 'Iris-virginica'

arr_virg = arr_iris[mask_virg,:]

sepal_len_mean_virg = np.mean(arr_virg[:,0])

sepal_len_var_virg = np.var(arr_virg[:,0])

#------------------------------------------------

means_setosa = np.mean(arr_setosa[:,0:4],axis = 0)
var_setosa = np.var(arr_setosa[:,0:4],axis = 0)

means_versi = np.mean(arr_versi[:,0:4],axis = 0)
var_versi = np.var(arr_versi[:,0:4],axis = 0)

means_virg = np.mean(arr_virg[:,0:4],axis = 0)
var_virg = np.var(arr_virg[:,0:4],axis = 0)











