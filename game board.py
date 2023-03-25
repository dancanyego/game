# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 22:57:35 2023

@author: danca
"""

from IPython.display import clear_output

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9] )
    print(board[4]+'|'+board[5]+'|'+board[6] )
    print(board[1]+'|'+board[2]+'|'+board[3] )
    
test_board = [' ']*10
display_board(test_board)

# Welcome the player and ask them to chooce a position

def player_input():
    choice = 'game on'
     
    while choice not in ['O','X']:
        choice = input("Player 1 :: Enter Your Prefered Choice ::> ")
        
        if choice not in ['O','X']:
            print("Sorry Invalid Choice!! Try again ")
            
        if choice in ['O','Y']:
           return True
        else :
           return False
       
player_input()          
    
