import socket
s=socket.socket()

s.bind(('172.19.99.50',54))
s.listen(3)

print('waiting for connections')
while True:
    c,addr=s.accept()
    print('connect with',addr)
    
    while True:
        data=c.recv(1024).decode()
        print('Client: '+data)
        
        if data=='Bye':
            break
        response=input('Server: ')
        c.sendall(response.encode())
        
        if response=='Bye':
            break
    c.close()
