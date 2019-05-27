# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:46:54 2016

@author: apanda88
"""

##########Find factor
"""max=12
n=1
while n < max:
    factor=1
    print(n,end="\t")
    while factor <= n:
        if n%factor == 0:
            print(factor,end="\t")
            factor=factor+1
    print("\n")
    n+=1"""
    
n=1
max=eval(input("provide value :" ))
fact=max%n
for n in range(1,max+1):
    print(n,"\t",":",end="")
    for fact in range(1,n+1):
         if n%fact==0:
             print(fact,end="\t")
    print("\n")

 

     

