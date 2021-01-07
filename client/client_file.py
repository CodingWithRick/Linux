import socket
s = socket.socket()
host = input(str("Enter the host address: "))
port = 8080
s.connect((host, port))
print('Connection Established');
filename = input(str("Please enter the incoming filename: "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been successfully received")
