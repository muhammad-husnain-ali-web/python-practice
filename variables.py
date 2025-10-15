x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

name = "Husnain" #name is a string value
age = 21 #name is a integer value
cgpa = 3.65 #name is a floating value
is_learning_python = True #name is a boolen value

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_learning_python))


# All there give same output
print("Name:", name)
print("Age:", age)
print("Cgpa:", cgpa)
print("Learning Python:", is_learning_python)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Cgpa: {cgpa}")
print(f"Learning Python: {is_learning_python}")

print(f"Name: {name}\nAge: {age}\nCgpa: {cgpa}\nLearning Python: {is_learning_python}")

# typecasting
marks = 50.0 #floating value
marks = int(marks)
print(marks)


# typecasting into integer beacause the value that input is string
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
print(f"Sum of {a} and {b} is: {a+b}")

# string variation 
name1 = "Husnain"
name2 = 'Husnain "Ali"'
name3 = """Husnain "Ali" """
print(f"Name1: {name1}\nName2: {name2}\nName3: {name3} {len(name2)}")


# string is immutable means string cannot be change 
str1 = "Husnain"
str2 = "Ali"
print(str1+str2)
print(str1+" "+str2)
print(str1)
print(str2)
print(str1[1]) # get the value from the index of str1 index start from 0 and end at (len(str)-1)


# slice
print(str1[1:4]) # start from 1 (include starting index) to 4 (excluding ending index)
print(str1[:4])  # is same as str[0:4] starting from 0 index
print(str1[4:]) # is same str[1:len(str)] starting from len(str) index
print("negitive selice")
print(str1[-5:-1]) #staring count index from right
print(str1[2:6])  # is same as str[-5:-1] 


# str function
print(str1.endswith("in")) # return boolen value (true or false)
print(str1.startswith("H")) # return boolen value (true or false)
print(str1.capitalize()) # All funtion dont change str it return new string
print(str1.upper()) # All funtion dont change str it return new string
print(str1.lower()) # All funtion dont change str it return new string
print(str1.replace("H","My"))  # All funtion dont change str it return new string
print(str1.find("na")) # give the starting index of value if value found if not not found it return -1
print(len(str1)) # return length of str
print(str1.count("i")) # return the count for value in str how many time it comes in str
print(str1)  #Original is not change new string is create



# Mini Challange 
favorite_book = "Atomic Habits"
age = 21
temperature = 36.5
is_learning_python = True
print(f"My favorite book is {favorite_book}.\nI am {age} years old.\nToday's temperature is {temperature}°C.\nI am learning Python for AI: {is_learning_python}")
