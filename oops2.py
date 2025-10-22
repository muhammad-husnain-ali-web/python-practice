# delete del keyword
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Husnain")
print(s1.name)
del s1 # delete object from memory
print(s1) # ERROR

s2 = Student("Ali")
print(s2.name)
del s2.name # delete object attribute name from memory
print(s2) # no error 
print(s2.name) # error this attribute delete from memory

# private attribute or method
# pribvate attribute or method are only acccessible in the class and not accessible outside the class
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #private attribute ( __ make private attribute or method by adding brfore the attibute or method name )
    
    def password(self):
        print(self.__acc_pass)

a1 = Account("2323", "1234")
print(a1.acc_no)
a1.password()
print(a1.__acc_pass) # ERROR

class Employee:
    __name = "anonymous"
    
    def __hello(self, name):
        print("Hello", name)
    
    def welcome(self):
        self.__hello(self.__name)

e1 = Employee()
e1.welcome()


# Inheritance
# single level inheritance
class Vahicles:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def getNme(self):
        print("Name:", self.name)
    
    def display(self):
        print("Name:", self.name)
        print("Model:", self.model)

class Car(Vahicles):
    def __init__(self, brand, name, model):
        self.brand = brand
        super().__init__(name, model)
    
    def display(self): # oviride method
        print("Name:", self.brand)
        super().display()

c1 = Car("toyta", "furtuner", "2023")
c1.display() # call its own method if exit if not then call parant method
c1.getNme() # call parant method

# multi level inheritance
class Car:
    @staticmethod
    def start():
        print("car start")
    
    @staticmethod
    def stop():
        print("car stop")

class ToyataCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyataCar):
    def __init__(self, tye):
        self.type = tye

c1 = Fortuner("2025") 
c1.start() # call parant method

# multiple inheritance
class A:
    varA = "welcome to A class"
class B:
    varB = "welcome to B class"
class C(A, B):
    varC = "welcome to C class"

c = C()
print(c.varA)
print(c.varB)
print(c.varC)


# class method
class Person:
    name = "anonymous"
    
    def changeName(self, name):
        self.name = name

p1 = Person()
p2= Person()
p1.changeName("Husnain")
print(p1.name)
print(p2.name)
print(Person.name)

class Person:
    name = "anonymous"
    
    # def changeName(self, name):
    #     self.__class__.name = name
    
    # def changeName(self, name):
    #     Person.name = name
    
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p2 = Person()
p1.changeName("Husnain")
print(p1.name)
print(p2.name)
print(Person.name)

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.prcantage = str((self.phy + self.chem + self.math)/3) + "%"
        

s1 = Student(32, 55, 67)
print(s1.phy)
print(s1.chem)
print(s1.math)
print(s1.prcantage)
s1.phy = 100
print(s1.prcantage) # still showing old data


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    # recommended 
    @property
    def prcantage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
    
    # first way to handle this changing 
    # def updateParcantage(self):
    #     self.prcantage = str((self.phy + self.chem + self.math)/3) + "%"
    

# now for when any change
# s2 = Student(32, 55, 67)
# print(s2.phy)
# print(s2.chem)
# print(s2.math)
# print(s2.prcantage)
# s2.phy = 100
# s2.updateParcantage() # call the update parcantahe function
# print(s2.prcantage) # it show the new data

s1 = Student(32, 55, 67)
print(s1.phy)
print(s1.chem)
print(s1.math)
print(s1.prcantage)
s1.phy = 100 # now there is no need to change it mannully
print(s1.prcantage)


# polymorphism 
# polymorphism when same operter or function has the different meaning in differnt context
# polymorphism is inheritance when base class and dervied class same function but they work differnt for both classes

# simple class
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(f"{self.real}i + {self.img}j")
    
    def add(self, obj2):
        newReal = self.real + obj2.real
        newImg = self.img + obj2.img
        return Complex(newReal, newImg)

c1 = Complex(1,5)
c1.showNumber()
c2 = Complex(1,5)
c2.showNumber()
c3 = c1.add(c2)
c3.showNumber()

# Polymorphism change meaning of + 
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(f"{self.real}i + {self.img}j")
    
    def __add__(self, obj2):
        newReal = self.real + obj2.real
        newImg = self.img + obj2.img
        return Complex(newReal, newImg)

c1 = Complex(1,5)
c1.showNumber()
c2 = Complex(1,5)
c2.showNumber()
c3 = c1 + c2 # change meaning of + hear 
c3.showNumber()


# challenge or practice question
class Circle:
    def __init__(self, raduis):
        self.raduis = raduis
    
    def area(self):
        return (22/7) * self.raduis ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.raduis

c1 = Circle(20)
print(c1.area())
print(c1.perimeter())

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Role:", self.role)
        print("Dept:", self.dept)
        print("Salary:", self.salary)

e1 = Employee("accountant", "Finance", "60,000")
e1.showDetails()

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Role:", self.role)
        print("Dept:", self.dept)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "20,000")
    
    def showDetails(self): # Polymorphism base and derived same funtion but defferent meaning
        print("Name:", self.name)
        print("Age:", self.age)
        return super().showDetails()

e1 = Engineer("Husnain", 21)
e1.showDetails()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, obj2):
        return self.price > obj2.price
    
    def __lt__(self, obj2):
        return self.price < obj2.price

o1 = Order("Chips", 20)
o2 = Order("Kurkure", 15)
print(o1 > o2)