# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:48:45 2016

@author: apanda88
"""

###########prime Number##########
max = 10
count=0
for i in range(2,max+1):
    for j in range(2,i+1):
        if (i%j==0 and i !=j):
            count=1
            break
    if(count==1):
        print( i,"Opposite mane paduni")
    else:
        print(i,"prime")
    count=0