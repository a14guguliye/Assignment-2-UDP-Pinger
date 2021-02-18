import socket 
from datetime import datetime
import time

#configuring the server port 
serverPort=1234
#configuring the socket to UDP 
clientsocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(0,200):
    #marking the starttime 
    starttime=datetime.now()
    
    #sending the message at the specific time 
    clientsocket.sendto(str(i).encode(),(socket.gethostname(),serverPort))
    print("ping has been sent at "+str(starttime))

    #receiving the message at the specific time 
    responseandaddress=clientsocket.recvfrom(1024)
    endttime=datetime.now()
    print("pong has been received at "+str(endttime))
    #calculating the difference 
    print(str(i)+"."+" RTT TIME:"+str((endttime-starttime).total_seconds()))
    print("\n\n")
