# List and list are mutable can be changed
marks = [90, 40, 50, 40, 59, 368, 38, 3, 3]

print(type(marks))
print(marks)
print(marks[4])

# valid
# tup[0] = "hello" # mutable can be changed

# slice , slice is same as string
print(marks[1:4])
print(marks[:4])  # is same as marks[0:4]
print(marks[1:]) # is same marks[1:len(marks)]
print("negitive selice")
print(marks[-5:-1])


# list function or matheds

# append a new element at the end of list
marks.append(6)
print(marks)

# sort and sort(reverse=True) sort lis in accending or desending order on the basis of number if integer or the string charter if string
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

# reverse the order of list
marks.reverse()
print(marks)


# in this first is index and the second is the elemet that will add in list
marks.insert(2,1) 
print(marks)

c=marks.copy() # return the copy of list
print(marks)
print(c)

marks.remove(40) # remove the element from list
print(marks)

# give index to this and it will pop or remove value from this index
marks.pop(2)
print(marks)


i = marks.index(50) # give index if give value to this if not then error
print(i)

# count count the how much time value
c = marks.count(3)
print(c)

print(len(marks))

digit = ["h", "f", "r", "a", "e", "c", "b"]
student = ["Husnain",85, 68.9, True ] 

print(digit)
print(type(digit))
print(student)
print(type(student))

digit.sort()
print(digit)


# challenge or practice question
movies = []
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))
print(movies)

# alternate
movies = []
movies.insert(0,(input("Enter 1st movie: ")))
movies.insert(1,(input("Enter 2nd movie: ")))
movies.insert(2,(input("Enter 3rd movie: ")))
print(movies)


# list palindrome
list = [1, 2, 3, 2, 5]
copyList = list.copy()
copyList.reverse()
if(list == copyList):
    print(list, "is palindrome")
else:
    print(list, "is not palindrome")
