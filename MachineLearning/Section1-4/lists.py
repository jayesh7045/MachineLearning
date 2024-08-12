l1 = ["a", "b", "c", "d", "e"]
print(l1[0:-3])
l1[1:] = "watermelon"
print(l1)
l1.append(100)
print(l1)
l1.pop()
print(l1)
l1.insert(1, "Jayesh")
print(l1)
l1.remove("Jayesh")
print(l1)
l1.index("w")
print(l1)
print(l1.count('a'))
l1.reverse()
print(l1)
l1.sort()
print(l1)
l1.clear()
print(l1)
for number in range(10):
    print(number**2)
    
    
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jayi"]
for index,num in enumerate(l3):
    print(index, num)
    
    

# List Comprehension
l2 = [i**2 for i in range(10)]
print(l2)

# List Comprehension
l3 = [num for num in range(10) if num %2 == 0]
print(l3)


empty_list = list()
print(type(empty_list))
