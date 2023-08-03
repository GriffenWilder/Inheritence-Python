#Iter and Iteration
"""Tup="Mohsin","Aasim","Qasim"
Repetation=iter(Tup)
print(next(Repetation))
print(next(Repetation))
print(next(Repetation))"""
#Polymorphsim
"""class Car:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def Move(self):
        print("Drive!")
    def Type(self):
        print("Land Vehicle")
class Ship:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def Move(self):
        print("Sail!")
    def Type(self):
        print("Water Vehicle")     
class Plane:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def Move(self):
        print("Fly!")
    def Type(self):
        print("Air Vehicle")           
my1=Car("Mustang","SUV")
my2=Ship("Murree","Oil Tanker")
my3=Plane("Boieng","Passanger")  
for x in (my1,my2,my3):
    x.Move() 
    x.Type()"""
#Parent Classes and Child Classes Polymorphsism
#Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle
"""class Vehicle:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def move(self):
        print("Drive!")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail")
class Plane(Vehicle):
    def move(self):
        print("Fly")
my1=Car("Mustang","SUV")
my2=Boat("Murree","Oil Tanker")
my3=Plane("Boieng","Passanger")  
for x in(my1,my2,my3):
    print(x.brand)   
    print(x.model)      
    x.move() """
#Create a class representing a basic car. It should have attributes like make, model, year, 
# and color. 
# Implement methods to change the color of the car and display its details. 

"""class Car:
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
    def changeclor(self,new_color):
        self.changeclor=new_color
print(Car)"""

""""Create a class called Vehicle with attributes like make, model, and year. 
Implement child classes Car, Motorcycle, and Truck, which inherit from Vehicle.
 Each child class should have additional attributes specific to that type of vehicle."""

"""class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class Car(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make, model, year)
class Motorcycle(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make, model, year)
class Truck(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make, model, year)
my1=Vehicle.Car("Mustang","Ford","1998")
my2=Vehicle.Motorcycle("Suzuki","Davidson","1999")
my3=Vehicle.Truck("Zummer","Hummer","1978")
print(my1)
print(my2)
print(my3)"""

#Implement a class Shape with methods to calculate the area and perimeter. 
# Create child classes Rectangle, Circle, and Triangle, which inherit from Shape.

#  Each child class should override the area and perimeter calculation methods according to its specific shape.
"""import math
class Shape:
    def __init__(self,area,parameter):
        self.area=area
        self.parameter=parameter
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.length*self.width
    def calculate_parameter(self):
        return 2*(self.length+self.width) 
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return math.pi*self.radius*self.radius
    def calculate_parameter(self):
        return 2*math.pi*self.radius
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def calculate_area(self):
        return(self.side1*self.side2*self.side3)/2
    def calculate_parameter(self):
        return(self.side1+self.side2+self.side3)

r=Rectangle(10,20)
c=Circle(5)
t=Triangle(5,10,15)
#print(r)
print("Area of Rectangle",r.calculate_area())
print("Parameter of Rectangle",r.calculate_parameter())
#print(c)
print("Area of Circle",c.calculate_area())
print("Parameter of Circle",c.calculate_parameter())
#print(t)
print("Area of Triangle",t.calculate_area())
print("Parameter of Triangle",t.calculate_parameter())"""

#Create a base class Employee with attributes like name, employee_id, and salary. 
# Implement child classes Manager and Developer, which inherit from Employee.
#  Add specific attributes and methods for each child class.
"""class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
class Manager(Employee):
    def __init__(self,name,id,salary):
        super().__init__(self,name,id,salary)
    def display_details(self):
        super().display_details()
        #print("Developer Details",self.name,self.id,self.salary)   
class Developer(Employee):
    def __init__(self,name,id,salary):
        super().__init__(self,name,id,salary)
    def display_details(self):
        super().display_details()
        #print("Developer Details",self.name,self.id,self.salary)

m=Manager("Mohsin ALi",8,"150000")
d=Developer("Aasim",9,"180000")
print("Manager",m.name())
print("Manager",m.id())
print("Manager",m.salary())
print("Manager",d.name())
print("Manager",d.id())
print("Manager",d.salary())
Manager.display_details()"""

#Implement a base class Animal with methods like speak and move.
# Create child classes like Dog, Cat, and Bird, which inherit from Animal. 
#Each child class should override the speak and move methods according to the specific behavior of the animal.

class Animal:
       def speak(self):

        pass
       def speak(self):
        
        pass
class Dog(Animal,):
  
    def move(self):
        return"1"
    def speak(self):
        return"Woof!"
class Cat(Animal):
  
    def move(self):
        return "2"
    def speak(self):
        return"Meoow"    
class Bird(Animal):
    
    def move(self):
        return "3"
    def speak(self):
        return"Humms" 
dog =Dog()
cat = Cat()
bird = Bird()
print("Dog",dog.speak())
print("Dog",dog.move())