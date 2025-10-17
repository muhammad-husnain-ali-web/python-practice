# mutable can be change
dict = {
    "name": "Husnain",
    "rollno": 100076,
    "CGPA": 3.89
}

print(dict)
print(type(dict))
print(dict["name"])

student = {
    "name" : "Husnain",
    "subject" : ("python","C","Java","Javascript"), #any type can be used in key value
    "rollNo" : 100076,
    "CGPA" : 3.78,
}

print(student)
# if key exist then change this key value but if not exist then make new key value pair
student["name"] = "Muhammad Husnain" 
student["surname"] = "Ali"
print(student)
print(student["subject"])
print(student["subject"][0])

# Empty dict and after can assign value to it
dict1 = {}
print(dict1)
dict1["name"] = "Husnain"
print(dict1)


# nesting dectionary
student1 = {
    "name" : "Husnain",
    "rollNo" : 100076,
    "subject" : {
        "phy" : 97,
        "chem": 98,
        "math" : 95,
        "h" : [5, 7, 8]
    }
}
print(student1)
print(student1["subject"]["phy"])
print(student1["subject"]["h"][1])


# Method
print(len(student))
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(tuple(student.keys()))
print(len(tuple(student.keys())))

print(student.values())
print(list(student.values()))
print(len(list(student.values())))
print(tuple(student.values()))
print(len(tuple(student.values())))

print(student.items())
pairs = list(student.items())
print(pairs)
print(pairs[0])
print(pairs[2])
print(pairs[2][0])
print(pairs[1][1][0])

print(student.get("name")) #If key does not exist then it return None
r = student.get("name")
print(r)

student.update({"controy" : "Pakistan"})
print(student)
temp = {
    "controy" : "USA",
    "age" : 20,
}
student.update(temp)
print(student)



# challenge or practice question
Dict = {
    "cat": "a small animal",
    "table" : ("a piece of furniture", "list of fact & figure")
}
print(Dict)

marks = {}
marks.update({"phy": int(input("Enter phy marks: "))})
marks.update({"chem": int(input("Enter chem marks: "))})
marks.update({"math": int(input("Enter math marks: "))})
print(marks)