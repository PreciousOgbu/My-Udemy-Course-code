# # different ways to define a string in python 
# mystr1 = 'Welcome'
# print(mystr1)

# mystr2 = "Welcome"
# print(mystr2)

# mystr3 = '''Welcome'''
# print(mystr3)

# # triple quote string can extend multiple lines

# mystr3 = '''Welcome 
# to the world of 
# Pyython Programming''' 
# print(mystr3)


# Accessing characters in a string 
# mystr = 'Language'
# print('my string [0]=', mystr[0])
# print('my string [-1]=', mystr[-1])
# print('my string [1:]=', mystr[1:])
# print('my string [5:-2]=', mystr[5: -2])
#print('my string [10]=', mystr[10])


# Strings are immutable 
# But different strings can be assigned 
# mystr = 'Language'
# print(mystr)

# mystr = 'Programing'
# print(mystr)

#mystr[3] = 'x'

# Concatenation of strings 
# mystr1 = 'Welcome'
# mystr2 = ' to all'

# # using + 
# print('mystr1 + mystr2 =' , mystr1 + mystr2)

# # using *
# print('mystr1 *3 =', mystr1*3)

# iterating through a string 
# letter_count = 0
# for letters in 'Hello World':
#     if (letters =='l'):
#         letter_count += 1
# print(letter_count, 'times 1 letter has been found')

# string membership 
# print('l' in 'Hello')
# print('l' not in 'Hello')
# print('b' in 'Hello')
# print('b' not in 'Hello')

# built in function
#mystr = 'university'

# using enumerator ()
# my_list_enumerate = list(enumerate(mystr))
# print('list(enuerate(mystr)) ', my_list_enumerate)

# # using character count 
# print('len(mystr) = ', len(mystr))

# string formatting using escape sequence
#print("tell me "what's your name?")

#using triple quotes
print('''Tell me "What's your name?"''')

# escaping single quotes
print('tell me "What\'s your name?"')
# escaping double quotes 
print("tell me \"What's your name?\"")

