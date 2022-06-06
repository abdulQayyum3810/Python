class playerChararcter:
    def __init__(self,name,age) -> None:
        self._name=name #_ tells user that its private and dont try to modify it
        self.age=age 
    def run(self):
        print("run")
    def speak(self):
        print(f"my name is {self.name} and I am {self.age} years old")
player1=playerChararcter("babar",50)
print(player1)
player1.name="Amir"
player1.speak="Boom" #Now method is converted to attribute (method is overwritten)
"""player1.speak()"""# Now it is not callable as method tp get 
print(player1._name) # Now it will not through an error