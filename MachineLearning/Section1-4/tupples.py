# Tupples are immutable
empty_tupple = () #empty_tupple
empty_tupple1 = tuple()
print(empty_tupple1)
print(empty_tupple)
print(type(empty_tupple))

#Converting list to tuple
tp1 = tuple([1, 2, 3, 4])
print(type(tp1))

tp2 = [(1, 2, 3, 4)]
print(tp2)
print(type(tp2))



# In list as well as in tuple we can make use of different types of datatype elements
tp3 = (1, 2, 4, 10, "Jayesh", "Wadhwani", 100)
tp4 = ("Basu", "Rutik")
# We can add two tuples as well
tp5 = tp3+tp4
print(tp5)


# We can extend tuple by multiplying it
multiply_tuple = (1, 2, 3)
print(multiply_tuple*3)  # This will multiply the tuple 3 times. But this wont change the Main tuple
print(multiply_tuple)


for i in (multiply_tuple):
    print(i*4)
    

tp5 = ["Jayesh", "Harish", "Wadhwani"]
a, v, c = tp5
g = a+v+c
print(g)
print(a, v, c)

# We can have
# Nested List
# Nested Tuples
# Nested List and tuples

 