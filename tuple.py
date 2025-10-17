tup1 = (1,)  # tup1 = (1) is invalid beacause its consider as inter or accoroing to datatype and its type is inter or accoroing to datatype
tup = (50,45,21,45,64,73,33) # immutable cannot be changed

print(type(tup))
print(tup)
print(tup[0]) # immutable

# invalid
# tup[0] = "hello" # immutable cannot be changed / ERROR


# slice Slice is same as str and list
print(tup[1:4])
print(tup[:4])  # is same as tup[0:4]
print(tup[1:]) # is same tup[1:len(tup)]
print("negitive selice")
print(tup[-4:-2])

# # method
print(tup)
c = tup.count(45)
print(c)
i = tup.index(33)
print(i)
print(len(tup))


# challenge or practice question
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

list = list(grade)
print(list)
list.sort()
print(list)

