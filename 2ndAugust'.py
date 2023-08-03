#Create a base class Staff with attributes like name, employee_id, and department. 
# Implement child classes like Faculty and Administration, which inherit from Staff. 
# Add specific methods or attributes for each type of staff member.
"""class Staff:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
class Faculty(Staff):
    def __init__(self,name,id,deparment,subject):
        super().__init__(name,id,deparment)
        self.subject=subject
    def display_details(self):
        super().display_details()
        print(self.subject)
    def conduct(self):
        print(self.subject)

class Administration(Staff):
    def __init__(self,name,id,deparment,rank):
        super().__init__(name,id,deparment)
        self.rank=rank
    def display_details(self):
        super().display_details()
        print(self.rank)
    def position(self):
        print(self.rank)
        
f=Faculty("Zumero",85,"SE","Database")
a=Administration("Pumero",98,"CS","Second")
f.display_details()
a.display_details()"""

#Implement a class ElectronicDevice with attributes like brand, model, and price.
#  Create child classes like Smartphone, Laptop, and TV, which inherit from ElectronicDevice. 
# Each child class should have additional attributes specific to the type of device.

"""class ElectronicDevice:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price:.2f}")

class Smartphone(ElectronicDevice):
    def __init__(self,brand,model,price,type):
        super().__init__(brand,model,price)
        self.type=type
    def display_details(self):
        print(self.type)
        print(self.brand)
        print(self.model)
        print(self.price)

class Laptop(ElectronicDevice):
    def __init__(self,brand,model,price,screen):
        super().__init__(brand,model,price)
        self.screen=screen
    def display_details(self):
        print(self.screen)
        print(self.brand)
        print(self.model)
        print(self.price) 

class TV(ElectronicDevice):
    def __init__(self,brand,model,price,inches):
        super().__init__(brand,model,price)
        self.inches=inches
    def display_details(self):
        print(self.inches)
        print(self.brand)
        print(self.model)
        print(self.price)
        

s=Smartphone("Iphone","8","56000","TouchScreen")
l=Laptop("Lenovo","9","58000","Hybrid")  
t=TV("Iphone","10","56000","Smart LED")
print("Smartphone Details",s.display_details()) 
print("Laptop Details",l.display_details())
print("TV Details",t.display_details()) """

"""class ElectronicDevice:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price:.2f}")


class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, price, screen_size, storage):
        super().__init__(brand, model, price)
        self.screen_size = screen_size
        self.storage = storage

    def display_details(self):
        super().display_details()
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Storage: {self.storage} GB")


class Laptop(ElectronicDevice):
    def __init__(self, brand, model, price, processor, ram):
        super().__init__(brand, model, price)
        self.processor = processor
        self.ram = ram

    def display_details(self):
        super().display_details()
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram} GB")


class TV(ElectronicDevice):
    def __init__(self, brand, model, price, screen_type, resolution):
        super().__init__(brand, model, price)
        self.screen_type = screen_type
        self.resolution = resolution

    def display_details(self):
        super().display_details()
        print(f"Screen Type: {self.screen_type}")
        print(f"Resolution: {self.resolution}")


# Creating instances of the classes
smartphone = Smartphone("Apple", "iPhone 13", 999, 6.1, 128)
laptop = Laptop("Dell", "Inspiron", 799, "Intel Core i5", 8)
tv = TV("Samsung", "QLED Q60A", 1299, "QLED", "4K UHD")

# Displaying the details of the electronic devices
print("Smartphone Details:")
smartphone.display_details()

print("\nLaptop Details:")
laptop.display_details()

print("\nTV Details:")
tv.display_details()"""

#Create a base class Shape with methods like draw and rotate. 
# Implement child classes like Rectangle, Circle, and Triangle, which inherit from Shape. 
# Override the draw and rotate methods for each child class to showcase the specific shape's
#  drawing and rotation.

"""class Shape:
    def draw(self):
        pass
    def rotate(self):
        pass
        
class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")
    def rotate(self):
        print("Rotating Rectangle")   
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")
    def rotate(self):
        print("Rotating Circle")   

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")
    def rotate(self):
        print("Rotating Triangle")

r=Rectangle()
c=Circle()
t=Triangle()  
r.rotate()
r.draw()
c.rotate()
c.draw()
t.rotate()
t.draw()
"""
#Create a base class Item with attributes like title, item_id, and availability_status. 
# Implement child classes like Book and DVD, which inherit from Item.
#  Add specific attributes and methods for each child class.  

"""class Item:
    def __init__(self,tittle,id,availability):
        self.tittle=tittle
        self.id=id
        self.availability=availability
    def display_details(self):
        print(f"Tittle: {self.tittle}")
        print(f"ID: {self.id}")
        print(f"Avaiability:{self.availability}")

class Book(Item):
    def __init__(self,tittle,id,availability,genere):
        self.genre=genere
        super().__init__(tittle,id,availability)
        print("Genre Of This Book",self.genre)
    def display_details(self):
        super().display_details()
        print(self.genre)
    def avail(self):
        print(self.availability)

class DVD(Item):
    def __init__(self,tittle,id,availability,taste):
        self.taste=taste
        super().__init__(tittle,id,availability)
        print("Genre Of This Book",self.taste)
    def display_details(self):
        super().display_details()
        print(self.taste)
    def issue(self):
        print(self.taste)

b=Book("The Loin King",52,"Yes","Story Mode")        
d=DVD("The Loin King Movie",25,"No","Thriller")
print("Book Details")
b.display_details()
print("DVD Details")
d.display_details()
b.avail()
d.issue()"""

#Create a base class Account with attributes like account_number, account_holder_name, and balance.
#  Implement child classes like SavingsAccount, CurrentAccount, and FixedDeposit, which inherit from Account.
#  Add specific methods for each child class, such as calculate_interest for SavingsAccount,
#  overdraft_limit for CurrentAccount, and calculate_maturity_amount for FixedDeposit.

"""class Account:
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Number: {self.number}")
        print(f"Balance:{self.balance:.2f}")

class SavingAccount(Account):
    def __init__(self, name, number, balance,current_balance,time,interest_rate):
        self.current_balance=current_balance
        self.time=time
        self.interest_rate=interest_rate
        if current_balance==0:
            print(self.current_balance)
        else:
            print("Recharge Your Balance")
        super().__init__(name, number, balance)
        print(self.current_balance)
        print(self.time)
        print(self.interest_rate)

    def display_details(self):
        super().display_details()
        print(self.current_balance)
    def calculate_intreset(self):
        return (self.current_balance*self.time*self.interest_rate)
    
class CurrentAccount(Account):
    def __init__(self, name, number, balance,current_balance,time,interest_rate):"""

#Implement a vehicle rental system with a base class Vehicle having attributes like make, model, and year,
#  and methods to calculate rental charges and display details.
#  Create child classes Car, Motorcycle, and Truck, 
# each with specific attributes like seating_capacity, rental_rate, etc.   

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def rental_charges(self):
        pass
    def display_details(self):
        print("Vehicle Details")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class Car(Vehicle):
    def __init__(self,make,model,year,seating_capacity,rental_rate):
        self.seating_capacity=seating_capacity
        self.rental_rate=rental_rate
        super().__init__(make,model,year)
        print(self.seating_capacity)
        print(rental_rate)

    def calculate(self,days):
        return (self.rental_rate*days)
    
    def display_details(self):
        super().display_details()
        print(self.seating_capacity)
        print(self.rental_rate)

class Truck(Vehicle):
    def __init__(self,make,model,year,seating_capacity,rental_rate):
        self.seating_capacity=seating_capacity
        self.rental_rate=rental_rate
        super().__init__(make,model,year)
        print(self.seating_capacity)
        print(rental_rate)

    def calculate(self,days):
        return (self.rental_rate*days)
    
    def display_details(self):
        super().display_details()
        print(self.seating_capacity)
        print(self.rental_rate)

c=Car("BMW","m4",2003,2,7)
t=Truck("Ford","Henry",2005,5,9)
print("Car Details")
c.display_details()
c.rental_charges()
print("Truck Details")
t.display_details()
t.rental_charges()



           


