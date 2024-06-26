'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 3, Conditionals  

- 

'''

#-------------------------------------------------------
# data type - Boolean

b1 = True

b2 = False

bl = [True,False,b1,b2]


#-------------------------------------------------------
# logic operators

b3 = True and True

b4 = True and False

b5 = False and False

b6 = True and True and False

b7 = True or True

b71 = True or False

b8 = 2 in [2,6,10]

b9 = 'hello' in [2,3,4,'world',True]


#-------------------------------------------------------
# comparison operators


b10 = 2 < 10 # less than, returns boolean

b11 = 10 < 10

b12 = 2 <= 10 # less than or equal

b13 = 3 <= 3

b14 = 4 > 1 # greater than 

b15 = 4 >= 5 # greater than or equal

b16 = 4 == 5 # test for equality

b17 = 5 == 5

i1 = 5
i2 = 7

b18 = i1 == i2

b19 = 5 == 5.0

b20 = 5 == 5.1

b21 = 4 != 5 # not equal

#--------------------------------------------------------
# control structure - conditional - if statements

i3 = 7
i4 = 5

if i3 > i4:  #(if, expression evalutes to a boolean, colon)
    print('hello world') # indent 4 spaces or tab
    print('hello world')
    print('hello world')
    print('hello world')
    print('hello world')

print('Hello World')



cond1 = 3 < 4 and 5 <= 6
if cond1:
    print('123')


cond2 = 3 < 4
cond3 = 5 <= 6
if cond2 and cond3:
    print(234)



#--------------------------------------------------------
# control structure - conditional - if-else

if 3<4:
    print('3<4')
else:
    print('3 is greater than or equal to 4')


if 5<4:
    print('5<4')
else:
    print('5 is greater than or equal to 4')



#--------------------------------------------------------
# control structure - conditional - if-elif-else

if False:
    print(1)
elif False:   # elif : else if
    print(2)  # if the first condition was not met and
              # the current condition is met
elif False:
    print(3) # if the previous two conditions were False
             # and the current condition is True
elif False:
    print(4)
elif False:
    print(5)
elif False:
    print(6)
elif False:
    print(7)
else:
    print(8) # if no previous condition was met



#--------------------------------------------------------
# piecewise function 1

x = 2

if x < 0:
    f = x**2
elif x < 1:
    f = x-5
elif x < 4:    
    f = x**3
else:
    f = 5
    
print(x,f)


#--------------------------------------------------------
# piecewise function 2

x1 = -4

if x1 < 0:
    f1 = -x1
elif x1 >= 0:
    f1 = x1
    
print(x1,f1)


#--------------------------------------------------------
# piecewise function 3

x2 = 6

if x2 < 0:
    f2 = -x2
elif x2<4:
    f2 = x2
else:
    f2 = 8-x2
    
    
print(x2,f2)


#----------------------------------------------
# leap year calculator

year = 2008389232

if year % 4 != 0: # year not divisible by 4
    print(year,'common year','condition 1')
elif year % 100 != 0: # year not divisible by 100
    print(year,'leap year', 'condition 2')
elif year % 400 != 0: # year not divisible by 400
    print(year,'common year', 'condition 3')
else:
    print(year,'leap year', 'condition 4')












