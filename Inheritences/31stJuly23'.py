"""class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def myfunc(self):
        print("My Name Is "+self.name)  
Boggy=person("Mohsin Ali",177854)
print(Boggy)
Boggy.myfunc()"""

#instead of self parameter you can use any other word too


"""class Animals:
    pass
    def __init__(landanimals,name,legs):
        landanimals.name=name
        landanimals.legs=legs
    def myfunc(abc):
        print("These are all the animals "+abc.name)
        

A1=Animals("Tiger",4)
A1.legs=4
A1.myfunc()
print(A1.legs)"""

#Inheritence
#Class into Class
#__init_ class
#super init
"""class Student:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def printname(self):
        print(self.name,self.gender)  
class Person:
    def __init__(self,name,gender):
        super().__init__(name,gender)  
        self.graduationyear=2024      
P1=Student("Mohsin","Male")
print(P1.graduationyear)"""

        