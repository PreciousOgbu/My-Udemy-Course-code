# Declaring and assigning  value to Constants
# PI = 3.14
# GRAVITY = 9.8

# Declaring and assigning  value to a variable
# a = 'Apple'
# print(a)

# Changing value of a variable
# a = 'Aeroplane'
# print(a)

# a = 100
# print (a)

# Assigning multiple values to a variable

# b, c, d = 1, 2.5, 'Hello'
# print(b, c, d)


# Assigning same value to multiple variables
# b = c = d = 5
# print(b, c, d)

# class MyComplexNumber:
#     #Constructor methods 
#     def __init__(self,real = 0, imag = 0): 
#        print('MyComplexNumber constructor executing...')
#        self.real_part = real
#        self.imag_part = imag
          
#     def displayComplex(self):
#         print('{0} + {1}j'.format(self.real_part,self.imag_part))

# Create a new object against MyComplexNumber class
# cmplx1 = MyComplexNumber(40, 50)

#Calling displayComplex() function
# Output: 40 + 50j

#cmplx1.displayComplex()

# Create another object against MyComplexNumber class
# and create a new attribute 'new attribute'
# cmplx2 = MyComplexNumber (60, 70)
# cmplx2.new_attribute = 80
# cmplx2.displayComplex()

#Output: (60, 70, 80)

#print(cmplx2.real_part, cmplx2.imag_part, cmplx2.new_attribute)

# but cmplx object doesn't have attribute 'new_attribute'
# AttitudeError: 'MyComplexNumber' object has no attribute 'new attribute'
#cmplx1.new_attribute

# Deleting object attributes and the object
# print(cmplx1)
# del cmplx1.real_part
# del cmplx1


# ARRAYS
# Defining and Declaring an array

arr = [ 10, 20, 30, 40, 50]
print(arr)

# Acessing Array elements

print(arr[0])
print(arr[1])
print(arr[3])
print(arr[-2])  #Negative Indexing
print(arr[-1])    #Negative Indexing

brands = [ "Coke", 'Apple', 'Google',  'Microsoft', 'Toyota']
print(brands)

# Finding the length of the array
num_brands = len(brands)
print(num_brands)

# Adding an element to an array usin append()
brands.append('Intel')
print(brands)

# Removing elements from an array
colors = [ 'violet', 'indigo', 'blue', 'green', 'yellow','orange', 'red']
del colors[4]
colors.remove('blue')
colors.pop(3)
print(colors)


#Modifying the element of a string using indexing
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
fruits[1]= "Pineapple"
fruits[-1]= "Guava"
print(fruits)

# Concatenating two arrays usint the + opeartor
concat = [1, 2, 3]
concat = concat + [4, 5, 6]
print(concat)

# Repeating element in an array
repeat = ["a"]
repeat = repeat * 5
print(repeat)

# Slicing an array
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)
print(fruits[1:4])
print(fruits[:3])
print(fruits[-4:])
print(fruits[-3:-1])

# Declaring and defining multidimensional array
multd = [1,2], [3,4], [5,6], [7,8]
print(multd) 
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])