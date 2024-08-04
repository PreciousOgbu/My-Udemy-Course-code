# try:
#     """
#     The code which can give rise to an exception is wriiten here.
#     """

#     a = "Hi"
#     b = int(a)
#     print("I am here....")
#     print(f'b = {b}')
# except:
#     print("Exception caught!")

# # CATCHING SPECIFIC EXCEPTIONS 
# try:
#     a = 5
#     b = 0
#     c = a/b
# except ZeroDivisionError:
#     print("Division by zero is not possible")


# # EXCEPTIONS CAN BE RAISED ALSO

# try:
#     raise TypeError
# except TypeError:
#     print("TypeError Exception caught")

# #  TRY...FINALLY
# try:
#     print("In try block")
#     #raise TypeError
# except:
#     print("In except block")
# finally:
#     print("In the finally block")


# USER DEFINED EXCEPTIONS

class VotersEligbility(Exception):
    def __init__(self):
        super()
try:
    age = 12 
    print("Age is " +str(age))
    if age < 18:
        raise VotersEligbility
except VotersEligbility:
    print("Age is less than 18")

else:
    print("Age is greater than or equal to 18")

finally:
    print("End of the program")

