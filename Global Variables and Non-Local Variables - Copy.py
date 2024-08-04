# Global and Local variable with different name
# x = "global" #Global variable caan be accesed from anywhere
# def funct1():
#     global x
#     y = "local"
#     x = x * 2
#     print(x)
#     print(y)

# print("Global x = ", x)
# funct1()
# print("Global x =", x)


# Global and local varaible with same name
# a = 5
# def funct2():
#     a = 10   #Local variables are accessed from the block where it is defined only
#     print("local a:", a)
    
# print("global a: ", a)
# funct2()
# print("global a: ", a)


# Creating and using non-local variables 
def outer():
    x = 'local'

    def inner():
        #nonlocal x  # Nonlocal variable are used in nested function
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer:', x)

outer()
