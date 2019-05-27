# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 00:38:28 2016

@author: apanda88"""

for x in 'ABC':
 for y in 'ABC': 
  if y != x: 
    for z in 'ABC':
        if z != x and z != y:
         print(x,'|',y,'|',z)
         

    
        