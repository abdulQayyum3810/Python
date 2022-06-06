#sorrounded by double underscores
class Employee:
    raise_amount=1.04
    num_of_emps=0
    def __init__(self,fname,lname,pay,myDict):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.myDict=myDict
        self.email="{}.{}@gmail.com".format(fname,lname)
        Employee.num_of_emps+=1
    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
    def __repr__(self):
        return "Employee({}, {},{})".format(self.fname,self.lname,self.pay)
    def __str__(self):
        return "{}   {}".format(self.fullname(),self.email)
    def __add__(self,other):
        return self.pay+other.pay
    def __len__(self):
        return len(self.fullname())
    def __getitem__(self,index):
        return self.myDict[index]
emp1=Employee("Test","User",80000,{"country":"pakistan","city":"Bhakkar"})
emp2=Employee("Test","User2",40000,{"country":"USA","city":"New York"})

print(repr(emp1))
print(str(emp1))
#in background of above two lines
print(emp1.__repr__())
print(emp1.__str__())


print(1+1)# what we see
print(int.__add__(1,1)) #in background

print(len("test")) #what we see
print("test".__len__())#in background

print(emp1+emp2)# used dunder addition method defined in Employee
print (len(emp1))# uses dunder len method defined in Employee Class
print(emp1["country"]) #uses dunder getitem method