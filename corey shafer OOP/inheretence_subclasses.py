

class Employee:
    raise_amount=1.04
    num_of_emps=0
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email="{}.{}@gmail.com".format(fname,lname)
        Employee.num_of_emps+=1
    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)


class Developer(Employee):
    def __init__(self,fname,lname,pay,prog_lang):
        super().__init__(fname,lname,pay) #parent classs is handelling first three arguments
       # Employee.__init__(self,fname,lname,pay)    #also valid
        self.prog_lang=prog_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay,employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--->",emp.fullname())



emp1=Employee("Test","User",80000)
emp2=Employee("Test","User2",40000)

#Developer class is getting four arguments but three are handled by employee class
dev1=Developer("Develper","User1",30000,"Python")
dev2=Developer("Develper","User2",50000,"Java")

print(dev1.prog_lang)
#get resolution order and other information about class Developer
"""print(help(Developer)) """

mgr_1=Manager("Sue","Smith",10000,[dev1])
print(mgr_1.email)

mgr_1.print_emps()
mgr_1.add_emp(dev2)
mgr_1.print_emps()
mgr_1.remove_emp(dev1)
mgr_1.print_emps()

#check instance of class or not
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer))

#check subclass of other class or not
print(issubclass(Developer,Employee))
print(issubclass(Developer,Manager))