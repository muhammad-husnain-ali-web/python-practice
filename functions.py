# function 
def helloWord():
    print("Hello World")
helloWord()

#  functions with parameters but it gives error if not found all parameters
def sum01(a, b):
    print(a+b)
sum01(2, 3)

# function with parameter but it not gives error if not found all parameters as it assign default value to parameters
def sum02(a=0, b=0):
    print(a+b)
sum02(2, 3)

# function with default parameter
def user(name="user"):
    print(f"Hello, {name}")

user("Husnain")
user()

# return value function
def sum03(a, b):
    return a+b
a = sum03(2, 3)
print(a)


# star print functions
def starPrint():
    for i in range(1, 6, 1):
        for j in range(1, 6, 1):
            print("*", end ="")
        print(end="\n")

starPrint()


# recursion function
def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n-1)

print(fact(5))


# challenge or practice question

# find lenght of list
def lenList(lst):
    print("Length of list", len(lst))
    print(lst)
list = [1,2,3,4,5,5]
lenList(list)

# print list
def printList(lst):
    for i in range(len(lst)):
        print(lst[i], end=" ")
    for el in lst:
        print(el, end=" ")
list = [1,2,3,4,5,5]
printList(list)


# factorial find
def fact(n):
    fact = 1
    for i in range(1, n+1,):
        fact *= i
    return fact
x = int(input("Enter range of factorial: "))
fac = fact(x)
print("Factorial of", x, "is:", fac)

# same 
def fact1(n):
    if(n==1 or n==0):
        return 1
    return n * fact1(n-1)
x = int(input("Enter range of factorial: "))
fac = fact1(x)
print("Factorial of", x, "is:", fac)

#  usd to pkr converter
def convertor(v):
    return v*290
u = int(input("Enter USD for Rupees: "))
p = convertor(u)
print(u, "USD", "=", p, "PKR")

# sum funtion
def sum1(n):
    if(n==1 or n==0):
        return 1
    return n + sum1(n-1)
x = int(input("Enter range of factorial: "))
s = sum1(x)
print("Factorial of", x, "is:", s)

# sum list
def sumList(lst):
    print(sum(lst))
list = [1,2,3,4,5,5]
sumList(list)

# Variable arguments (*args)
def total(*numbers):
    print(numbers)
    print(type(numbers))
    print(sum(numbers))

total(1, 2, 3, 4, 5)


# Keyword variable arguments (**kwargs)
def info(**data):
    print(data)
    print(type(data))

info(name="Husnain", age=21, course="Python for AI")