'''
-------------------------------------------------------
Math 140 - module 2 project 0
-------------------------------------------------------
author:   Jonathan Royal  <jkroyal@aggies.ncat.edu>       
          Juillard Bumidange <jgbumidang@aggies.ncat.edu> 
          Payton Sanford  <pcsanford@aggies.ncat.edu>                           
-------------------------------------------------------
Description: project euler

notes: - you may use code from week12.py to generate a list
         of prime numbers
       - do not use sympy or other packages with
         advanced prime number functions
-------------------------------------------------------
'''
import numpy as np

# Part a)
# - solve Project Euler problem 7 (https://projecteuler.net/problem=7)
# - hint : the answer is below 200,000
# - include a single print statement at the end to display the answer



maxN = 2000000

prime_mask = np.ones((maxN,),dtype = bool)
prime_mask[0] = False
prime_mask[1] = False



for i in range(2,maxN):
    if prime_mask[i]:
        prime_mask[i*2:maxN:i] = False

#for i in range(maxN):
#    print(i,prime_mask[i])

prime_list = []
for i in range(maxN):
    if prime_mask[i]:
        prime_list += [i]

print(prime_list[10000])



# Part b)
# - solve Project Euler problem 10 (https://projecteuler.net/problem=10)
# - include a single print statement at the end to display the answer


sop=0
for i in prime_list:
    if i < maxN:
        sop= sop+i

print(sop)


# Part c)
# - solve Project Euler problem 3 (https://projecteuler.net/problem=3)
# - hint: the answer is below 200,000
# - include a single print statement at the end to display the answer

z=600851475143
l=200000

Fac=[]
for i in prime_list:
    if z%i==0:
       Fac= Fac +[i]

abc= Fac[-1]
print(abc)       








