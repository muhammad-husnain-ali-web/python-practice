i=1
while i<=10 :
    print(i)
    i += 1

i=10
while(i>=1):
    print(i)
    i -= 1

x = int(input("Enter a number for search: "))
list = (1, 4, 16, 25, 36, 49, 64, 81, 100)
i=0
while i<len(list):
    if(x==list[i]):
        print(list[i], "found at", i)
        break # break is to exist from loop
    else:
        print("finding.....")
    i += 1
else: # this else run if it check all tuple and fount or break  not exicute 
    print("Not Found")
    
x = int(input("Enter a number for search: "))
list = (1, 4, 16, 25, 36, 49, 64, 81, 100)
i=0
while i<len(list):
    if(x==list[i]):
        print(list[i], "found at", i)
    else:
        print("finding.....")
    i += 1
else: # this else execute even it found the number beacause loop is full execute there is no break 
    print("Not Found")


# both loops are same 
i=1
while i<=20:
    if(i%2!=0):
        i += 1
        continue # continue is skip remaining instruction of the iteration and start new iteration
    print(i)
    i += 1

i=1
while i<=20:
    if(i%2==0):
        print(i)
    i += 1


# table of any number
num = int(input("Enter a number for table: "))
i=1
while i<=10:
    print(f"{num} * {i} = {num*i}")
    i += 1



# challenge or practice question

print("1 to 100")
i=1
while i<=100:
    print(i)
    i += 1

print("100 to 1")
i=100
while i>=1 :
    print(i)
    i -= 1


# table
n = int(input("Enter a number for table: "))
i=1
while i<=10:
    print(n, "*", i, "=", n*i)
    i += 1

# list travise
list = [1, 4, 16, 25, 36, 49, 64, 81, 100]
i=0
while i<len(list):
    print(list[i])
    i += 1

# sum of first n natural number
sum = 0
i = 1
n = int(input("Enter range of number for sum: "))
while i<=n:
    sum += i
    i += 1
print("Sum:", sum)

# factorial of first n natural number
fact = 1
i = 1
n = int(input("Enter range of number for fact: "))
while i<=n:
    fact *= i
    i += 1
print("Fact:", fact)


# for loop

# list
list = (1, 4, 16, 25, 36, 49, 64, 81, 100)
for el in list:
    print(el)

# tuple
tup = (1, 4, 16, 25, 36, 49, 64, 81, 100)
for el in tup:
    print(el)

# string
str = "Husnain"
for el in str:
    print(el)

# set
set = {1, 4, 16, 25, 36, 49, 64, 81, 100}
for el in set:
    print(el)


# find from list/ tuple
x = int(input("Enter a number for search: "))
list = (1, 4, 16, 25, 36, 49, 64, 81, 100)
i=0
for el in list:
    if(x==el):
        print(el, "found at", i)
        break
    print(el)
    i += 1
else:
    print("Not finding")


# only stoping value
for i in range(10): #range start form 0 and increase by 1 and  ending value not include but startin value include # range(start, stop, step)
    print(i)

# starting and stoping value
for i in range(1, 11):
    if(i%2==0):
        print(i)

# starting and stoping value and step/increasing value
for i in range(2, 11, 2):
    print(i)

# step can be decrement / increament
for i in range(100, 0, -1):
    print(i)
for i in range(1, 101, 1):
    print(i)

for i in range(10): #if pass keyword compiler generate error
    pass

print("Husnain")



# challenge or practice question

# list travise
list = [1, 4, 16, 25, 36, 49, 64, 81, 100]
for el in list:
    print(el)

# search element from tuple
x = int(input("Enter a number for search: "))
list = (1, 4, 16, 25, 36, 49, 64, 81, 100)
for el in list:
    if(x==el):
        print(el, "found")
        break
else:
    print("Not finding")

# list travise
list = [1, 4, 16, 25, 36, 49, 64, 81, 100]
for i in range(len(list)):
    print(list[i])

# search element from a list
x = int(input("Enter a number for search: "))
list = (1, 4, 16, 25, 36, 49, 64, 81, 100)
for i in range(len(list)):
    if(x==list[i]):
        print(list[i], "found")
        break
else: #optional
    print("Not finding")

# 1 to 100
for i in range(1, 111, 1):
    print(i)

# 100 to 1
for i in range(100, 0, -1):
    print(i)

# table 
n = int(input("Enter a number for table: "))
for i in range(1, 11):
    # print(n, "*", i, "=", n*i)
    print(f"{n} * {i} = {n*i}")

# sum of first n natural number
sum = 0
n = int(input("Enter range of number for sum: "))
for i in range(1, n+1):
    sum += i
    i += 1
print("Sum:", sum)

# factorial of first n natural number
fact = 1
n = int(input("Enter range of number for fact: "))
for i in range(1, n+1):
    fact *= i
    i += 1
print("fact:", fact)