'''
Created on 09/10/2012

@author: Mutten
'''
#import numpy as np                  # Import of numpy
#import matplotlib.pyplot as plt     # Import Matplotlib
#import pylab                        # Import pylab      
import socket                       # Import socket module

oor = 0.0
coll = 0.0
#q = socket.socket()                 # Create a socket object for Quit
s = socket.socket()                 # Create a socket object for Start 
                
host = socket.gethostname()         # Get local machine name
port = 12345 
portq = 12346
print 'Server started!'
print 'Waiting for clients...'


s.bind((host, port))                    # Bind to the port
#q.bind((host, portq))                   # Bind to the port
#q.listen(5)
#h,addr2 = q.accept()
while oor < 5 and coll < 4 :            # While loop for Coll and oor 
    s.listen(5)                         # Now wait for client connection.
    c, addr = s.accept()                # Establish connection with client.
    print 'Got connection from', addr   # Print Connetion and address
    msg = c.recv(1024)                  # msg receve from client
    if msg == 'OutOfRoad'  : 
        oor = oor + 1
        print (oor), ' >> ', msg       # Print address and msg from Client
        #c, addr = s.accept()
        
    elif msg == 'Collision' :
        coll = coll + 1
        print (coll), ' >> ', msg       # Print address and msg from Client
        #c, addr = s.accept()
    
    if oor < 5 and coll < 4 :    
        c.send(msg);                    # Send msg to client
    else :
        c.send("Exit")
    c.close()
    print oor , "Udenfor "
    print coll , "Sammen" 
#h.send("exit");                     # send exit message to Client 
#h.close()                           # Close     Connection to client