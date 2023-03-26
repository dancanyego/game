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




# New  Class 

class Circle():
    # Class Object attribute
    
    pi = 3.142
    
    def __init__(self,radius =1):
        self.radius = radius
        
    #Method
    
    def get_circumference(self):
        return self.radius * self.pi*2
    
    # Instance of the circle
my_cirle = Circle()

my_cirle.get_circumference()