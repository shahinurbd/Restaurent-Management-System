from abc import ABC
from order import Order
class Users(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Customer(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('Order items exceeded!!')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print('Item Added!!')
        else: 
            print('Item not found')

    def view_menu(self,restaurent):
        restaurent.menu.view_menu()

    def view_cart(self):
        print("**View Cart**")
        print('Name\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
            print(f'Total price: {self.cart.total_price}')

    def pay_bill(self):
        print(f"Total {self.cart.total_price} taka paid successfully")
        self.cart.clear()


class Employee(Users):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary


class Admin(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.empoyees=[]

    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)

    def view_employee(self,restaurent):
        restaurent.view_employee()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

    def view_menu(self,restaurent):
        restaurent.menu.view_menu()
