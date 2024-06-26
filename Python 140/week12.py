'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 12

'''

import numpy as np

#------------------------------------------------
# lists
# - mutable

l1 = [1,2,3]

#------------------------------------------------
# tuples
# - immutable

t1 = (1,2,3)


#------------------------------------------------
# sets
# - collections of distinct items

s1 = set([1,2,3,4,4,4,4,4])

s2 = set([3,4,5,6])


# set difference
# elements of s1 that are not in s2
s3 = s1 - s2

# set union
# elements of either set
s4 = s1 | s2

# set intersection
# elements of both sets
s5 = s1 & s2

# symmetric difference
# elements of one set or the other, but not both
s6 = s1 ^ s2


#-------------------------------------------------
# dictionaries
# - key-value pairs
# define using { key1:value1, key2:value2    }

# dictionary of factors of integers
d1 = { 2:[1,2], 3:[1,3], 4:[1,2,4] }

factors_of_3 = d1[3]

factors_of_4 = d1[4]

# add a new key-value pair
d1[6] = [1,2,3,6]

# remove a key-value pair
del d1[3]



#-------------------------------------------------
# dictionary keys
# - number
# - strings
# - tuples
# - sets and lists are not allowed

# dictionary values
# - lists
# - numbers
# - strings

d2 = {'a':1,'b':2,'c':3}

d3 = {(1,2,3):6, (4,5):9, (4,5,6):15  }

# d4 = {[1,2,3]:6, [4,5]:9, [4,5,6]:15} # error, not allowed

print(d3[(1,2,3)])
#print(d3[3]) # error, key does not exist

# d5 = {set([1,2,3]):4 }


#--------------------------------------------------
# where to use dictionaries

# store info about customers

store = {'Tom': ['Monday', '4pm', 400, 25]}

print(store['Tom'])


# represent polynomials
# 1+2x +3x^2 +10x^10 
# list - index represents a power of x, coefficients are stored in the list 

poly_list = [1,2,3,0,0,0,0,0,0,0,10]

#value of the polynomial at x
x = 1
p1 = 0
for i in range(len(poly_list)):
    p1 += poly_list[i]*x**i
    #p1 = p1 + poly_list[i]*x**i
print('poly list',p1)



# dictionary - power is the key, coefficient is the value
poly_dict = {0:1,1:2,2:3,10:10}

p2 = 0
for key in poly_dict:
    p2 += poly_dict[key]*x**key
    #p2 = p2 + poly_dict[key]*x**key
print('poly dict',p2)


# side note
# val +=     val = val +  
# val -=     val = val -
# val *=     val = val *
# val /=     val = val /




#--------------------------------------------------
# generate a list of prime numbers

maxN = 100

prime_mask = np.ones((maxN,),dtype = bool)
prime_mask[0] = False
prime_mask[1] = False

'''
# first True value is at index 2
# mark False the multiples of 2
prime_mask[2*2:maxN:2] = False

# next True value is at index 3
# mark False the multiples of 3
prime_mask[3*2:maxN:3] = False

# next True value is at index 5
# mark False the multiples of 5
prime_mask[5*2:maxN:5] = False


print(4,prime_mask[4])
print(5,prime_mask[5])
'''

for i in range(2,maxN):
    if prime_mask[i]:
        prime_mask[i*2:maxN:i] = False

#for i in range(maxN):
#    print(i,prime_mask[i])

prime_list = []
for i in range(maxN):
    if prime_mask[i]:
        prime_list += [i]

# list comprehension
prime_list_v2 = [i for i in range(maxN) if  prime_mask[i]  ]




