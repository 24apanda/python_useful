
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
        emp_str.split('-')
        return cls(first,last,int(pay))
    @staticmethod ##doesn't take instance or class as first argument
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
        
class developer(Employee):
    def __init__(self,first,last,pay,prog):
        super().__init__(first,last,pay)
        self.prog=prog
    '''@classmethod
    def dev_str(cls,d_str):
        d_str.split('-')
        return cls(first,last,int(pay),prog)'''
class manager(Employee) :
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rm_emp(self,emp):
        if emp  in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('--#>',emp.fullName())
            
            
            
            
dev='Ashu-Panda-5000-Python'
dev1=developer('Ashu','Panda',5000,'Python')
dev2=developer('Mama','Panda',1000,'ASP')
mgr_1=manager('Jimmy','Panda',11000,[dev1])
print(dev1.email)
print(dev1.pay_hike())
print(dev1.prog)
print(mgr_1.fullName())
print(mgr_1.print_emps())
mgr_1.add_emp(dev2)
print(mgr_1.print_emps())
mgr_1.rm_emp(dev2)
print(mgr_1.print_emps())

print(isinstance(mgr_1,manager))
print(issubclass(manager,Employee))
print(issubclass(manager,developer))
