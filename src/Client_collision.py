'''
Created on 26/09/2012

@author: Mutten
'''
#!/usr/bin/python           
 
import socket               
#import time
#import random
#i=random.uniform                            # variable i = Random number or hole number
def main():                                  #def main(): is for SCANeR to run the script correctly (and multiple times)
    s = socket.socket()                      # Create Socket   
    host = socket.gethostname()              #"10.115.254.55"  # Host IP   
    port = 12345                             # Host Port   
 
    print 'CollisionClient is connecting to ', host, port  # Bind to the port
    s.connect((host, port))                  # Connect to Host IT and port
    print 'CollisionClient is connected' 

    #while True:                             # While Loop
    #    i=random.uniform (1,5)              # Random a number between 1 and 5 /  add 1 for every time 
    #    msg = '%d'%i                        # Message to Server  
    msg ="Collision"                         # Message is the name of the rule in SCANeR
    s.sendall(msg)                           # Send message to all
    #print 1+1
    msg = s.recv(1024)                       # Message Recv  
    print 'CollisionClient is receiving: ', msg    #Print to Screen msg is the total number of collisions received from the server
#    print 'Math doing OK', msg              # Print to Screen 
#    time.sleep(1)                           # Sleep timer in seconds 
#s.close ("exit")
    s.close()
    return 0                                 #end of def main():
                                