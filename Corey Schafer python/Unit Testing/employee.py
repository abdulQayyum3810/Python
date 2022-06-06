import requests

class Employee:
    raise_amt = 1.05

    def __init__(self, fname, lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    @property  # getter
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    @property  # getter
    def email(self):
        if self.fname == None:
            return "email does not exist"
        else:
            return "{}.{}@email.com".format(self.fname, self.lname)
        
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
        
    def monthly_schedule(self, month):
        response=requests.get(f"http://company.com/{self.lname}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
