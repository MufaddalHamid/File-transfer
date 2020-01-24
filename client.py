import socket
s=socket.socket()
host=input(str("enter host address"))
port=8080
s.connect((host,port))
print("connected")
filename=input(str("pls enter file name for incoming file"))
file=open(filename,'wb')
fd=s.recv(1024)
file.write(fd)
file.close()
print("file recieved successfully")
