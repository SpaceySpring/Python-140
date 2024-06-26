'''
-------------------------------------------------------
Math 140 - module 0 project 5
-------------------------------------------------------
author:   Payton Sanford  <pcsanford@aggies.ncat.edu>        
                         
-------------------------------------------------------
Description:

Writing functions
    
-------------------------------------------------------
'''


#------------------------------------------------------
#------------------------------------------------------

# Part a)
# create the following function
# function name: factors
# input: n (an integer greater than 1)
# output: a list of the factors of n (including 1 and n)

def factors(n):
    factor = []
    for i in range(1,n+1,1):
        if n % i == 0:
            factor.append(i)
    return (factor)


#------------------------------------------------------
#------------------------------------------------------

# Part b)
# create the following function
# function name: isprime
# input: n (an integer greater than 1)
# output: a Boolean value (True if n is prime or 
#                           False if n is composite) 

def isprime(n):
    number1_max = int(n**(1/2))

    number1_remainders = []

    for i in range(2,number1_max+1,1):
        number1_remainder = n%i
        number1_remainders.append(number1_remainder)
    
    number1_remainders_min = min(number1_remainders)

    if number1_remainders_min == 0:
        return False
    elif number1_remainders_min > 0:
        return True


#------------------------------------------------------
#------------------------------------------------------

# Part c)
# create the following function
# function name: month
# input: n (an integer between 1 and 365)
# output: the month (as a string) corresponding to the 
#          nth day of the year



def month(n):
    month_list1 = [31,28,31,30,31,30,31,31,30,31,30,31] 
    if n - sum(month_list1[0:1])<0 :
        return 'Jan'
    elif n - sum(month_list1[0:2])<0 :
        return 'Feb'
    elif n - sum(month_list1[0:3])<0 :
        return 'Mar'
    elif n - sum(month_list1[0:4])<0 :
        return 'Apr'
    elif n - sum(month_list1[0:5])<0 :
        return 'May'
    elif n - sum(month_list1[0:6])<0 :
        return 'Jun'
    elif n - sum(month_list1[0:7])<0 :
        return 'Jul'
    elif n - sum(month_list1[0:8])<0 :
        return 'Aug'
    elif n - sum(month_list1[0:9])<0 :
        return 'Sep'
    elif n - sum(month_list1[0:10])<0 :
        return 'Oct'
    elif n - sum(month_list1[0:11])<0 :
        return 'Nov'
    elif n - sum(month_list1[0:12])<0 :
        return 'Dec'


#------------------------------------------------------
#------------------------------------------------------

# Part d)
# create the following function
# function name: fact
# input: n (an integer greater than 1)
# output: a list of the factorials  0!,1!,2!,3!,...,n!



def fact(n):
    factorials = [1,1]

    for i in range(2,n+1,1):
        fac = i*factorials[-1] 
        factorials.append(fac)
    return factorials


#------------------------------------------------------
#------------------------------------------------------

# Part e)
# create the following function
# function name: math140
# input: None
# output: your name (as a string)

def math140():
    return 'Payton Sanford'
