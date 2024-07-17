#  # Name (also called identifier) is simply a name given to objects

# # We can get the address (in RAM) of some objects through the built-in function, id()
# # You may get different value of id

# a = 2
# # Output: id(2) = 14073067722360
# print(f'id (2) = {id(2)}')

# # Output: id(a) = 1407298800684360
# print(f'id(a) = {id(a)}')

# a = a+1
# # Output: id(a) =
# print(f'id(a) = {id(a)}')

# # Output: id(3) =
# print(f'id(3) = {id(3)}')

# b = 2
# # Output: id(a) =
# print(f'id(b) = {id(b)}')

# Scope
def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print(f'a = {a}')

    inner_function()
    print(f'a = {a}')

a = 10
print(f'a = {a}')
outer_function()
print(f'a = {a}')