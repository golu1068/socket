# Import socket module 
import socket                

msg='';
print('working')
while 1:
    port = 12345
    s = socket.socket()  
    s.connect(('127.0.0.1', port)) 
    msg = s.recv(1024)
    print (msg)
# close the connection 
    s.close()
    print('donr')
    if (msg == b'quit'):
        break