'''
Created on 09/10/2012

@author: Mutten
'''
import numpy as np                  # Import of numpy
import matplotlib.pyplot as plt     # Import Matplotlib
import pylab                        # Import pylab      
import socket                        # Import socket module

x = 0.0
oor = 0.0                           # Out of Road
coll = 0.0                          # Collision
xListe = []                         # Empty array for x = Time
ycoll = []                          # Empty array for y = Collision
yoor =  []                          # empty array for y = Out of Road
#q = socket.socket()                # Create a socket object for Quit
s = socket.socket()                 # Create a socket object for Start 
                
host = socket.gethostname()         # Get local machine name
port = 12345 
#portq = 12346
print 'Server started!'
print 'Waiting for clients...'


s.bind((host, port))                    # Bind to the port
              
while oor < 5 and coll < 4 :            # While loop for Coll and oor for a < 
    s.listen(5)                         # Now wait for client connection.
    c, addr = s.accept()                # Establish connection with client.
    print 'Got connection from', addr   # Print Connetion and address
    msg = c.recv(1024)                  # msg receve from client
    if msg == 'OutOfRoad'  :            # if Massage = Out of Road go into if statement 
        oor = oor + 1                   # Count oor + 1 
        print (oor), ' >> ', msg        # Print address and msg from Client
        #c, addr = s.accept()
        
    elif msg == 'Collision' :           # els if msg = Collision go into Statement as above
        coll = coll + 1                 # Count Coll + 1 
        print (coll), ' >> ', msg       # Print address and msg from Client
        #c, addr = s.accept()
        
    elif msg == 'Start' :           # els if msg = Collision go into Statement as above
        print "NU start vi rigtig"
        #coll = coll + 1                 # Count Coll + 1 
        #print (coll), ' >> ', msg       # Print address and msg from Client
        #c, addr = s.accept()
        
    if oor < 5 and coll < 4 :           # If oor < 5 and coll < 4 
        c.send(msg);                    # Send msg to client
    else :                              # Else
        c.send("Exit")                  # send Exit to Client 
    c.close()                           # Close Connection
    print oor , "Udenfor "              # Print oor as "Udenfor" Togeather  
    print coll , "Sammen"               # Print coll as "Sammen" Together 
    x=x+1
    xListe.append(x)
    ycoll.append(coll)
    yoor.append(oor)



 
      
        
    
#    y.append(float(msg))            # y append to the list with a float (comma numbers) numbers from msg (Numbers from client) 

plt.plot(xListe,yoor,xListe,ycoll )                                  
#plt.plot(xListe, yoor)                      # plot the x and y 

pylab.show() 