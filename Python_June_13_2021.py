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

#-----------------------------


import socket

##def Socket_Programming():
##    
##    host = socket.gethostname()
##    port = 5000
##    server_socket = socket.socket()
##    print("Waiting for client to be Connected.................")
##    server_socket.bind((host,port))
##    server_socket.listen(2)
##    conn, address = server_socket.accept() #accept new connetion
##    print("Connection from : " + str(address))
##    while True:
##        data = conn.recv(1024).decode()
##        if not data:
##            break
##        print("from connected user: " + str(data))
##        data_to_client = input("Reply back to the Client")
##        conn.send(data_to_client.encode()) #send data to the client
##
##    conn.close() # Close the connection
##
##if __name__ == "__main__":
##    
##    Socket_Programming()


host = socket.gethostname()
print(host)




























                    
