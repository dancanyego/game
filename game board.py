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
        marker = input("Player1 choose X or O : => ")
        
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return(player1,player2)
player1_marker,player2_marker = player_input()
player_input()
    
def place_marker(board, marker, position):
    
    pass
   
    
