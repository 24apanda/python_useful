# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:18:37 2017

@author: apanda88
"""
"""
class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.email=first+'.'+'@gmail.com'
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
        
        
emp1=Employee('Ashu','Panda')
emp2=Employee('Jimmy','Pan')

print(emp1.first)

print(emp2.email,'\n',emp2.fullname()) 

print(type(emp1))


print(Employee.fullname(emp1))"""

########Class variable##########33

class Employee:
    raise_amount=1.04
    emp_no=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+'@gmail.com'
        Employee.emp_no+=1
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    def pay_hike(self):
        self.pay=int(self.pay * self.raise_amount)
        
print("employee number check:",Employee.emp_no)  ###it will return 0 ,initiated before      

emp1=Employee('Ashu','Panda',10000)
emp2=Employee('Jimmy','Pan',20000)

print(emp1.raise_amount)
print(emp1.pay)
print(emp2.raise_amount)
print(Employee.raise_amount)


print(emp1.raise_amount)

 
print(Employee.pay_hike(emp2))
print(emp1.__dict__)

Employee.raise_amount=1.6  #Name space
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

emp1.raise_amount=1.5  
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

print("final employee number:",Employee.emp_no)








        
        