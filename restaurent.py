from menu import Menu

class Restaurent:
    def __init__(self,name):
        self.name=name
        self.empoyees=[]
        self.menu=Menu()

    def add_employee(self,employee):
        self.empoyees.append(employee)

    def view_employee(self):
        print('----Employee List----')
        for emp in self.empoyees:
            print(emp.name,emp.phone,emp.email,emp.address)