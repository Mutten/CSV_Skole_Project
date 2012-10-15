'''
Created on 15/10/2012

@author: Mutten

Dette program simulere SCANeR
'''

import Client_collision
import Client_OutOfRoad
import Client_Startup
import time

Client_Startup.main()
time.sleep(2)
Client_collision.main()
time.sleep(1)
Client_OutOfRoad.main()
time.sleep(1)
Client_OutOfRoad.main()
time.sleep(6)
Client_OutOfRoad.main()
time.sleep(5)
Client_OutOfRoad.main()
time.sleep(1)
Client_OutOfRoad.main()
time.sleep(1)