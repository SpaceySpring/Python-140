'''
-------------------------------------------------------
Math 140 - module 0 project 3
-------------------------------------------------------
author:   Your Name  <yourEmail@ncat.edu>        
          Your Name  <yourEmail@ncat.edu>  
          Your Name  <yourEmail@ncat.edu>                           
-------------------------------------------------------
Description:
    Working with for loops to build lists
    
    
Background: 
https://en.wikipedia.org/wiki/Prime_number
A prime numbers is a natural number greater than 1 that
is not a product of two smaller natural numbers
2,3,5,7,11

https://en.wikipedia.org/wiki/Wilson%27s_theorem
Prime test using Wilson's theorem


Note :
    In some calculations, it may be helpful to introduce
    additional variables. However, make sure that the
    names do not overlap with those requested
    in the project
    
-------------------------------------------------------
'''

'''
In the first part of the project, we are testing if a 
number is prime or composite by looking at the remainders
when that number is divided by smaller numbers.
Note that we only have to check up to the square root
of the number.
'''

# Part a) ----------------------------------------------------
# variable name : number1
# define an integer between 2 and 350


number1 = 72


# Part b) ----------------------------------------------------
# variable name : number1_max
# find the square root of number1 and cast to an integer

number1_max = int(number1**(1/2))




# Part c) ----------------------------------------------------
# variable name : number1_remainders
# use a for loop to build a list of the remainders 
# when number1 is divided by the numbers 2,3,4,5,...,number1_max
# note: we want the remainder for number1_max included in the list
number1_remainders = []

for i in range(2,number1_max+1,1):
    number1_remainder = number1%i
    number1_remainders.append(number1_remainder)
    
    
    

# Part d) ----------------------------------------------------
# variable name : number1_remainders_min
# find the minimum of number1_remainders

number1_remainders_min = min(number1_remainders)

# Part e) ----------------------------------------------------
# Use a conditional to see if number1_remainders_min is 0 
# or not. 
# The conditional should print number1 together with its primality.

# Examples
# 
# number1     what is printed
#--------     ----------------
# 4           4 composite
# 5           5 prime
# 210         210 composite

conditional_min = []

if number1_remainders_min == 0:
    conditional_min = [number1, 'prime']
elif number1_remainders_min > 0:
    conditional_min = [number1, 'composite']
    


#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

'''
In this part of the project, we are testing if a 
number is prime or not, making use of Wilson's theorem.
'''

# Part a) ----------------------------------------------------
# variable name : number2
# define an integer between 2 and 350


number2 = 127



# Part b) ----------------------------------------------------
# variable name : wilson_list
# write a for loop to create the following sequence
# the index 0 term is 1
# the index 1 term is 1
# the index n>1 term is the remainder when n! is divided by number2
# compute the list items using two steps in the for loop
#    - multiply the previous term by the current index (which is n)
#    - find the remainder when this number is divided by number2
#
# compute number2 terms of this seqeunce (i.e. the length of the
#   list should be number2)


# Examples
# 
# number2     wilson_list
#--------     ----------------
# 4           [1,1,2,2]
# 5           [1,1,2,1,4]
# 6           [1,1,2,0,0,0]
# 11          [1, 1, 2, 6, 2, 10, 5, 2, 5, 1, 10]
# 25          [1, 1, 2, 6, 24, 20, 20, 15, 20, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


wilson_list = [1,1]
for i in range (2,number2):
    fac = i*wilson_list[-1]%number2
    wilson_list.append(fac)
    


# Part c) ----------------------------------------------------
# Use a conditional to see if the last term of the sequence
# wilson_list is number2-1 or not 
# The conditional should print number2 together with its primality.

# Examples
# 
# number2     what is printed
#--------     ----------------
# 4           4 composite
# 5           5 prime
# 210         210 composite

conditional2 = []

if wilson_list[-1] == 0:
    conditional2 = [number2, 'prime']
elif wilson_list[-1] > 0:
    conditional2 = [number2, 'composite']



#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

'''
Bonus:
In this part of the project, you are asked to build a seqeunce from OEIS

A005165   Alternating factorial
'''

# (bonus) ----------------------------------------------------
# variable name : alt_fact
# build a list of alternating factorials of length 15
# - use a single for loop
# - do not use conditional statements
# - hint: you may need an additional variable that is updated in the for loop


alt_fact = []


