
class Employee:
    raise_amount=1.1
    emp_no=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+'@gmail.com'
    def fullName(self):
        return '{} {}'.format(self.first,self.last)
    def pay_hike(self):
        self.pay=self.pay*self.raise_amount
        return int(self.pay)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def employee_str(cls,emp_str):
        emp_str1.split('-')
        return cls(first,last,int(pay))
    @staticmethod ##doesn't take instance or class as first argument
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
emp1=Employee('Ashu','Panda',1000)
emp2=Employee('Mama','Panda',500)

print(emp1.email)
print(emp2.first)
print(emp1.fullName())
print("emp1.pay_hike()",emp1.pay_hike())
print(emp1.raise_amount)
print(Employee.raise_amount)
print(emp1.__dict__)#It will convert instance to dictionaty format

##Decorator class metod call
Employee.set_raise_amt(1.2)
print(Employee.raise_amount)
print("emp1.pay_hike()",emp1.pay_hike())
emp2.set_raise_amt(1.12)
print(emp2.pay_hike())

emp_str1='John-Daa-2000'

newemp1_str=Employee.employee_str(emp_str1)
print(newemp1_str.first)
print(newemp1_str.email)
print(newemp1_str.fullName())
print(newemp1_str.pay_hike())

####static Method ####
import datetime
my_date=datetime.date(2017,12,30)
print(Employee.is_workday(my_date))

