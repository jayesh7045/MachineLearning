my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
print(type(my_iterator))  # This is <class 'list_iterator'> This line is printed by the __str__ function which is a dundder method
print(next(my_iterator))

try:
    
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))

except StopIteration:
    print("No More Elements in the list")
