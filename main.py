from food_items import FoodItem
from order import Order
from menu import Menu
from restaurent import Restaurent
from users import Customer,Admin,Employee

mamar_restaurent = Restaurent('Mamar Restaurent')
def customer_menu():
    name = input('Enter Your Name: ')
    phone = input('Enter Your Phone: ')
    email = input('Enter Your Email: ')
    address = input('Enter Your Address: ')
    customer = Customer(name=name,phone=phone,email=email,address=address)

    while True:
        print(f'Welcome {customer.name}!!')
        print('1. View Menu')
        print('2. Add item to cart')
        print('3. View Cart')
        print('4. Pay Bill')
        print('5. Exit')

        choice = int(input('\nEnter Your Choice: '))

        if choice==1:
            customer.view_menu(mamar_restaurent)

        elif choice==2:
            item = input('Enter item name: ')
            item_quantity = int(input('Enter item Quantity: '))
            customer.add_to_cart(mamar_restaurent,item,item_quantity)

        elif choice==3:
            customer.view_cart()

        elif choice==4:
            customer.pay_bill()

        elif choice==5:
            break
        
        else:
            print('Invalid choice, Try Again!')


def admin_menu():
    name = input('Enter Your Name: ')
    phone = input('Enter Your Phone: ')
    email = input('Enter Your Email: ')
    address = input('Enter Your Address: ')
    admin = Admin(name=name,phone=phone,email=email,address=address)

    while True:
        print(f'Welcome {admin.name}!!')
        print('1. Add New Item')
        print('2. Add New Employee')
        print('3. View Employees')
        print('4. View Items')
        print('5. Delete Item')
        print('6. Exit')

        choice = int(input('\nEnter Your Choice: '))

        if choice==1:
            item_name = input('Enter item name: ')
            item_price = int(input('Enter item price: '))
            item_quantity = int(input('Enter item quantity: '))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_restaurent,item)


        elif choice==2:
            name = input('Enter employee name: ')
            phone = input('Enter employee phone: ')
            email = input('Enter employee email: ')
            address = input('Enter employee address: ')
            age = input('Enter employee age: ')
            designation = input('Enter employee designation: ')
            salary = input('Enter employee salary: ')
            employee = Employee(name=name,phone=phone,email=email,address=address,age=age,designation=designation,salary=salary)
            admin.add_employee(mamar_restaurent,employee)

        elif choice==3:
            admin.view_employee(mamar_restaurent)

        elif choice==4:
            admin.view_menu(mamar_restaurent)

        elif choice==5:
            item = input('Enter item name: ')
            admin.remove_item(mamar_restaurent,item)

        elif choice==6:
            break
        
        else:
            print('Invalid choice, Try Again!')

while True:
    print('Welcome!!')
    print('1. Customer')
    print('2. Admin')
    print('3. Exit')
    choice = int(input('\nEnter Your Choice: '))

    if choice==1:
        customer_menu()
    elif choice==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print('Invalid Choice, Try Again!')





