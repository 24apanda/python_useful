# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:49:49 2016

@author: apanda88
"""
"""
ids = ["9pti", "2plv", "1crn"]
ids.append("1alm")  #append an element
print(ids)


del ids[0]  #delete an element
print(ids)

ids.sort()
print(ids)

ids.reverse()
print(ids)

ids.insert(1, "10pti") #insert element at specific position , slower than append
print(ids)"""

"""zipping lists together---->"""
"""
names = ['ben', 'chen', 'yaqin']


gender = [0, 0, 1]

sex = ['m', 'f', 't']

values = list(zip(names, gender,sex))

print(values)"""

""" Difference between append and extend--->

if we want to append several objects contained in a list, the result as expected (or not...) is: """

stack = ['a', 'b', 'c']
print(stack.insert(2,'z'))

print(stack.append('d'))


stack.append(['d', 'e','f'])
print(stack)


gender = [0, 0, 1,1,1,1,1,1,1,1]

sex = ['m', 'f', 't',1,1,1,1,1,1,1]

values1=list(zip(stack,gender,sex))

print(values1)

print(values1.index((['d', 'e', 'f'], 1, 1)))








