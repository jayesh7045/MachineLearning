def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Create a closure
add_five = outer_function(5)

# Use the closure
result = add_five(10)
print(result)  # Output: 15

## Same as there in JavaScript