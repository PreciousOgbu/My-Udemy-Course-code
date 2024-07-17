
# Value1 = 100
# print(type(Value1))
# print(isinstance(Value1, int))
# print(isinstance(Value1, float))
# print(isinstance(Value1, complex ))


# Value2 = 100.24
# print(type(Value2))
# print(isinstance(Value2, int))
# print(isinstance(Value2, float))
# print(isinstance(Value2, complex ))


# Value3 = 50 + 6j
# print(type(Value3))
# print(isinstance(Value3, int))
# print(isinstance(Value3, float))
# print(isinstance(Value3, complex ))


# print(0b1101)
# print(0xab)
# print(0o23)

# print(10 + 33.4)


# Type conversion
# print(int(10.5))
# print(int(-20.99))
# print(float(10))

# Python Decimal
# data1 = 0.1 + 0.2
# print(data1)
# data1 = 1.20 * 2.50
# print(data1)
# from decimal import Decimal as D
# print(D('0.1')+ D('0.2'))
# print(D('1.2') * D('2.5'))

# Python Fractions
# from fractions import Fraction as F
# print(F(1.5))
# print(F(5))
# print(F(1,5))

# Python math module 
# import math
# print(math.pi)
# print(math.cos(10))
# print(math.log(10))
# print(math.log10(10))
# print(math.exp(10))
# print(math.factorial(5))
# print(math.sinh(10))
#print(abs(-12.34))


# Python random module
import random
# print('Random number -> ', random.randrange(5,15))
# print('Random number -> ', random.randrange(5,15))
# print('Random number -> ', random.randrange(5,15))
# print('Random number -> ', random.randrange(5,15))

day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
print(random.choice(day))

print(day)
random.shuffle(day)
print(day)

# Print random element
print(random.random())