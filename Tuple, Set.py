# creating an empty tuple
# tuple1 = ()
# print(tuple1)

# # creating tuples with integer elements
# tuple2 = (1, 2, 3)
# print(tuple2)

# # tuple with mixed data types
# tuple3 = (101, 'Presh', 2000.00, 'HR Dept')
# print(tuple3)

# # creation of nested tuple
# tuple4 = ("points", [1, 4, 3,], (7, 8, 6))
# print(tuple4)

# # tuple can be created without parentheses
# # also called tuple packing
# tuple5 = 101, 'Presh', 2000.00, 'HR Dept'
# print(tuple5)

# # tuple unpacking is also possible
# empid, empname, empsal, empdept = tuple5
# print(empid)
# print(empname)
# print(empsal)
# print(empdept)

# print(type(tuple5))




#  SET
# creating sets
# my_set1 ={11, 33, 66, 55, 44, 22}
# print(my_set1)

# # set of mixed data types
# my_set2 = {101, "Agatha", (21, 2,1994)}
# print(my_set2)

# # duplicate values are not allowed
#my_set3 = {11, 22, 33, 33,44, 22}
#print(my_set3)

# # set cannot have mutable items
# # my_set4 = {1, 2,[3,4]}
# # print(my_set4)

# #we can make set from a list
# my_set5 = set([1, 2, 3, 2])
# print(my_set5)
# print (type(my_set5))


# # we can make a list from a set
# my_list1 = list({11, 22, 33, 44})
# print(my_list1)
# print(type(my_list1))

#operations on sets
# my_set1 = {11, 33, 44, 66, 55}
# print(my_set1)

# 'set'object does not support indexing
#my_set1[0]

# add an element
# my_set1.add(77)
# print (my_set1)

# # add multiple elements
# my_set1.update([88, 99, 22])
# print(my_set1)




# # add list and set
# my_set1.update([100, 102], {103, 104, 105})
# print(my_set1)


# remove and discard
# initalize my_set
# my_set1 = {11, 33, 44, 55, 66}
# print(my_set1)

#discard an element which is not present, no error
# my_set1.discard(4)
# print(my_set1)

# remove an element which is not present, error raised
#my_set1.remove(6)
#print(my_set1)

# discard an element 
# my_set1.discard(44)
# print(my_set1)
# my_set1.remove(55)
# print(my_set1)

# Using pop()
# Intialize my_set
# my_set1 = {11, 33, 44, 55, 66}
# print(my_set1)


# #pop an element
# print(my_set1.pop())

# #Pop another element
# print(my_set1.pop())
# print(my_set1)

# # Clear my set
# my_set1.clear()
# print(my_set1)


# SET OPERATIONS - Union 
# myset1 = {0, 1, 2, 3 ,4, 5}
# myset2 = {4, 5, 6, 7 , 8 , 9}
# print(myset1)
# print(myset2)

# #use | opeator for union 
# print(myset1 | myset2)
# print(myset2 | myset1)
# print(myset1 .union(myset2))
# print(myset2 .union(myset1))

# Set Operations - Intersection
# myset1 = {0, 1, 2, 3 ,4, 5}
# myset2 = {4, 5, 6, 7 , 8 , 9}
# print(myset1)
# print(myset2)

# # Use & operator for Intersection
# print(myset1 & myset2)
# print(myset2 & myset1)
# print(myset1.intersection(myset2))
# print(myset2 .intersection(myset1))

# # set operations - set difference 
# myset1 = {0, 1, 2, 3 ,4, 5}
# myset2 = {4, 5, 6, 7 , 8 , 9}
# print(myset1)
# print(myset2)

# # use - operator for set difference 
# print(myset1  - myset2)
# print(myset2 - myset1)
# print(myset1 .difference(myset2))
# print(myset2 .difference(myset1))

# # set operations - symmetric difference 
# myset1 = {0, 1, 2, 3 ,4, 5}
# myset2 = {4, 5, 6, 7 , 8 , 9}
# print(myset1)
# print(myset2)

# # use ^ operator for symmetric difference
# print(myset1  ^ myset2)
# print(myset2 ^ myset1)
# print(myset1 .symmetric_difference(myset2))
# print(myset2 .symmetric_difference(myset1))

# set membership
# myset1 = {0, 1, 2, 3, 4, 5}
# print(2 in myset1)
# print(6 in myset1)
# print(2 not in myset1)
# print(6 not in myset1)

# #  iterating through a set
# for letter in set("Welcome"):
#     print(letter)

# built in function with set
# myset1 = {0, 1, 2, 3, 4, 5}
# print(len(myset1))
# print(max(myset1))
# print(min(myset1))
# print(sorted(myset1))


# Python frozenset
# Initalize A and B
myset1 = frozenset([ 1, 2, 3, 4])
myset2 = frozenset([ 3, 4, 5, 6])
print(myset1)
print(myset2)
print(myset1.difference(myset2)) 
print(myset1.union(myset2))
print(myset1.intersection(myset2))
print(myset1.symmetric_difference(myset2))
#myset1.add(10)


