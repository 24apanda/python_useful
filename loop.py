# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:43:49 2016

@author: apanda88
"""
######indefinite loop###########
done= False
while not done:
   entry=eval(input("any value "))
   if entry == 999 :
        done = True        
   else:
        print(entry)
        
###########for loop######
for n in range(1,12,2):
    print(n)
    
for n in range(10,2,-2):
    print("\n",n,',',end='')
    
for n in range(1,-1,-1):
    print(n,',',end='')