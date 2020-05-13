import socket   
import threading             
from tkinter import *
master = Tk()

clo = 0
def qui():
    global clo, msg, sen
    msg = 'quit'
    sen = 1
    clo = 1
    master.destroy()
msg=''; sen=0;
def go():
    global sen, msg
    sen = 1
    msg = e1.get()    

def data_send():
    global msg, sen
    while 1:
        if (msg != '' and sen == 1):
           c, addr = s.accept()
           if (c != 0):
               print ('Got connection from', addr) 
               msg_by = bytes(msg, 'utf-8')
               c.send(msg_by)
               sen = 0
        if (clo == 1):
            break
    
e1 = Entry(master)
e1.grid(row =0, column=0)
b1 = Button(master, text='send',command = go)
b1.grid(row = 0, column = 1)
b2 = Button(master, text='quit', command=qui)
b2.grid(row=1, column=0)

s = socket.socket()          
print ("Socket successfully created")
  
port = 12345              
  
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
s.listen(5)      
print ("socket is listening")  
loop_active = True

t2 = threading.Thread(target=data_send)

t2.start()


master.mainloop()     
