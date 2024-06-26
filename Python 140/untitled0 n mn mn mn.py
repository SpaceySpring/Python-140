# -*- coding: utf-8 -*-
"""
Created on Tue May 10 19:57:09 2022

@author: bestb

Attribute Information:
   1. White King file (column)
   2. White King rank (row)
   3. White Rook file
   4. White Rook rank
   5. Black King file
   6. Black King rank
   7. optimal depth-of-win for White in 0 to 16 moves, otherwise drawn
	{draw, zero, one, two, ..., sixteen}.

"""
# imports) ----------------------------------------------------

import numpy as np
import pandas as pd

# part 1a) ----------------------------------------------------

df1 = pd.read_csv('krkopt.data',header=None)
arr_chess = df1.values 

# part 2a) ----------------------------------------------------

white_king_for_a_mask = arr_chess[:,0] == 'a'
white_king_a = arr_chess[white_king_for_a_mask,:]
white_king_a_count = np.count_nonzero(white_king_a[:,0])

# part 2b) ----------------------------------------------------

black_king_for_four_mask = arr_chess[:,5] == 4
black_king_four = arr_chess[black_king_for_four_mask,:]
black_king_four_count = np.count_nonzero(black_king_four[:,0])

# part 2c) ----------------------------------------------------

draw_mask = arr_chess[:,6] == 'draw'
draw = arr_chess[draw_mask,:]
draw_count = np.count_nonzero(draw[:,0])

# part 2d) ----------------------------------------------------

optimal_mask = arr_chess[:,6] == 'twelve'
optimal = arr_chess[optimal_mask,:]
optimal_count = np.count_nonzero(optimal[:,0])

# part 3a) ----------------------------------------------------

root_mask_for_5 = draw[:,3] == 5
root_5 = draw[root_mask_for_5,:]
root_count_5 = np.count_nonzero(root_5[:,0])

# part 3b) ----------------------------------------------------

root_mask_for_7 = draw[:,3] == 7
root_7 = draw[root_mask_for_7,:]
root_count_7 = np.count_nonzero(root_7[:,0])

# part 3c) ----------------------------------------------------

optimal_mask_1 = arr_chess[:,6] == 'one'
optimal_1 = arr_chess[optimal_mask_1,:]
white_root_for_5 = optimal_1[:,3] == 5
white_root_5 = optimal_1[white_root_for_5,:]
white_root_5_count = np.count_nonzero(white_root_5[:,0])

# part 4a) ----------------------------------------------------

average_white_king_rank = np.mean(optimal_1[:,1])

# part 4b) ----------------------------------------------------

vars_white_king_rank = np.var(optimal_1[:,1])

# part 4c) ----------------------------------------------------

average_black_king_rank = np.mean(optimal_1[:,5])

# part 5) ----------------------------------------------------

sorted_whites = np.argsort(arr_chess[:,0])
arr_bank_sorted_whites = arr_chess[sorted_whites,:]

sorted_roots = np.argsort(arr_chess[:,2])
arr_bank_sorted_roots = arr_chess[sorted_roots,:]

sorted_black = np.argsort(arr_chess[:,4])
arr_bank_sorted_black = arr_chess[sorted_black,:]
