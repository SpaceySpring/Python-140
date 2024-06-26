'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 8, 1D arrays in NumPy

  

'''

import numpy as np 

#-----------------------------------------------------------------------
# mask - array of Boolean values
#      - commonly associated with an array of values that is to be sliced


m1 = np.array([True,False,True],dtype =bool )

a1 = np.array([3,12,11],dtype = int)

a2 = a1[m1]


#-----------------------------------------------------------------------
# create a mask using a comparison operator

m2 = a1 > 5

a3 = a1[m2]

#---------

a4 = np.arange(2,1000,2)

m3 = a4 <= 50

a5 = a4[m3]

#-----------------------------------------------------------------------
# functions

max_a4 = np.max(a4)

min_a4 = np.min(a4)

arg_max_a4 = np.argmax(a4) # index of the largest value in the array

arg_min_a4 = np.argmin(a4) # index of the smallest value in the array

max_a4_v2 = a4[arg_max_a4]


#-------------

sum_a4 = np.sum(a4)

a5 = np.array([3,2,2],dtype = int)

prod_a5 = np.prod(a5)


#--------------
# stats functions

average_a5 = np.mean(a5) # mean or average value

var_a5 = np.var(a5) # variance of the array (measure of spread)

std_a5 = np.std(a5) # standard deviation (measure of spread)


#-----------------------------------------------------------------------
# assigning subarrays

a6 = np.zeros((6,),dtype = float)


# change the values at even indices to be 1

a7 = np.ones((3,),dtype = float)

a6[0:6:2] = a7 

# change the values at odd indices to be 1,2,3

a8 = np.array([1,2,3],dtype = float)

a6[1:6:2] = a8

#--------------

a9 = np.zeros((6,),dtype = int)

a10 = np.array([1.2,4.1,3.14],dtype = float)

a9[0:6:2] = a10


#------------------------------------------------------------------

a11 = np.array([1,2,3,4,5,6,7,8],dtype = int)

m11 = a11 > 3

m12 = a11 <= 2

m13 = np.logical_and(m11,m12)
m14 = np.logical_or(m11,m12)
m15 = np.logical_not(m11)
m16 = np.logical_xor(m11,m12)











