'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 6, 

 - functions
 - tuples

'''

#---------------------------------------------------
# tuples - ordered collection of items (similar to a list, but immutable) 
# parentheses instead of square brackets for lists

t1 = (2,3,4,'hello',4.0)

t1_1 = t1[1]

# t1[1] = 5  #error

t2 = t1[0:5:2]

t3 = t1 + t2 # concatenation
 
n1 = (3+5)  # computation grouped with parentheses

t4 = (3+5,) # tuple with 1 item

t5 = (7,)  # tuple with 1 item


#t5.append(5) # error

t5 = t5 + (5,)

l1 = [2,3,4]

l1 = l1 + [5]

#t5 = t5 + (5) # error

n2 = 5 + 4.0

t6 = (1,2,1,1,1,8)

t61 = t6.count(1)

t68 = t6.index(8)


t7 = (3,4.0,'hello')

t71,t72,t73 = t7  # tuple unpacking

t8 = (3,4,5)

t81,_,t83 = t8 # tuple unpacking

t9 = (3,6,9)

t91,t92,_ = t9 # tuple unpacking

a,z,c = t7 


#----------------------------------------------------------------------------
# functions
# def fcn_name(inputs):
#     computations
#     return(what is to be returned)

# num1,num2,val are local variables

def add1(num1,num2): # function to add two numbers
    val = num1 + num2
    return(val)

# s1, s2 are global variables
    
s1 = add1(4,5)

s2 = add1(5,9.0)



#--------------------

# list1, summ1 are local variables

def add2(list1):
    #print(list1)
    summ1 = 0  # initialize sum to be 0
    for i in list1:
        summ1 = summ1 + i
        #print(i,summ1)
    return(summ1)


l2 = [4,5,5,6,6,6,6]
s3 = add2(l2)

#l3 = [1,2,3]
#s4 = add2(l3)
    
    
#--------------------

def add_mult(num1,num2):
    val1 = num1 + num2
    val2 = num1 * num2
    return(val1,val2)

u1 = add_mult(5,6)

s4,_ = add_mult(7,8)

_,p1 = add_mult(56,2)


#--------------------


#---------------------------------------------------------
'''
# Recall from week 4 
# for loops -  building lists - squares

# find the squares of the first 5 integers
squares = []

for i in range(0,5,1):
    square = i**2
    #squares = squares + [square] # option 1
    squares.append(square)      # option 2
    print(squares)
'''


def squares(maxN):
    # input : positive integer
    # output : list of the squares of the first maxN integers
    squares = []
    for i in range(0,maxN,1):
        square = i**2
        #squares = squares + [square] # option 1
        squares += [square] # option 2
    return(squares)


sq1 = squares(10)












