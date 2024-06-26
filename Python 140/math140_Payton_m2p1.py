'''
-------------------------------------------------------
Math 140 - module 2 project 1
-------------------------------------------------------
author:   Payton Sanford <pcsanford@aggies.ncat.edu>        
          Juillard Bumidang  <jgbumidangEmail@aggies.ncat.edu>  
          Jonathan Royal <jkroyal@aggies.ncat.edu>                           
-------------------------------------------------------
Description:

-- programming monopoly - Project Euler 84
https://projecteuler.net/problem=84

"Chance"
0.Advance to GO
1.Go to JAIL
2.Go to C1
3.Go to E3
4.Go to H2
5.Go to R1
6.Go to next R (railway company)
7.Go to next R
8.Go to next U (utility company)
9.Go back 3 squares.


'''
# import statements -----------------------------------------------------------

import numpy as np

# variables -------------------------------------------------------------------

current_position = 0 # start on Go square
spaces_on_board = 40
number_of_rolls = 5*10**6
dice_sides = 6
#space_counts = np.zeros((spaces_on_board,),dtype=float)
#space_counts = {i:0 for i in range(spaces_on_board)}
space_counts = [0 for i in range(spaces_on_board)]

doubles = 0 # number of conseutive doubles rolled

cc_card = 0 # current top card in community chest stack
# 0 - advance to go
# 1 - go to jail
ch_card = 0

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
   
    if current_position == 30:
        current_position = 10
        continue

    # add code here for the chance squares
    if current_position in [7]:
        if ch_card == 0:
            current_position = 0 # adance to go
        elif ch_card == 1:
            current_position = 10 # go to jail
        elif ch_card == 2:
            current_position = 11 # Go to C1
        elif ch_card == 3:
            current_position = 24 # Go to E3
        elif ch_card == 4:
            current_position = 39 # Go to H2
        elif ch_card == 5: 
            current_position = 5 # Go to R1
        elif ch_card == 6:
            current_position = 15 # Go to next R (railway company)
        elif ch_card == 7:
            current_position = 15 # Go to next R
        elif ch_card == 8:
            current_position = 12 # Go to next U (utility company)
        elif ch_card == 9:
            current_position -= 3 # Go back 3 squares.
        ch_card = (ch_card + 1)%16

    if current_position in [22]:
        if ch_card == 0:
            current_position = 0 # adance to go
        elif ch_card == 1:
            current_position = 10 # go to jail
        elif ch_card == 2:
            current_position = 11
        elif ch_card == 3:
            current_position = 24
        elif ch_card == 4:
            current_position = 39
        elif ch_card == 5: 
            current_position = 5
        elif ch_card == 6:
            current_position = 25
        elif ch_card == 7:
            current_position = 25
        elif ch_card == 8:
            current_position = 28
        elif ch_card == 9:
            current_position -= 3
        ch_card = (ch_card + 1)%16
        
    if current_position in [36]:
        if ch_card == 0:
            current_position = 0 # adance to go
        elif ch_card == 1:
            current_position = 10 # go to jail
        elif ch_card == 2:
            current_position = 11
        elif ch_card == 3:
            current_position = 24
        elif ch_card == 4:
            current_position = 39
        elif ch_card == 5: 
            current_position = 5
        elif ch_card == 6:
            current_position = 5
        elif ch_card == 7:
            current_position = 5
        elif ch_card == 8:
            current_position = 12
        elif ch_card == 9:
            current_position -= 3
        ch_card = (ch_card + 1)%16
        




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




