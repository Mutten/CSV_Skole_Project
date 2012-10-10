'''
Created on 26/09/2012

@author: Mutten
'''
#!/usr/bin/python                   # This is server.py file
import numpy as np                  # Import of numpy
import matplotlib.pyplot as plt     # Import Matplotlib
import pylab                        # Import pylab      
import socket                       # Import socket module

s = socket.socket()                 # Create a socket object
host = socket.gethostname()         # Get local machine name
port = 12345                        # Reserve a port for your service.

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))                # Bind to the port
s.listen(5)                         # Now wait for client connection.
c, addr = s.accept()                # Establish connection with client.
print 'Got connection from', addr   # Print Connetion and address

y=[]                                # y = a new ararry / list
x = np.arange(0, 5, 0.1)            # x = numpy in range from 0 to 5 with a jump of 0.1  - Come up with x and y
while len(y)<len(x) :               # While the lenth of y is less then lenth of x do whatever in the loop
    msg = c.recv(1024)              # msg receve from client
    print (addr), ' >> ', msg       # Print address and msg from Client
    #msg = 'Traceback OK '
    c.send(msg);                    # Send msg to client 
      
        
    #y = np.sin(x)
    y.append(float(msg))            # y append to the list with a float (comma numbers) numbers from msg (Numbers from client) 

                                    # Just print x and y for fun
    print x
    print y

                                    
plt.plot(x, y)                      # plot the x and y 

pylab.show()                        # Shows the curve


c.send("exit");                     # send exit message to Client 
c.close()                           # Close Connection to client