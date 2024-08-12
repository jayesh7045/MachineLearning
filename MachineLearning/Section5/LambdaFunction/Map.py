def square(x):
    return x**2;
list1 = [1, 2, 3, 4, 5]
data = list(map(square, list1));
print(data)



#* Similar thing can be achieved using the lambda function
data2 = list(map(lambda x : x**2, list1))
print(data2)

#* Problem Statement -> To add the elements of the 2 lists and return the final output list
a = [1, 2, 3]
b = [4, 5, 6]
added_list = list(map(lambda x, y : x+y, a, b))
print(added_list)

#* Use map and convert list of string to int
list_of_strings = ["23", "34", "78"]
print(list(map(lambda x : int(x), list_of_strings)))
