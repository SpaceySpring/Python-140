'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 5, 

- project euler  https://projecteuler.net/

- code golf https://codegolf.stackexchange.com

'''

#------------------------------------------------------------------
'''
PE problem 1

If we list all the natural numbers below 10 that are 
multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

#mult_of_3 = list(range(3,1000,3))

#mult_of_5 = list(range(5,1000,5))


mult_3_or_5 = []

for i in range(3,10,1):
    if i % 3 == 0 or i % 5 == 0:
        mult_3_or_5.append(i)
        
summ = sum(mult_3_or_5)
print(mult_3_or_5)
    
    
#------------------------------------------------------------------
'''
code golf

add numbers in a list

'''

L = [3,4,10,15,16,25]


# 1st attempt
sum1 = 0

for num in L:
    sum1 = sum1 + num



# revised
sum2 = sum(L)
    

#------------------------------------------------------------------
'''
code golf

conditional statements

'''

# compute the month from the day of the year

day_of_year = 60

month_days = [31,28,31,30,31,30,31,31,30,31,30,31]



# 1st attempt
if  0 <= day_of_year and day_of_year <= month_days[0]:
    month = 'jan'
elif  month_days[0] < day_of_year and day_of_year <= sum(month_days[0:2]):
    month = 'feb'
elif  sum(month_days[0:2]) < day_of_year and day_of_year <= sum(month_days[0:3]):
    month = 'mar' 
#etc


# revised
if  day_of_year <= month_days[0]:
    month = 'jan'
elif day_of_year <= sum(month_days[0:2]):
    month = 'feb'
elif day_of_year <= sum(month_days[0:3]):
    month = 'mar' 
#etc


#------------------------------------------------------------------
'''
PE problem 2

Each new term in the Fibonacci sequence is generated by adding 
the previous two terms. By starting with 1 and 2, the first 10 
terms will be:

1,2,3,5,8,13,21,34,55,89,....

By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.

'''


fib = [1,2]

for i in range(2,31+1,1):
    val = fib[-1] + fib[-2]
    fib.append(val)

print(fib[-1])

# binary search

# indices where value below 4,000,000
# 
# indices where value above 4,000,000
# 

