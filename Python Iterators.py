# # Defining a list

# our_list = [44, 77, 11, 33]

# # Get an iterator using iter() method 
# our_iter = iter(our_list)

# ## iterate through it using the next() method


# #   prints 44
# print(next(our_iter)) 

# #   prints 77
# print(next(our_iter)) 

# #   prints 11
# #print(next(our_iter)) 

# #   prints 33
# #print(next(our_iter)) 

# ## next(bj) is same as calling obj. __next__() method

# #   prints 11
# print(our_iter.__next__()) 

# #   prints 33
# print(our_iter.__next__()) 



# CREATING A CUSTOM ITERATOR 

# class Pow_of_Two:
#     ''' Class to implement an iterator 
#     of powers of two '''
#     def __init__(self, max = 0):
#         self.max = max
        
#     def __iter__(self):
#         self.n = 0
#         return self
    
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
        
# print(Pow_of_Two.__doc__)
# a = Pow_of_Two(4)
# i = iter(a)
# print(i.__next__())
# print(next(i))
# print(next(i))
# print(next(i))


# CREATING A INFINITE CUSTOM ITERATOR 
class infinite_iter:
    """ infinite iterator to return all
    odd numbers"""

    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        num = self.num
        self.num += 2
        return num 
    
i =infinite_iter()
a = iter(i)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

