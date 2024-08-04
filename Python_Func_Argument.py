# # Function Arguments 


# def findMax(a, b):       # Function taking arguments and returning a value 
#     if a >b:
#         return a
#     else:
#         return b
    

# print(f'Max number between 10 and 20 is {findMax(10, 20)}')

# def hello(name, msg = ", how are you?"):    # Function with default parameter
#     print("Hello ", name, msg)


# hello("Presh,", "have a nice day")
# hello("Presh")


# def sumAll(*args):     # Function with aarbitary arguments 
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
    
# print("Sum of all the integers between 1-5 is ", sumAll(1,2,3,4,5))


def defaultArg(a,b,c):    
    print(f'a = {a}, b = {b}, c = {c}')


defaultArg(10, 20, 30 )