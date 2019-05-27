# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:07:07 2016

@author: apanda88
"""

for i in range(1,11):
    print(i,end="\t")
print()
print("--------------------------------------------------------------------------#\n")

for row in range(1,11):
    for col in range(1,11):
        product=row*col
        print(product,end="\t")
    print("\n")

