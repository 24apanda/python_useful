# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:36:23 2016

@author: apanda88
"""


"""print(" 1 2 3 4 5 6 7 8 9 10 ")
print(" * * * * * * * * * * ")
for row in range(1,11):
    if row < 10:
     print(" ",end=" ")
    print(row,"|",end=" ")
    for column in range(1,11):
        product=row*column
        if product<100:
            print(end=" ")
        if product < 10: # Need to add another space?
           print(end=" ")
           print(product, end=" ") # Display product
           print()"""
           
# Print a multiplication table to 10 x 10
 # Print column heading
print(" 1 2 3 4 5 6 7 8 9 10")
print(" +----------------------------------------")
for row in range(1, 11): 
 if row < 10: 
  print(" ", end="")
 print(row, "| ", end="") 
 for column in range(1, 11):
  product = row*column 
 if product < 100: # Need to add space?
  print(end=" ")
 if product < 10: # Need to add another space?
  print(end=" ")
 print(product, end=" ") # Display product
 print()