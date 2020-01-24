
from tkinter import filedialog
from tkinter import *
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
root.destroy()
import socket
s=socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(1)
print(host)
print("waiting...")
connection,addr= s.accept()
print(addr,"has connected to server")
f=open(root.filename,'rb')
fd=f.read(1024)
connection.send(fd)
print("data has been sent")

