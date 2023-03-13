import socket
c=socket.socket()

c.connect(('172.19.99.50',54))

while True:
    clientMessage=input('Client: ')
    c.sendall(clientMessage.encode())
    
    if clientMessage=='Bye':
        break
    
    serverResponse=c.recv(1024).decode()
    print('Server: '+serverResponse)
    
    if serverResponse=='Bye':
        break
c.close()
