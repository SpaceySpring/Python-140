'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 11, combined control structures

'''

import numpy as np

#--------------------------------------------------------------
# nested for loops

for i in range(0,4): # i=0,1,2,3
    for j in range(0,3): # j = 0,1,2
        print('i=',i,', j=',j)


#--------------------------------------------------------------
# note we can use nested for loops to scan through all
# indices of a 2d array

arr1 = np.zeros((4,3),dtype=int)

for i in range(0,4): # i=0,1,2,3
    for j in range(0,3): # j = 0,1,2
        arr1[i,j] = i*j


#--------------------------------------------------------------
# np.max() for a 1d array 
# find the max value of arr2

arr2 = np.array([1,5,3,7,4],dtype = int)

max1 = arr2[0] # initialize with the first value

arr2_len, = np.shape(arr2)
for i in range(1,arr2_len): # scan remaining values in arr2
    print('i=',i,',current max=',max1)
    if arr2[i] > max1:
        max1 = arr2[i] # update the max value
        print('i=',i,',updated max=',max1)


#--------------------------------------------------------------
# function to find the max of a 1d array

def max_ward_1d(arr_1d_loc):
    max_1d_loc = arr_1d_loc[0]
    
    arr_1d_loc_len, = np.shape(arr_1d_loc)
    for i in range(1,arr_1d_loc_len): 
        if arr_1d_loc[i] > max_1d_loc:
            max_1d_loc = arr_1d_loc[i]
    return(max_1d_loc)


max_test_1d = max_ward_1d(arr2)

    
#--------------------------------------------------------------
# function to find the max of a 2d array

def max_ward_2d(arr_2d_loc):
    max_2d_loc = arr_2d_loc[0,0]
    
    rows,cols = np.shape(arr_2d_loc)
    for i in range(0,rows):
        for j in range(0,cols):
            if arr_2d_loc[i,j] > max_2d_loc:
                max_2d_loc = arr_2d_loc[i,j]
    return(max_2d_loc)


max_test_2d = max_ward_2d(arr1)


#--------------------------------------------------------------
# argmax for 1d arrays - examples

arr3 = np.array([1,2,3,6,2,2],dtype = int)

amax3 = np.argmax(arr3)

arr4 = np.array([1,2,6,6,2,2],dtype = int)

amax4 = np.argmax(arr4) # only the first occurance is returned

#--------------------------------------------------------------
# argmax for 1d arrays


max2 = arr4[0] # initialize with the first value
max2_ind = 0

arr4_len, = np.shape(arr4)
for i in range(1,arr4_len): # scan remaining values in arr2
    print('i=',i,',current max=',max2,',current max ind=',max2_ind)
    if arr4[i] > max2:
        max2_ind = i
        max2 = arr4[i] # update the max value
        print('i=',i,',updated max=',max2,',updated max ind=',max2_ind)


#---------------------------------------------------------------
# np.sum() for 2d arrays

def sum_ward_2d(arr_loc):
    summ = 0 # initialize sum
    rows,cols = np.shape(arr_loc) # compute shape
    
    for i in range(rows):   
        for j in range(cols):
            summ += arr_loc[i,j] # add the i,j entry to summ
            
    return(summ)


#---------------------------------------------------------------
# np.sum() for 2d arrays - sum columns (axis=0)

def sum_ward_2d_axis0(arr_loc):
    
    rows,cols = np.shape(arr_loc) # compute shape
    summ = np.zeros((cols,),dtype = float) # initialize sum
    for i in range(rows):   
            summ += arr_loc[i,:] # add row i to summ
    return(summ)

arr5 = np.ones((7,2),dtype = int)

arr5_sum1 = np.sum(arr5,axis=0)

arr5_sum2 = sum_ward_2d_axis0(arr5)



#---------------------------------------------------------------
# create mask


# def <function name> ( local variables  ):
def array_comp(arr_loc,val):
    # arr_loc - local varaible name for the array we want a mask for
    # val - value to compare with
    
    # when calling array_comp(arr6,2)
    # arr_loc = arr6
    # val = 2

    # when calling array_comp(arr7,6)
    # arr_loc = arr7
    # val = 6

    
    len_arr_loc, = np.shape(arr_loc)
    mask_loc = np.zeros((len_arr_loc, ),dtype = bool)
    
    for i in range(len_arr_loc):
        if arr_loc[i] == val:
            mask_loc[i] = True
        else:
            mask_loc[i] = False
    return(mask_loc)


arr6 = np.array([1,2,6,6,2,2],dtype = int)

mask6_1 = arr6 == 2
mask6_2 = array_comp(arr6,2)

arr7 = np.array([1,7,6,6,2,2],dtype = int)

mask7_1 = arr7 == 6
mask7_2 = array_comp(arr7,6)







