# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 21:10:29 2017

@author: apanda88
"""
#########sub class and inheritance############3
class Employee:
    raise_amount=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+'@gmail.com'
        #Employee.emp_no+=1
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    def pay_hike(self):
        self.pay=int(self.pay * self.raise_amount)
         
class developer(Employee): ####inherit from employee
     raise_amount=1.1
     def __init__(self,first,last,pay,skill):
         #Employee.__init__(first,last,pay)
         super().__init__(first,last,pay)
         
         self.skill=skill
class manager(Employee):
    
        def __init__(self,first,last,pay,employees=None) :
            super().__init__(first,last,pay)
            if employees is None:
                self.employees=[]
            else:
                self.employees=employees
        def add_emp(self,emp):
            if emp not in self.employees:
                self.employees.append(emp)
        
        def rem_emp(self,emp):
            if emp  in self.employees:
                self.employees.remove(emp)
        def print_emps(self):
            for i in self.employees:
                 print('-->',i.fullname())
            

    

    
dev1=developer('Ashu','Panda',10000,'python')
dev2=developer('Jimmy','Pan',20000,'dataANA')

mgr1=manager('jim','pandda',40000,[dev1])
mgr1.add_emp(dev2)

print(mgr1.email)
mgr1.print_emps()

print(isinstance(mgr1,developer))
print(isinstance(mgr1,Employee))