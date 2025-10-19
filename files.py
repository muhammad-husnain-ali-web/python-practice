# read mod
f = open("files/file.txt") # is same as open("files/file.txt", "r") as this open in r mod
c = f.read()
print(c)
f.close()

# write mod
f = open("files/file.txt", 'w')
c = f.write("Helo this is changed") # it return length of string
print(c)
f.close()

# append mod
f = open("files/file.txt", 'a')
c = f.write("\nHello")
print(c)
f.close()

#  f.write(st) can assign str variable
st = "Hello how are you.\nHow is your coding.\nWhich language is favourite."
f = open("files/file1.txt", "w")
f.write(st)
f.close()


# this is same as 
with open("files/file2.txt", "w") as f:  # There is no need close file it automatically cose file 
    f.write(st)

# f.readlines()
with open("files/file2.txt", "r") as f:  # There is no need close file it automatically cose file 
    lines = f.readlines() # f.readlines() it read line one by one and return list of lines
    print(lines)


with open("files/file2.txt", "r") as f:  # There is no need close file it automatically cose file 
    line = f.readline()
    while line != "":
        print(line)
        line = f.readline()


# challenge or practice question
with open("files/practic.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I&O\nusing Java\nI like programming in Java")

with open("files/practic.txt", "r") as f:
    data = f.read()
    new = data.replace("Java", "Python")
with open("files/practic.txt", "w") as f:
    f.write(new)

word = "Python"
with open("files/practic.txt", "r") as f:
    data = f.read()
    if(word in data):
        print("Found")
    else:
        print("Not found")

word = "learning"
line = 1
data = True
with open("files/practic.txt", "r") as f:
    while data:
        data = f.readline()
        if(word in data):
            print("found", "at", line)
        line +=1


def checknumber(word):
    line = 1
    data = True
    with open("files/practic.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                return line
            line +=1
    return -1

x =input("Enter a number for search: ")
res = checknumber(x)
if(res!= -1):
    print("found", "at", res)
else:
    print("Not found")


# table write in files
def tableWrite(n):
    with open(f"files/tables/table{n}.txt", "w") as file:
        for i in range(1, 11):
            st = f"{n} * {i} = {n*i}\n"
            file.write(st)
for i in range(2, 11):
    tableWrite(i)