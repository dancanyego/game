# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 22:57:35 2023

@author: danca
"""

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9] )
    print(board[4]+'|'+board[5]+'|'+board[6] )
    print(board[1]+'|'+board[2]+'|'+board[3] )
    
test_board = [' ']*10
display_board(test_board)

# Welcome the player and ask them to chooce a position

def player_input():
    marker = ''
    # Asking the player to choose X OR O
    while marker != 'X' and marker != 'O':
        marker = input("Player1 choose X or O : => ").upper()
        
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return(player1,player2)

# Using tupple unpacking in order to assign the input 
player1_marker,player2_marker = player_input()  
player_input()
    
def place_marker(board, marker, position):
    
    board[position] = marker
    
    
    # Check The winner of the game Through checking the winning combinations
    
def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
win_check(test_board,'X')



import random

# To randomly choose the player to begin 

def choose_first():
    
    flip = random.randint(0, 1)
    
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'
    
    
def space_check(board ,position):
    
    return board[position] == ''

# Checking if the board is full and returning a value

def full_board_check(board):
    pass

