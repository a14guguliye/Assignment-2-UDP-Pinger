import socket

#CONFIGURATION OF THE SERVERPORT 
serverPort=1234
#CONFIGURATION OF THE SERVERSOCKET 
serverSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#GENERATING THE ARTIFICIAL SERVER 
serverSocket.bind((socket.gethostname(),serverPort))

print("server is ready to receive")

#sending the server into listening mode 
while 1:
    #server is gettinbg the client info
    #plus we also get the address 
    msgandaddress=serverSocket.recvfrom(1024)
    #server is reading the text 
    a=(msgandaddress[0].decode())    
    
    #server is sending the response 
    filecomposition="response sent for "+str(a)
    #server is sending the composition to the client 
    serverSocket.sendto(filecomposition.encode(),msgandaddress[1])
   


    
    