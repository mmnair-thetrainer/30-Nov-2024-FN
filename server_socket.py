import socket

sock = socket.socket()
host = socket.gethostname()
port = 11011
sock.bind((host, port))
sock.listen(5)
while True:
    con, address = sock.accept()
    print("Incoming connection from: ", address)
    print(con)
    con.send("Connected successfully".encode())
    con.close()