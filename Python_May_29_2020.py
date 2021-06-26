#CLASS

## Python is unstructured
## Java, c, c++, c# all are structured

##Class is structured

##unbouded -- without constructor
##class My_Class:
##
##    var = 10
##
##    def add(a,b):
##        sum = a+b
##        return sum
##
##    def mul(a,b):
##        mul = a*b
##        print(mul)
##
##    def ss(a,b):
##        print(a,b)
##
##addn = My_Class.add(19,33)
##print(addn)
##My_Class.mul(12,77)
##print(My_Class.var)

##My_Class.ss("aaa",123)

##my = My_Class
##addn = my.add(19,33)
##print(addn)
##my.mul(12,77)
##print(my.var)

# In This process, memory usage is high
# So we use below method

#--------------------

##class My_Class:
##
##    """
##    Author : Trivikram
##    Date : 29/05/2021
##    Reason : Used to add and multiply 2 numbers
##    """
##    
##    var = 10
##
##    def __init__(self, a, b):  #Constructoer #instantiatoer #initialize the instance data
##
##        self.a = a
##        self.b = b
##
##    def add(self):
##        sum = self.a+self.b
##        return sum
##
##    def mul(self):
##        mul = self.a*self.b
##        print(mul)
##
##    def ss(self):
##        print(self.a,self.b)
##
##
##my = My_Class(20,30) #(here we have 3 arguments self,20 and 30) #Constructor (Whenever we create a constructor, it will create a default memory which is hidden (represented as "self")
##
##addn = my.add()
##print(addn)
##my.mul()
##print(my.var)

#my is an instance of My_Class (Single memory for outside data or function calling)

##print(my.__doc__) # Used to print the document string of the clas

#----------------------------------------------------------------------------

#OOPS

##Overriding

##class My_Class:
##    
##    var = 10
##
##    def __init__(self, a, b):  #Constructoer #instantiatoer #initialize the instance data
##
##        self.a = a
##        self.b = b
##
##    def add(self):
##        sum = self.a+self.b
##        return sum
##
##    def mul(self):
##        mul = self.a*self.b
##        print(mul)
##
##    def add(self): #Overriding
##        print(self.a,self.b)
##
##m = My_Class(10,20)
##
##m.add()
#output : 10 20 but not 30 (10+20) because its overridden by second add function

#----------------------------------------------

###Overloading

##Python does not support Overloading

#----------------------------------------------

##access specifiers

##1.Public
##2.Private (ex: __ZZ)
##3.Protected (python doesn't support)

##2.Private (ex: __ZZ)
##
##class My_Class:
##    
##    var = 10
##
##    def __init__(self, a, b):  #Constructoer #instantiatoer #initialize the instance data
##
##        self.a = a
##        self.b = b
##
##    def add(self):
##        sum = self.a+self.b
##        return sum
##
##    
##
##    def __mul(self): #data hiding #encapsulatoion
##        mul = self.a*self.b
##        print(mul)
##
##    def add(self): #Overriding
##        print(self.a,self.b)
##
##m = My_Class(10,20)
##m.mul()

#output : AttributeError: 'My_Class' object has no attribute '

#------------------------------------------------------

##def aa(a,b,c):
##    print("3 arguments")
##
##def aa(a,b):
##    print("2 arguments")
##
###if multiple functions has same name
##
##
##aa(1,2)


class My_Class:
    
    var = 10

    def __init__(self, a, b):  #Constructoer #instantiatoer #initialize the instance data

        self.a = a
        self.b = b

    def add(self):
        sum = self.a+self.b
        return sum

    

    def __mul(self): #data hiding #encapsulatoion
        mul = self.a*self.b
        print(mul)

    def add(self): #Overriding
        print(self.a,self.b)

    def mul_add(self):
        mul(a,b)
        add(a,b)

m = My_Class(10,20)
m.mul_add()













