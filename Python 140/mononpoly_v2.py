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
number_of_rolls = 10**6
dice_sides = 6
#space_counts = np.zeros((spaces_on_board,),dtype=float)
#space_counts = {i:0 for i in range(spaces_on_board)}
space_counts = [0 for i in range(spaces_on_board)]

doubles = 0 # number of conseutive doubles rolled

cc_card = 0 # current top card in community chest stack
# 0 - advance to go
# 1 - go to jail

# game play -------------------------------------------------------------------

for i in range(number_of_rolls):
    
    # store current position -----------
    space_counts[current_position] += 1
    
    # dice roll (To do)
    die1 = np.random.randint(1,dice_sides+1)
    die2 = np.random.randint(1,dice_sides+1)
    
    # doubles jail
    if die1 == die2:
        doubles += 1
    else:
        doubles = 0
        
    if doubles == 3:
        current_position = 10
        doubles = 0
        continue
    
    # move to new position
    current_position += die1+die2
    #current_position = current_position + die1 + die2 
    current_position = current_position % spaces_on_board
    #print(die1,die2,current_position)

    # chance

    # community chest
    if current_position in [2,17,33]:
        if cc_card == 0:
            current_position = 0 # adance to go
        elif cc_card == 1:
            current_position = 10 # go to jail
        cc_card = (cc_card + 1)%16
    
    



# analysis --------------------------------------------------------------------

# print(space_counts)
percentages = [space_counts[i]/number_of_rolls*100 for i in range(spaces_on_board)]
percentages = [np.around(p,3) for p in percentages]
print(percentages)

# sort by percentages
percentages_negative = [-p for p in percentages]
indices = np.argsort(percentages_negative)
print(indices)




