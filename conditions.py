# if condition 
age = 21
if(age>=18):
    print("you are adult")
    
# if else condition 
age = 17
if(age>=18):
    print("you are adult")
else:
    print("you are not adult")

# if else if condition
light = input("Enter light color: ")
if(light=="green"):
    print("Go")
elif(light=="red"):
    print("Stop")
elif(light=="yellow"):
    print("Wait")
else:
    print("Invalid light")
    
# Nestig condition
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if(a>b):
    if(a>c):
        print(a, "is greatest number")
    else:
        print(c, "is greatest number")
else:
    if(b>c):
        print(b, "is greatest number")
    else:
        print(c, "is greatest number")

if(a>b and a>c):
    print(a, "is greatest number")
elif(b>a and b>c):
    print(b, "is greatest number")
else:
    print(c, "is greatest number")


# challange

mark = int(input("Enter student mark: "))
if(mark>=100 and mark<=90):
    print("Student grade is A.")
elif(mark>=80):
    print("Student grade is B.")
elif(mark>=70):
    print("Student grade is C.")
elif(mark>=40):
    print("Student grade is D.")
else:   
    print("Student grade is F.")

n = int(input("Enter a number: "))
if(n%2==0):
    print(n, "is even")
else:
    print(n, "is odd")

n = int(input("Enter a number: "))
if(n%7==0):
    print(n, "is a multipe 7")
else:
    print(n, "is not a multipe 7")
