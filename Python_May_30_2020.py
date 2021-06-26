#Inheritance

##class First:
##
##    def __init__(self,a,b):
##        self.a = a
##        self.b = b
##
##    def add(self):
##        print("Parent Sum: ",self.a+self.b)
##
##    def mul(self):
##        print("Parent Mul: ",self.a*self.b)
##
##
##class Second(First):
##
##    def div(self):
##        print('Div: ',self.a/self.b)
##
##    def add(self):
##        First.add(self)
##        #print("child Sum :",self.a+self.b)
##
##v = Second(100,25)
##v.div()
##v.mul()
##v.add()

#--------------------------------------

#Exception handling

##try:
##    var = 100/0
##    print('a' + 10)
##    
##except ZeroDivisionError:
##    print("Zero")
##
##except:
##    print("eror")
##
###one an error is raised the next lines of code will not run

#--------------------

##try:
##    var = 100/0
##    print('a' + 10)
##    
##except (ZeroDivisionError,TypeError) as ex:
##    print(ex)

##except:
##    print("eror")

# A try can have multiple except
# default except should be at last always

##def my_fun(name="Don",age):
##    print(name,age)
##
##my_fun(20)
##
### here we should not give argumets as above, always we need to give defualt agruments at last

#--------------------------

##try:
####    var = 100/2
##    print(10 + 10)
##    
##except (ZeroDivisionError,TypeError) as ex:
##    print(ex)
##
##except:
##    print("eror")
##
##else: #else will be executed when there there is no exception
##    print('else')
##
##finally:
##    print("finally")
##
##
##try :
##    var = "a" + 19
##except Exception as e:
##    print("error")
##    print(e)
##
##else:
##    print("No error")
##
##finally:
##    print("Thank You")

#-------------------------------------------------

#User Defined exceprion
#Using 'raise'
##try:
##    var = 0
##    xxx = 10/0
##    if var<1:
##        raise TypeError("User defined exception")
##except (TypeError,ZeroDivisionError) as e:
##    print(e)
##finally:
##    print("Thank You")
##
##print("Outside Try")

#output:
##division by zero
##Thank You
##Outside Try

# If the error is caught then only  the code ouside the try will get executed

##class LessThanOneError(Exception):
##    pass
##
##try:
##    var = 0
##    if var<1:
##        raise LessThanOneError("User defined exception")
##except (LessThanOneError,ZeroDivisionError) as e:
##    print(e)
##finally:
##    print("Thank You")

##try:
##    var = 0
##    xxx = 10/0
##    if var<1:
##        raise TypeError("User defined exception")
##    print("kjbbshshb") # This will not get executed
##except (TypeError,ZeroDivisionError) as e:
##    print(e)
##finally:
##    print("Thank You")
##
##print("Outside Try")

#-------


class LessThanOneError(Exception):
    v = "error fron user defined exception class"

try:
    var = 0
    if var<1:
        raise LessThanOneError()
except (LessThanOneError,ZeroDivisionError) as e:
    print(e.v)
finally:
    print("Thank You")

#------------------------------
##
##class A:
##    def fun():
##        print("A")
##
##class B(A):
##    def fun():
##        print("B")
##
##class C(A):
##    def fun():
##        print("C")
##
##class D(B,C):
##    pass

#MRO - Method resolution order




        
