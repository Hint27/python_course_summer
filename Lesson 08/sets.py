# A set is a collection which is unordered, unchangeable*, and unindexed.

my_set = { "Apple", "Banana", "Cherry" }
my_set_constructor = set(("Python", "Js"))
print(my_set)
print(my_set_constructor)

# Unchangeable
# my_set[0] = "Ball"
# print(my_set)

# No Duplicate Allowed
# The values True and 1 are considered the same value in sets, and are treated as duplicates:
my_set2 = { True, 1, 2, 3, False, 0 }
print(my_set2)

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can check if an element exists in a set using the 'in' keyword

print(2 in my_set2)
print(5 in my_set2)

# Adding An Item to set
my_set3 = { "Laptop", "Phone" }
print(my_set3)
my_set3.add("HeadPhone")
print(my_set3)

# using the update method
my_set3.update({"iPhone", "PowerBank"})
print(my_set3)

# union method
one = {1, 2, 3}
two = {4, 5, 6}

new_set = two.union(one)
print(new_set)

# Remove Set Items
rm_set = { "apple", "banana", "cherry" }
rm_set.remove("banana")
print(rm_set)
# rm_set.remove("Banana")
# print(rm_set)

# discard method: item not exist, return None
rm_set.discard("apple")
print(rm_set)

# pop method
rm_set.update(("orange", "mango"))
print(rm_set)
rm_set.pop()
print(rm_set)

dupe_set = {1, True, 4, 5, False, 0}
print(dupe_set)

# Leaving only the duplicate
dupe_one = {1, 2, 3}
dupe_two = {1, 3, 5}

print(dupe_one.intersection(dupe_two))

# Leaving everything except the dupe
print(dupe_one.symmetric_difference(dupe_two))