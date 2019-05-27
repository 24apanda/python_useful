# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:25:42 2017

@author: apanda88
"""
#######class method  and static method ###########
class Employee:
    raise_amount=1.1
    emp_no=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+'@gmail.com'
        Employee.emp_no+=1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def pay_hike(self):
        self.pay=self.pay * self.raise_amount
        return self.pay
        
    @classmethod ############decorator 
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def new_str(cls,emp_str):
        first,last,pay=emp_str1.split('-')
        return cls(first,last,pay)
        
    @staticmethod
    def work_day(day): ####static method doesn't take instance or class as first argumnet
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
        
import datetime
my_date=datetime.date(2016,1,15)

print( Employee.work_day(my_date))
    
        
   

emp1=Employee('Ashu','Panda',10000)
emp2=Employee('Jimmy','Pan',20000)

emp_str1='mama-panda-20000'

"""first,last,pay=emp_str1.split('-')
new_emp1=Employee(first,last,pay)
print(new_emp1.fullname())"""

new_emp1=Employee.new_str(emp_str1) ###calling class method
print(new_emp1.pay)

Employee.set_raise_amt(1.2)

print(Employee.pay_hike(emp1))
print(Employee.set_raise_amt)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp1.set_raise_amt(1.3)


print(Employee.set_raise_amt)
print(emp1.raise_amount)
print(emp2.raise_amount)