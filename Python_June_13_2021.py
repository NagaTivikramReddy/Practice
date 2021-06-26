# GIL (Global Interpreter lock)
#Python will execute code line by line using GIL Mechanism
import time
import threading
##
##def func1():
##    print("Func1")
##    print(time.ctime())
##
##def func2():
##    print("Func2")
##    print(time.ctime())
##
##func1()
##func2()
##
###---------
##
##def func1():
##    print("Func1")
##    print(time.ctime())
##    time.sleep(4)
##
##def func2():
##    print("Func2")
##    print(time.ctime())
##
##func1()
##func2()

#-------------------------

##def func1(name):
##    print("Func1")
##    print()
##    print(time.ctime())
##    time.sleep(4)
##
##def func2(name):
##    print("Func2")
##    print()
##    print(time.ctime())
##    
##t1 = threading.Thread(target = func1, args = ["Vikram"])
##t2 = threading.Thread(target = func2, args = ["Naga"])
##
##t1.start()
##t2.start()

#--------------------------------

##def Fun(name, delay):
##    counter = 0
##    while(counter<5):
##        counter+=1
##        print(name)
##        print(time.ctime())
##        time.sleep(delay)
##
##
##t1 = threading.Thread(target = Fun, args = ["Vikram",2])
##t2 = threading.Thread(target = Fun, args = ["Naga",4])
##
##t1.start()
##t2.start()


                    
