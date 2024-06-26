'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 4, for loops 

'''

#--------------------------------------------------------
# casting to int using int()

f1 = 3.14

i1 = int(f1)

f2 = 4.89

i2 = int(f2) 


#---------------------------------------------------------
# range() and list() functions
# range(start,end,increment)

r1 = range(0,10,1)

l1 = list(r1)

r2 = range(0,20,2) # even integers

l2 = list(r2)

r3 = range(1,20,2) # odd integers

l3 = list(r3)

l4 = list(range(3,50,3)) # multiples of 3

l5 = list(range(5,-1,-1))

l6 = list(range(5,-5,-1))

l7 = list(range(5,-5,-2))

#---------------------------------------------------------
# for loops


# the variable i takes the 3 values in the list sequentially and the 
# code inside is excuted for each value 
for i in [5,8,10]:
    print(i)

'''
#the above loop is equivalent to 3 print statements

# i=5
print(5) # print(i)
# i= 8
print(8) # print(i)
# i= 10
print(10) # print(i)
'''


# the variable my_variable takes the 3 values in the list sequentially and the 
# code inside is excuted for each value  
for my_variable in [3,'hello',10]:
    print(my_variable)


# the variable j takes the values specified by the range() function
# in order and the code inside is excuted for each value  
    for j in range(3,15,4):
        print(j)



#---------------------------------------------------------
# for loops -  building lists - squares

# find the squares of the first 5 integers
squares = []

for i in range(0,5,1):
    square = i**2
    #squares = squares + [square] # option 1
    squares.append(square)      # option 2
    print(squares)
    


#---------------------------------------------------------
# for loops -  building lists - factorials

# want to compute a list of factorials    

# factorials
# 4! = 4*3*2*1
# 5! = 5*4*3*2*1 = 5*4!
# 6! = 6*5*4*3*2*1 = 6*5!
# n! = n * (n-1)!

# factorials = [1,1,2,6,24] 


'''
# how this works

factorials = [1,1] # factorials for 0,1

# append 2!
#fac = 2*1 
fac = 2*factorials[-1]  # 2*1!
factorials.append(fac)

# append 3!
#fac = 3*2*1
fac = 3*factorials[-1] # 3*2!
factorials.append(fac)

# append 4!
#fac = 4*3*2*1
fac = 4*factorials[-1] # 4*3!
factorials.append(fac)

# append 5!
#fac = 5*4*3*2*1
fac = 5*factorials[-1] # 5*4!
factorials.append(fac)
'''

factorials = [1,1] # factorials for 0,1

for i in range(2,6,1):
    fac = i*factorials[-1] 
    factorials.append(fac)
    print(factorials)


#---------------------------------------------------------
# for loops -  building lists - Fibonacci sequence
# https://en.wikipedia.org/wiki/Fibonacci_number
# recurrece F_n = F_(n-1) + F_(n-2)

fibonacci = [0,1] # [F_0,F_1]

'''
# append F_2
# fib = F_0 + F_1
fib = fibonacci[-2] + fibonacci[-1]
fibonacci.append(fib)

# append F_3
# fib = F_1 + F_2 
fib = fibonacci[-2] + fibonacci[-1]
fibonacci.append(fib)

# append F_4
# fib = F_2 + F_3 
fib = fibonacci[-2] + fibonacci[-1]
fibonacci.append(fib)
'''

for i in range(2,30,1):
    fib = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(fib)
    print(fibonacci)


#---------------------------------------------------------
# for loops -  building lists - Fibonacci sequence
# using a formula 
# golden ratio: phi = (1+sqrt(5))/2
# F_n =  floor( phi^n/sqrt(5) +1/2   )

fibonacci1 = [0,1]

phi = (1 + 5**0.5)/2

for n in range(2,10,1):
    fib1 = (phi**n)/(5**0.5) + 1/2 
    fib2 = int(fib1) # round down
    fibonacci1.append(fib2)
    print(fibonacci1)


#---------------------------------------------------------
# for loops -  building lists - sylvester sequence
# A000058, https://en.wikipedia.org/wiki/List_of_integer_sequences
# The code A000058 is the OEIS index
# https://oeis.org/

sylvester = [5]

for n in range(1,10,1):
    syl = sylvester[-1]**2 - sylvester[-1] +1
    sylvester.append(syl)
    print(sylvester)
    
    
    


