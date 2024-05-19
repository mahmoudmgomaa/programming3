# server_ side

From socket import *
 s = socket(AF_INET,SOCK_STREAM)
 print ("Socket successfully created")

 host ='127.0.0.1'
 port = 40674


 s.bind((host, port))
 print ("socket binded to ",port)
 s.listen(5)
 print ("socket is listening")

 while True:
 c, addr = s.accept()
 print ('Get connection from', addr )
Get connection from (‘127.0.0.1‘, 55182)
 c.send(b'Thank you for connecting')
 c.close()
 #############################################################
 # client_side
from socket import *
 s = socket(AF_INET,SOCK_STREAM)
 host ='127.0.0.1'
 port = 40674
 s.connect((host, port))
 print(s.recv(1024))
 s.close()
 ###########################################################
 # chat programme (server side)
from socket import *
try:
s=socket(AF_INET, SOCK_STREAM)
host="127.0.0.1"
port=7002
s.bind((host,port))
s.listen(5)
client, addr=s.accept()
print("connection from", addr[0])
while True:
x=client.recv(2048)
print("client : ",x.decode('utf-8'))
y=input(" server : ")
client.send(y.encode('utf-8'))
s.close()
except error as e:
print(e)
except KeyboardInterrupt :
print("chat is terminated")
##########################################
# chat programme (client side)
from socket import *
try:
s=socket(AF_INET, SOCK_STREAM)
host="127.0.0.1"
port=7002
s.connect((host,port))
while True:
y=input("client : ")
s.send(y.encode('utf-8'))
x=s.recv(2048)
print("server : ",x.decode('utf-8'))
s.close()
except error as e:
print(e)
except KeyboardInterrupt :
print("chat is terminated")


