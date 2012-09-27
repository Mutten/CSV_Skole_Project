'''
Created on 26/09/2012

@author: Mutten
'''
#!/usr/bin/python           
 
import socket               
import time
i=1                                 #variable i = 1
s = socket.socket()                 # Create Socket   
host = socket.gethostname()         # Host IP   
port = 12345                        #Host Port   
 
print 'Connecting to ', host, port  #Bind to the port
s.connect((host, port))             #Connect to Host IT and port 

while True:                         # While Loop
    i=1+i                           # add 1 for every time 
    msg = '%d'%i                    # Message 
    s.sendall(msg)                  # Send message to all
    #print 1+1
    msg = s.recv(1024)              # Message Recv  
    print 'Math doing OK', msg      # Print to Screen 
    time.sleep(1)                   # Sleep timer in seconds 
#s.close