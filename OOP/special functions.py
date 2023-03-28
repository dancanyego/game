# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:25:06 2023

@author: danca
"""

class Book():
    
    def __init__(self,title,author,pages,category):
        self.title= title
        self.author = author
        self.pages = pages
        self.category = category
        
    def __str__(self):
        return ("the {} book by { } named {} was Launched by {} himselfu").format(self.category, self.author,self.title,self.title)
    
    
b = Book('chemosi', 'author', 200, 'category')