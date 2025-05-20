
#A - klases un atribūtu izveide
class Product():
    def __init__(self, name, price, quanity):
        self.name = name
        self.price = price
        self.quanity = quanity

    #B - metodes izveide
    def get_total_price(self):
        total_price = self.price * self.quanity
        return total_price


#2. uzdevums - iepirkumu grozs
class ShoppingCart():

    #E - metožu izveide
    def add_product_to_cart(self, product):
        print('Product: ', product.name, 'has been added to cart')

    def remove_product_from_cart(self, product):
        print('Product: ', product.name, 'has been removed from cart')

    def get_total_price(self, product): 
        print('Total price: ', product.get_total_price())


#3. uzdevums
#H uzdevums
class SystemUser():

    #I - atribūtu izveide
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    #J - metožu izveide
    def set_user_info(self, newusername, newpassword, newemail): 
        self.username = newusername
        self.password = newpassword
        self.email = newemail
        print('Information is changed!')

    def get_user_info(self):

        print('Information about user:')
        print('Username: ',self.username)
        print('Passsword: ', self.password)
        print('Email: ', self.email)


#
class Customer(SystemUser):
    def __init__(self, username, password, email, customer_id, purchase_history, membership_statuss):
        super().__init__(username, password, email)
        #N - pieveino jaunus atribūtus
        self.customer_id = customer_id
        self.purchase_history = purchase_history
        self.membership_statuss = membership_statuss

    #M - metožu pārasktīšana
    def set_user_info(self, newusername, newpassword, newemail, newcustomer_id, newpurchase_history, newmembership_statuss):
        #izsaukt bāzes metodi un padot 3 jaunus atribūtus
        super().set_user_info(newusername, newpassword, newemail)
        self.customer_id = newcustomer_id
        self.purchase_history = newpurchase_history
        self.membership_statuss = newmembership_statuss

    def get_user_info(self):
        super().get_user_info()
        print('Customer ID: ', self.customer_id)
        print('Purchase history: ', self.purchase_history)
        print('Membership statuss: ', self.membership_statuss)
        

#C - objektu izveide klasei Product
pasta = Product('Spaghetti', 2.30, 4)
print('Products total price: ',pasta.get_total_price())

apple = Product('Apple', 1.20, 2)
print('Products total price: ',apple.get_total_price())


#F - objekts ShoppingCart klasei
iepirkumu_grozs = ShoppingCart()
#G - izsaukt metodes
print('---'*8)
iepirkumu_grozs.add_product_to_cart(pasta)
iepirkumu_grozs.get_total_price(pasta)
iepirkumu_grozs.remove_product_from_cart(pasta)


#K
bob = SystemUser('employeeBob', 'puppies', 'bobTheMan@email.com')
#noaminīt info un parādīt
bob.set_user_info('manegerBob', 'rainbows', 'superBob@email.com')
print('---'*8)
bob.get_user_info() #parāda nomainītos datus


#O - klienta objekts ara atjauninātu informāciju
anne = Customer('Anne12', 'lake', 'anneWithAnE@email.com', 38, '', '')#nav statuss un vēstures
#atjaunina info
anne.set_user_info('Anne85', 'ocean', 'superAnne@email.com', 38, 'French fries', 'Gold')
print('---'*8)
anne.get_user_info()






