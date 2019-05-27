# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:47:32 2017

@author: apanda88
"""
"""
def greet(name):
   """"""this person greet the person"""
   # print("hello,",name,"good morning")

    
#greet('Ashutosh')"""

#print(greet.__doc__)##doc string

"""
def my_func():
 x = 10
 x+=20
 print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)"""

####Find gcd###
"""
def gcd(x,y):
    if x < y :
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            hcf=i
    return hcf
    #print("gcd for ",x,"and",y,":",hcf)
    
print(gcd(3,12))"""
#######Find Lcm####
"""
def lcm(x,y):
    if x < y :
        greater=y
    else:
        greater=x
    for i in range(1,greater+1):
        if (greater%x==0) and (greater%y==0):
            lc=i
    return lc
    #print("gcd for ",x,"and",y,":",hcf)
    
print(lcm(4,48))"""










