# Global and Local variable with different name
x = "global"
def funct1():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

print("Global x = ", x)
funct1()