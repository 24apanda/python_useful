# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 23:02:05 2017

@author: apanda88
"""

class Employee:
    raise_amount=1.04
    #emp_no=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'
        #Employee.emp_no+=1
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    def pay_hike(self):
        self.pay=int(self.pay * self.raise_amount)
    
    def __repr__(self):
        return "employee( '{}')" .format(self.email)
    def __str__(self):
        return Employee.fullname(self)       
    def __add__(self,other):
        return self.pay+other.pay
        
      

emp1=Employee('Ashu','Panda',10000)
emp2=Employee('Jimmy','Pan',20000)

print(emp1.__repr__())
print(repr(emp1))
print(emp2.__str__())
print(repr(emp2))

print(emp1+emp2)