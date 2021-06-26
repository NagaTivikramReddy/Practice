import socket

def Client_Programming():

    host = socket.gethostname()#6.8.9.8
    port = 5000
    client_socket = socket.socket()# instantiate
    
    client_socket.connect((host, port))  # connect to the server
    message =input("enter your message:")  # take input
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input("Reply back to the Server: ")  # again take input

    client_socket.close()  



if __name__ == "__main__":

    Client_Programming()
