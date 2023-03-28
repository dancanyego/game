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
        return f"{self.title} rocks by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("The Book has been deleted")
    
    
b = Book('chemosi', 'author', 200, 'category')

print(b)
print('The book is of pages ' , len(b))
del(b)