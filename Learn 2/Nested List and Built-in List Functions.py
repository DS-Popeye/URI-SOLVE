
print("Original")
list =[ 80, 50, 70, 90, 44, 60]
print(list)

print("append") 
list.append(55)
print(list)

print("insert")
list.insert(list[2],44)
print(list)

print("insert")
list.insert(2,44)
print(list)

print("extend")
list.extend([0, 1, 2, 3, 4])
print(list)

print("extend")
list = list + [0, 1, 2, 3, 4]
print(list)

print("Remove")
list.remove(list[0])
print(list)

print("remove")
list.remove(70)
print(list)

print("Remove at last")
list.pop()
print(list)

print("sort")
list.sort()
print(list)

print("Index")
print(list.index(60))
print(list)

print("Count")
print(list.count(44))