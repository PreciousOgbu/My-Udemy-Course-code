# DICTIONARY

#  Accessing elements from a dictionary
# new_dict = {1: "Hello", 2: "Hi", 3: "Hola"}
# print(new_dict)
# print(new_dict[1])
# print(new_dict.get(2))

# # Updating value
# new_dict[1] = "Hey"
# print(new_dict)

# # Adding value
# new_dict[4] = 'Namaste'
# print(new_dict)


# Creating a new dictionary
#squares = {1:1, 2:4, 3:9, 4:16, 5:25}
# print(squares)

# # Remove a particular item
# print(squares.pop(4))
# print(squares)

# Remove an arbitary item
# print(squares.popitem())
# print(squares)

# delete a particular item
# del squares[1]
# print(squares)

# remove all items 
#squares.clear()

# Output: {}
#print(squares)

# Delete the dicttionary itself
#del squares

# Throws an error when prompted to print squares
#print(squares)


# Creating a new dictionary using comprehension
# squares = {x: x*x for x in range(6)}
# print(squares)


# Dictionary Membership test
# squares = {1: 1, 3: 9, 5: 25, 7: 49, 9:81}
# print(1 in squares)
# print(2 not in squares)

# Membership tests for key only not value
#print (49 in squares)

# Iterating through a dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])

# Using built in functions in a dictionary 
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(len(squares))
print(sorted(squares))

