'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 7, 1D arrays in NumPy

  

'''

import numpy as np 
# import numpy package - contains many functions to work with arrays
# import (package) as (local name for the package)


#------------------------------------------------------------------------
# array creation

# arrays are similar to lists
# typically have a common data type for the entries
size_a1 = (3,)
a1 = np.zeros(size_a1,dtype=int) # array of zeros of length 3

a2 = np.zeros((3,),dtype=float)

a3 = np.zeros((3,),dtype=object) # nonuniform data types in the array


a4 = np.ones((4,),dtype = float) # array of ones

l5 = [3,4,5,10,1.3]

a5 = np.array(l5,dtype = float) # create array from list

l51 = list(a5)


a6 = np.arange(1,20,2,dtype=int) 

l6 = list(range(1,20,2))

# can also create Boolean arrays

a6_shape = np.shape(a6) # lenth of a 1d array as a tuple with 1 entry


#------------------------------------------------------------------------
# array operations

a7 = np.array([1,3,6],dtype = float)
a8 = np.array([-1,3,-4],dtype = float)


# array-array operations
a9 = a7+a8  # add entries componentwise (not concatenation)
a10 = a7-a8  # subtract entries componentwise 
a11 = a7*a8  # multiply entries componentwise 
a12 = a7/a8  # divide entries componentwise 

# number-array operations
a13 = 3+a7
a14 = 3-a7
a15 = a7-3
a16 = 3*a7
a17 = 3/a7
a18 = a7/3
a19 = a7**2
a20 = 2**a7

# test for equality

b1 = a7 == a8 # componentwise test for equality, returns a Boolean array

#if a7 == a8:   error
#    print('hello')


b2 = np.array_equal(a7,a8)


#------------------------------------------------------------------------
# array slicing

a13_0 = a13[0] # change values as with lists

a13[0] = 5

a21 = np.arange(0,20,1,dtype=int)

n = np.shape(a21)[0]

a22 = a21[0:n:2] # slice similar to lists

a23 = a21[1:n:2]

index_list_1 = [10,5,4,11,16]

a24 = a21[index_list_1]

l7 = list(range(0,20,1))

# l8 = l7[index_list_1] # error


#------------------------------------------------------------------------
# import/export

a25 = np.ones((5,),dtype = int)

np.save('week7_a25.npy',a25)
a25_loaded = np.load('week7_a25.npy')

np.savetxt('week7_a25.txt',a25) 
a25_loaded2 = np.loadtxt('week7_a25.txt')


a26 = np.array([1,1.2,'hello'],dtype= object)

np.save('week7_a26.npy',a26)
a26_loaded = np.load('week7_a26.npy',allow_pickle=True)







