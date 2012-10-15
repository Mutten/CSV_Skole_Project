'''
Created on 15/10/2012

@author: Mutten
'''
import socket               
                                            
def main():                                  # def main(): is for SCANeR to run the script correctly (and multiple times)
    s = socket.socket()                      # Create Socket   
    host = socket.gethostname()                   # Host IP   
    port = 12345                             # Host Port
    
    print 'Scenario startet ', host, port  # Bind to the port
    s.connect((host, port))                 # Connect to Host IT and port
    print 'Scenario start connected' 
    
    msg ="Start"                        # Message is the name of the rule in SCANeR
    s.sendall(msg)                          # Send message to all
    
    msg = s.recv(1024)                      # Message Recv  
    print 'Start op modtager : ', msg      # Print to Screen msg is the total number of collisions received from the server

    s.close ()
    
    return 0                                # end of def main():