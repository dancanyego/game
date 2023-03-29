# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 00:20:36 2023

@author: danca
"""

class Account():
    
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance
        
  

    def deposit(self,dep_amt):
        self.balance += dep_amt
        available = self.balance + dep_amt
        print("Deposit Success!")
        print(f"your available balance is {available}")
        
    def withdraw(self,rem_amt):
        if self.balance >= rem_amt:
            self.balance -= rem_amt
            available = self.balance - rem_amt
            print("Withdrawal succesfull")
            print(f"your available balance is {available}")
            
        else:
            print("Insufficient Funds!!")
            
            
    def __str__(self):
        return f'Account owner:   {self.name}\nAccount balance: ${self.balance}'
            
            
acct1 = Account('Jose',100)
print(acct1)
acct1.name
acct1.deposit(150)
print(acct1)
acct1.withdraw(75)
print(acct1)
acct1.withdraw(20)
print(acct1)
        
