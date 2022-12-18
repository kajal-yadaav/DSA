class Employee:
    __raise_amount=1.03
    def __init__(self,first,last,sal):
        self.fname=first
        self.lname=last
        self.pay=sal
    @classmethod
    def set_raise_amt(cls,amount):
        cls.__raise_amount=amount

    @staticmethod
    def is_workday(day):
        return not(day.weekday()==5 or day.weekday()==6)
    def getsal(self):
        return self.pay*Employee.__raise_amount
emp1=Employee("manoj","kumar",50000)
emp2=Employee("dheeraj","mishra",60000)#init method runs automatically

Employee.set_raise_amt(1.05)
print(emp1.getsal())
print(emp2.getsal())

#There are 3 modules to handle date and time.

import datetime
my_date=datetime.date(2016,12,4)
print(my_date.today())
print(Employee.is_workday(my_date))
