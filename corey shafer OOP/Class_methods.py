#Regular methods (pass instance automaically), 
# class methods (pass class automatically) 
#class methods are alternative constructors
#and static Methods simple function they dont pass anything automatically but they have logical connection with class

import datetime
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
    #if instance dont have attribut raise_amount then it will take the value from class attribute
        self.pay=int(self.pay*self.raise_amount)
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def from_str(cls,emp_str):
        fname,lname,pay=emp_str.split('-')
        return cls(fname,lname,pay)
    @staticmethod
    def is_weekday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


emp1=Employee("Test","User",80000)
emp2=Employee("Test","User2",40000)

emp1.raise_amount=1.05
emp1.set_raise_amount(1.09) #it will change class variabel not emp1 
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

#creat instance using string
new_emp1_str="Jhon-Doe-70000"
new_emp2_str="Steve-Smith-90000"
new_emp3_str="Jane-Doe-50000"

#to creat employe from above strings we would do following
""" fname,lname,pay=new_emp1_str.split('-')
new_emp1=Employee(fname,lname,pay)
fname,lname,pay=new_emp2_str.split('-')
new_emp2=Employee(fname,lname,pay)
fname,lname,pay=new_emp3_str.split('-')
new_emp3=Employee(fname,lname,pay) """


#Alternative method is to construct new contructor called from_str
new_emp1=Employee.from_str(new_emp1_str)
new_emp2=Employee.from_str(new_emp2_str)
new_emp3=Employee.from_str(new_emp3_str)
print(new_emp2.fullname())


#static method example

my_date=datetime.date(2020,5,12)
print(Employee.is_weekday(my_date))