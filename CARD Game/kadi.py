# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 00:06:55 2023

@author: danca
"""

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank - rank
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
    