# vlae in set must be immutable but set is mutable 
set1 = {1, 2, 4, "Hello", "world"}
set2 = {5, 3, "Hello", "world", "Hello"} # repative value remove automatically
print(set1)
print(type(set1))
print(len(set1))
print(len(set2)) # 4 lenth as Hello comes 2 times

set3 = set() # empty set if set = {} it is as dectionay

set3.add(1)
set3.add(1) # if duplicate it will add only once
print(set3)

set3.add("Hello")
print(set3)

set3.add(3)
print(set3)

set3.add((4, 5, 4))
print(set3)

set3.remove(3) # remave value from set if not found then error
print(set3)

# set3.clear() # cear set empty set
# print(set3)

set3.pop() # Pop any rondom value or values from set
print(set3)

print(set1.union(set2)) 

print(set1.intersection(set2))


# challenge or practice question
courses = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(courses)
print(f"{len(courses)} class room required for 1 subject")

values = {9, 9.0} #value hash same 
print(values)
values = {9, "9.0"}
values = {("int", 9), ("float", 9.0)}
print(values)
print(type(values))