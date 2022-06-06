

class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    @property #getter
    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    @property #getter
    def email(self):
        if self.fname==None:
            return "email does not exist"
        else:
            return "{}.{}@gmail.com".format(self.fname,self.lname)
    @fullname.setter
    def fullname(self,name):
        fname,lname=name.split(' ')
        self.fname=fname
        self.lname=lname

    @fullname.deleter
    def fullname(self):
        print("Name deleted")
        self.fname=None
        self.lname=None
emp1=Employee("Test","User")
emp2=Employee("Test","User2")



print(emp1.email)
emp1.fullname="corey shafer"
print(emp1.email)
print(emp1.fname)

del emp1.fullname
print(emp1.fname)
print(emp1.email)