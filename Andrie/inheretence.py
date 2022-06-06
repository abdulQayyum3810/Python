#users can be _Wizards _Archers _orges 
class user:
    def singIn(self): #if we don't have any attiribute assigned at object creation then don't use __init__ method
        print("logged in")


class Wizards(user):
    pass



class Archers(user):
    pass
wizard1=Wizards()
print(wizard1.singIn())




