# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:38:38 2023

@author: danca
"""

class Dog():
    ## Class object attribute and these are the same for any instance of a class
    
    species = 'mammal'
    
    def __init__(self,breed,name):
        
        
        self.breed = breed
        self.name = name
        
        
    # Operations/ Actions ------->> Methods
    
    def bark(self):
        print("wooof my name is {}".format(self.name))
        print("Woof")
        
        
my_dog = Dog(breed = 'chiuhaha',name = 'sammy')
my_dog.bark()
my_dog.breed

