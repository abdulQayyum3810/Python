
class Employee:
    raise_amount=1.04
    num_of_emps=0
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        Employee.num_of_emps+=1
    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
emp1=Employee("Test","User",80000)
#both are same
print(emp1.fullname())
print(Employee.fullname(emp1))

print(emp1.pay)
#it will only raise pay of emp1 not others
emp1.apply_raise()
print(emp1.pay)

#get class or instance attributes and methods
print(Employee.__dict__)
print(emp1.__dict__)

# it will change only class attribute
Employee.raise_amount=1.05
#it will create attribute raise amount of emp1
emp1.raise_amount=1.06

print(Employee.num_of_emps)