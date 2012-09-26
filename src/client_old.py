'''
Created on 17/09/2012

@author: Mutten
'''
#!/usr/bin/python           # This is client.py file
 
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
 
print 'Connecting to ', host, port
s.connect((host, port))

while True:
    msg = 'CLIENT >> '
    s.sendall(msg)
    print "--",
    #msg = s.recv(1024)
    print 'SERVER >> ', msg
#s.close 