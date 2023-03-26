# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 22:57:35 2023

@author: danca
"""

from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
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
    
    for i in range(1,10):
        if space_check(board, i):
            return False 
        
        # Board is full We return True 
        return True
    
# Checking players Next Position and return True

def players_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Enter your New Position from (1 - 9) <<>> "))
        
        
    return position

# Check if a player wants to replay

def replay():
    
    choice = input("Wanna Play again 'Y' or 'N' :> ")
    
    return choice == 'Y'

# Bringing together the logic

#While loop to keep running the game 

#Break the loop with replay

print("Welcome to Tic TAC Toe")

while True:
    # play the game 
    ## Setting the board (Whos first and choose markers )
    
    the_board = [' '] * 10
    
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' Will Go First !!')
    
    play_game = "Ready to play game! <Y> or <N> :".capitalize()
    
    if play_game == 'Y' :
        game_on = True
    else:
        game_on = False
        
        
    # Game Play
    
    while game_on:
        if turn == 'Player 1':
            
            ## Player 1 Turn
            
            # Show the Board
            display_board(the_board)
            
            #Choose a position 
            position = players_choice(the_board)
            
            #Place a marker at the position
            
            place_marker(the_board, player1_marker,position)
            
            #check if they won
            
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 Has finally won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a tie!!")
                    game_on = False
                else:
                    turn = "Player 2"
            #Check if They tied
            #No Tie or win, Next players Turn 
        else:
            ##   player 2 turn 
            # Show the Board
            display_board(the_board)
            
            #Choose a position 
            position = players_choice(the_board)
            
            #Place a marker at the position
            
            place_marker(the_board, player1_marker,position)
            
            #check if they won
            
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 1 Has finally won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a tie!!")
                    game_on = False
                else:
                    turn = "Player 2"
            
        
           
            
    
    
    
    
    #Game Play(Player1 turn and player2 Turn)
    
    
    if not replay():
        break

    
        
    
