
from abc import ABC, abstractmethod

#A - klases un atribūtu izveide
class Product():
    def __init__(self, name, price, quanity):
        self.name = name
        self.price = price
        self.quanity = quanity

    #B - metodes izveide
    def get_total_price(self):
        total_price = self.price * self.quanity
        print(f"Total price for {self.name} is: {total_price} EUR")

#C - objektu izveide
pasta = Product('Spaghetti', 2.30, 4)
pasta.get_total_price()

apple = Product('Apple', 1.20, 2)
apple.get_total_price()

#D - klases izveide
class ShoppingCart():
    def __init__(self, name, price, quanity):
        self.name = name
        self.price = price
        self.quanity = quanity
        self.cart = []

    #E - metožu izveide
    def add_product_to_cart(self):
        self.cart = (self.name).append()
        print(f"{self.name} has been added to cart!")
        print('Your cart now is: ', self.cart)

    def remove_product_from_cart(self):
        self.cart = (self.cart).remove(self.name)
        print(f"{self.name} has been removed from cart!")
        print('Your cart now is: ', self.cart)

    def get_total_price(self): #!!!!!!!! cikls lai iet cauri visiem cartā
        total_price = self.price * self.quanity
        print(f"Total price for {self.name} is: {total_price} EUR")

#F - objekta izveide
fries = ShoppingCart('Frozen french fries', 2.90, 2)
fries.add_product_to_cart()

apple = ShoppingCart('Apple', 1.20, 2)
apple.add_product_to_cart()

pasta = ShoppingCart('Spaghetti', 2.30, 4)
pasta.add_product_to_cart()

#G - aprēķina kopējās izmaksas
#carts_sum = fries.get_total_price() + apple.get_total_price() + pasta.get_total_price()
#print('Your carts total is: ', carts_sum, 'EUR')

#H - klases izveide
class SystemUser():

    #I - atribūtu izveide
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    #J - metožu izveide
    def set_user_info(self): 
        what_to_change = input('What would you like to change (username or password or email): ')

        if what_to_change.lower() == 'username':
            self.username = input('Write your new username: ')
        elif what_to_change.lower() == 'password':
            self.password = input('Write your new password: ')
        else:
            self.email = input('Write your new email: ')

    def get_user_info(self):
        print(f"Username: {self.username}\nPassword: {self.password}\nEmail: {self.email}")

#K - objektu izveide
bob = SystemUser('manegerBob', 'puppies', 'bobTheMan@email.com')
bob.set_user_info()
bob.get_user_info()







