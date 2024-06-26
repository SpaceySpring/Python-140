'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 2, Lists  

- 

'''

#---------------------------------------------------------------------
# lists denoted with square brackets
# items separated by commas

l1 = [2,3,5,17]

l2 = ['hello', 'world']

l3 = [2,5,'hello']

l4 = [2.5,17,1,-4,52]

# ----------------------------------------------------------------------
# builtin functions

min_l1 = min(l1) # minimum number in a list of numbers

max_l1 = max(l1) # maximum number in a list of numbers

sort_l4 = sorted(l4) # sorted in ascending order

# sorted function takes 2 arguments : list to be sorted , reverse parameter
# by default reverse=False
# only need to specify reverse=True when we want revserse order

sort_l4_for = sorted(l4,reverse=False) # by default reverse=False

sort_l4_rev = sorted(l4,reverse=True) # sort in decending order

sum_l4 = sum(l4)

len_l4 = len(l4)

#-----------------------------------------------------------------------
# list operations

# l1[ index of the location]

first_l1 = l1[0] 

third_l1 = l1[2] # extract an item at a given index

l1[2] = 89 # replace an item at a given index


l5 = l1 + l4  # list concatenation

l6 = l2 + ['math140'] + ['math','140']


# negative index 

last_l1 = l1[-1] # last item in list l1

next_last_l1 = l1[-2] 


#-----------------------------------------------------------------------
# slicing
#  L[starting index : ending index: increment ]

l7 = l5[0:3] # items of index 0,1,2

l8 = l5[2:5] # items of index 2,3,4

l9 = l4[0:4:2] # items of index 0,2

l10 = l5[1:6:2] # items of index 1,3,5

l11 = l5[1:8:3] # items of index 1,4,7

l12 = l5[8:0:-1] # reverse order slice
                 # items of index 8,7,6,5,4,3,2,1

l_ex = l5[0:-1:-1]

l_ex2 = l5[-1:-10:-1]

l_shortcut = l5[::1]

l14 = l5[-1:-len(l5)-1:-1] # full list reverse order slice
                 # items of index 8,7,6,5,4,3,2,1,0
                 
l15 = l5[8:0:1]


#-----------------------------------------------------------------------                 
# class methods listname.function()

# find the index of 17 in list l4
ind17_l4 = l4.index(17)

# find the index of -4 in list l4
indn4_l4 = l4.index(-4)

# add 'math140' to list l2

# before we append l2 = ['hello', 'world']
l2.append('math140') # same as l2 = l2 + ['math140']
# after we append l2 = ['hello', 'world','math140']


l2.append('math')

# ind-4_l4 = 4

l13 = [1,1,1,1,2,2,2,2,2,2,3,3]

c1 = l13.count(1)

c2 = l13.count(2)

c3 = l13.count(3)























