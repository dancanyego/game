# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 21:41:36 2023

@author: danca
"""

game_list = ['0','1','2']

def display_game(game_list):
    print("Here is the current List")
    print(game_list)
    
display_game(game_list)

def position_choice():
    
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        
        choice = input("Pick a position from the standard input from 0 to 2 ::")
        
        if choice not in ['0','1','2'] :
            print("Sorry Invalid choice!!")
            
    return int(choice)

position_choice()
    
def replacement_choice(game_list,position):
    
    user_placement = input("Type a string to replace at the position: ")
    
    game_list[position] = user_placement
    
    return game_list

replacement_choice(game_list, 1)


def gameon_choice():
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        
        choice = input("Continue Playing (Y or N)::")
        
        if choice not in ['Y','N'] :
            print("Sorry Invalid choice!!")
            
    if choice == 'Y':
        return True
    else:
        print("game Over Nigga")
        return False

gameon_choice()


game_on = True
game_list = [0,1,2]

while game_on:
    
    display_game(game_list)
    position = position_choice()
    
    game_list = replacement_choice(game_list, position)
    
    display_game(game_list)
    
    game_on = gameon_choice()
