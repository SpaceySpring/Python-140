'''
Author : John Paul Ward

email : jpward@ncat.edu

topic :
math 140, week 13

-- programming monopoly - Project Euler 84
https://projecteuler.net/problem=84

- use pseudocode
- start small with working code
- test as you go

'''
# import statements -----------------------------------------------------------

import numpy as np

# variables -------------------------------------------------------------------

current_position = 0 # start on Go square
spaces_on_board = 41 
number_of_rolls = 10
dice_sides = 6
#space_counts = np.zeros((spaces_on_board,),dtype=float)
#space_counts = {i:0 for i in range(spaces_on_board)}
space_counts = [0 for i in range(spaces_on_board)]

# game play -------------------------------------------------------------------

for i in range(number_of_rolls):
    
    # store current position -----------
    space_counts[current_position] += 1
    
    # dice roll (To do)
    die1 = np.random.randint(1,dice_sides+1)
    die2 = np.random.randint(1,dice_sides+1)
    
    # doubles jail
        
    
    # move to new position
    current_position += die1+die2
    #current_position = current_position + die1 + die2 
    current_position = current_position % spaces_on_board
    #print(die1,die2,current_position)

    # chance

    # community chest
    



# analysis --------------------------------------------------------------------

# print(space_counts)
percentages = [space_counts[i]/number_of_rolls*100 for i in range(spaces_on_board)]
percentages = [np.around(p,3) for p in percentages]
print(percentages)

# sort by percentages


