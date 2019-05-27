# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:26:42 2016

@author: apanda88
"""

n = eval(input("Enter a number: "))
print(n)
c=print('|', n, '| = ', (-n if n < 0 else n),sep=" ")
print("Absolute value is :",c)