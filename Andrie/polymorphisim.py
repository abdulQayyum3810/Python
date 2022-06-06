# In polymorphism different classes and objects can share the same method name 
#but method will be different for every classs like attack() in the following example
class user():
    def __init__(self,email,fun) -> None:
        self.email=email
        self.fun=fun
    def singIn(self): 
        print("logged in")


class wizards(user):
    def __init__(self,name,power,fun,email) -> None:
        super().__init__(email,fun)
        self.name=name
        self.power=power
    def attack(self):
        print(f"{self.name} is attacking with the power of {self.power}")


class archers(user):
    def __init__(self,name,numOfArrows,fun,email) -> None: # take arguments in order in which child class requires, fun email
        super().__init__(email,fun) #order in which they are passed to super class should be same as super class requires, email,fun
        self.name=name
        self.numOfArrows=numOfArrows
    def attack(self):
        print(f"{self.name} is attacking with the arrows  {self.numOfArrows}")
wizard1=wizards("wizard1",20,3,"wizard1@gmail.com")
archer1=archers("archer1",70,4,"archer1@gmail.com")
print(wizard1.attack())

#polymorphism __ attack() name is same but different functionality for wizard and archer classses
print(wizard1.attack())
print(archer1.attack())

#another way of showing polymorphism
def playerAttack(char):
    char.attack()
playerAttack(wizard1)
playerAttack(archer1)


print(wizard1.fun)

#introspection
print(dir(wizard1)) # it will print all methods and attributes available to wizard object
print(str(wizard1))