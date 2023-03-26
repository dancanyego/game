# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:37:39 2023

@author: danca
"""

class Animal():
    
    def __init__(self):
        print("Animal Created")
        
    
    def who_am_i(self):
        print("I am a fucking animal")
        
    def eat(self):
        print("I am eating")
        
        
myanimal = Animal()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created!!")
        
mydog = Dog()

mydog.eat()