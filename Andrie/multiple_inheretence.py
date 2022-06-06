class user(object):
    def singIn(self): #if we don't have any attiribute assigned at object creation then don't use __init__ method
        print("logged in")


class Wizards(user):
    fun="wizard fun"
    def __init__(self,name,power) -> None:
        self.name=name
        self.power=power
    def attack(self):
        print(f"{self.name} is attacking with the power of {self.power}")


class Archers(user):
    fun="archer fun"
    def __init__(self,name,numOfArrows) -> None:
        self.name=name
        self.numOfArrows=numOfArrows
    def attack(self):
        print(f"{self.name} is attacking with the arrows of {self.numOfArrows}")
    def checkArrows(self):
        print(f"Arrows remaining {self.numOfArrows}")
    def run(self):
        print("ran really fast")
class HybridBorg(Wizards,Archers): #class variables/method of wizard will be preffered
    def __init__(self, name, power,numOfArrows) -> None:
        #wizard will write name attribute again
       Archers.__init__(self,name,numOfArrows)
       Wizards.__init__(self,name,power)

hybridBorg1=HybridBorg("hybridBorg1",30,60)
hybridBorg1.attack() #Archer attack method will be preffered
print(hybridBorg1.fun)
Wizards.fun="hah" #it will change wizards class variable
hybridBorg1.fun="jjjj" # it will create attribute for instance hybridBorg1
print(hybridBorg1.fun)
print(HybridBorg.fun)
print(Wizards.fun)


#MRO

print(HybridBorg.mro())

