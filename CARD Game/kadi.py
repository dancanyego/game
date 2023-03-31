# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 00:06:55 2023

@author: danca
"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    

#Deck class 

class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #Creating the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
                
new_deck = Deck()
new_deck.shuffle()
mycard = new_deck.deal_one()
print(mycard)
print(len(new_deck.all_cards))
bottom_card =new_deck.all_cards[-1]

#for card_object in new_deck.all_cards: 
#  print(card_object)

#Player Class

class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
new_player = Player('Jomba')
print(new_player)
new_player.add_cards(mycard)
print(new_player)
        


    