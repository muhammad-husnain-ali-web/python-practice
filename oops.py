class Student:
    name = "student" # class attribute for all the object or intances that will intanitiate from this class

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)


class Student:
    def __init__(self, name, rn):  # this is the constructor that execute automatically when object is intantiate
        self.name = name  # these are the object attribute that every object can have these attribute value different
        self.rollNumber = rn

s1 = Student("Husnain", 100076)
print(s1.name, s1.rollNumber)

s2 = Student("Ali", 100042)
print(s2.name, s2.rollNumber)

class Student:
    university = "GCUF" # class can have the class attributes and object attributes
    name = "student" #  class and object are same tthen prefrence give to the object attribute
    def __init__(self, name, rn):
        self.name = name 
        self.rollNumber = rn

s1 = Student("Husnain", 100076)
print(s1.name, s1.rollNumber)

s2 = Student("Ali", 100042)
print(s2.name, s2.rollNumber)

s2.name = "Ali Hamza" # can change the attribute value furture
print(s2.name, s2.rollNumber)

class Student:
    university = "GCUF"
    name = "student"
    def __init__(self, name, rn):
        self.name = name 
        self.rollNumber = rn
    
    # class can have method are function 
    def detial(self):
        print("Student roll number:", self.rollNumber)
        print("Student name:", self.name)
    
    # class method need a parameter like with it if not write then have to pass that parameter even if not use
    # def inform(self):
    #     print("Hello students, please submit your fee quickly")
    
    #  solution is make that method static
    @staticmethod 
    def inform():
        print("Hello students, please submit your fee quickly")

s1 = Student("Husnain", 100076)
s1.detial()

s2 = Student("Ali", 100042)
s2.detial()

s2.name = "Ali Hamza" # can change the attribute value furture
s2.detial()
s2.inform()


# Abstraction and Encapsulation
# Abstraction is only show user need data there is no need to show other data
# Encapsulation is include all detail in class 
class Car:
    def __init__(self):
        self.acc = False
        self.breack = False
        self.clucth = False
    
    def start(self):
        self.breack = False
        self.clucth = True
        self.acc = True
        print("Car start")
    
    def stop(self):
        self.clucth = False
        self.acc = False
        self.breack = True
        print("Car Stop")

c1 = Car()
c1.start()
c1.stop()


# challenge or practice question

class Student: #Encapsulation
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
    def getAvg(self):
        # sum = 0
        # for val in self.marks: #Abstraction
        #     sum += val
        avg = (sum(self.marks)/len(self.marks))
        # print("Hi", self.name, ".your Avg score is:", sum/len(self.marks))
        print("Hi", self.name, ".your Avg score is:", avg)
s1 = Student("Husnain", [98, 97, 99])
s1.getAvg()

class Account():
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account
    
    def debit(self, amount):
        self.balance -= amount
        print (f"Rs. {amount} is debit")
        print("Total balance:", self.getBalance())
        
    def credit(self, amount):
        self.balance += amount
        print (f"Rs. {amount} is credit")
        print("Total balance:", self.getBalance())
    
    def getBalance(self):
        return self.balance

a1 = Account(10000, 5432)
a2 = Account(50000, 5472)

a1.debit(1000)
a1.debit(1000)

a2.debit(1000)

a2.credit(400)
a2.credit(540)

a1.credit(500)

a1.credit(40000)

a2.credit(45000)
a2.debit(4000)

a1.debit(5000)

