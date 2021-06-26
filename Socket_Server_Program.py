import socket

def Socket_Programming():

    host = socket.gethostname() # 4.4.4.4
    port = 5000
    server_socket = socket.socket()
    print("Waiting for Client to be Connected..................")
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data_to_client = input("Reply back to the Client")
        conn.send(data_to_client.encode())  # send data to the client

    conn.close()  # close the connection

if __name__ == "__main__":

    Socket_Programming()

