my_tuple = ('fan', 23, True, 23)
my_string = "Rode"

print(my_tuple)

# Boolean
truthy = True
falsy = False

print(type(my_tuple) == tuple)
print(type(my_string) == str)

# A comma (,) must be added after a tuple item
# to create a tuple with only one item.
my_tuple2 = ('Pepperoni',)

print(type(my_tuple2))

# tuple constructor
tuple_construtor = tuple(('Chicken',))

print(tuple_construtor)

# Access Tuples
print(my_tuple[0]) # First Item
print(my_tuple[-1]) # Last Item
print(my_tuple[1:])
print(my_tuple[-4:-1])
print(my_tuple[2:])

# Check Item Existence in tuples
print('Camera' in my_tuple)
print('fan' in my_tuple)

# Tuple Methods
print("\n" + "Adding Item To Tuple".center(30, "*"))
count_of_23 = my_tuple.count(23)
print(count_of_23)

print(my_tuple.index('fan'))

# Unpacking of tuples
print("Unpacking of tuples".center(30, '='))
plants = ('maize', 'yam', 'grape', 'carrot', 'cucumber')

#(maize, yam, *remaining) = plants
(maize, *remaining, cucumber) = plants

print(maize)
#print(yam)
print(remaining)
print(cucumber)