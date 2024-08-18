# This is the normal Function
def square(num):
    for i in range(num):
        return i**2

print(square(3))

###########################_____#######################################################################_____#################################################_______#################################################__________________#################################################____

# This is Generator wala function
def square_(num):
    for i in range(num):
        yield i**2
    
Generator_obj = square_(3)
print(Generator_obj)

try:
    print(next(Generator_obj))
    print(next(Generator_obj))
    print(next(Generator_obj))
    print(next(Generator_obj))
except StopIteration:
    print("No more data in Generator Object")

print()
print()
print()
print("Iterating Using For Loop")
Generator_obj_ = square_(3)
for i in Generator_obj_:
    print(i)
print()
print()

###########################_____#######################################################################_____#################################################_______#################################################__________________#################################################____

    
