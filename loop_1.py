# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:47:18 2016

@author: apanda88
"""

max = 3
print(end=" ")
for column in (1,max):
  print(end="%2i" %column)
print()

print(end="+")
for column in (1,max+1):
    print(end="###")
print()

for row in range(1,max+1):
    print(end="%2i" %row)
for column in range(1, max + 1): 
 product = row*column; # Compute product
 print("\n",end="%2i " % product) # Display product
print()