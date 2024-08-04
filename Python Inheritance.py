# #  Creating class and object in Python
# class myBird:

#     def __init__(self):
#         print("myBird class is executing...")


#     def whatType(self):
#         print("I am a Bird...")

#     def canSwim(self):
#         print("I can Swim")



# # myPenguin class inheriting the attributes from myBird class

# class myPenguin(myBird):


#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("myPenguin class constructor is excecuting....")


#     def whoisThis(self):
#        print("I am Penguin...")


#     def canRun(self):
#         print("I can run faster.....")


# # Accessing the child class's attributes(Inheritance)
# pg1 = myPenguin()
# pg1.whatType()    #defined in my bird class
# pg1.whoisThis()    #defined in MyPenguin
# pg1.canSwim()        #  defined in myBird class
# pg1.canRun()      #ddefined in myPenguin class


# POLYMORPHISM

# class MyParrot:

#     def canFly(self):
#         print("Parrot can fly.....")

#     def canSwim(self):
#         print("Parrot cannot swim.....")

# class MyPenguin:
    


#     def canFly(self):
#         print("Penguin can't fly....")

#     def canSwim(self):
#         print("Penguin can swim....")



# # Common interface 
# def flying_bird_test(bird):
#     bird.canFly()
#     bird.canSwim()


# # Instantiate objects 
# bird_parrot = MyParrot()
# bird_penguin = MyPenguin()


# # Passing the object 
# flying_bird_test(bird_parrot)
# print()
# flying_bird_test(bird_penguin)



# PYTHON MULTIPLE INHERITANCE

class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass



# Multiple Inheritance 
class Base1:
    def funcBase1(self):
        print("funBase1() is executing...")

class Base2:
    def funcBase2(self):
        print("funBase2() is executing...")

    
class Base3:
    def funcBase3(self):
        print("funBase3() is executing...")


class MultiDerived(Base1, Base2, Base3):
    def funcMultiDerived(self):
        print("funcMultiDerived() is executing....")



md1 = MultiDerived()
md1.funcBase1()  
md1.funcBase2()
md1.funcBase3()
md1.funcMultiDerived()



