# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 00:20:36 2023

@author: danca
"""

class Account():
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

        
    def __str__(self):
        print(f"Account owner :> {self.name}")
        print(f"Account balance :> {self.balance}")
        
  

    def deposit(self,dep_amt):
        self.balance += dep_amt
        print("Deposit Success!")
        
    def withdrawal(self,rem_amt):
        if self.balance >= rem_amt:
            self.balance -= rem_amt
            
        else:
            print("Insufficient Funds!!")
            
            
acct1 = Account('Jose',100)
        
