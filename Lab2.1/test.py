import requests, json, pprint

import socket, os
from time import sleep

def client():
    print('\nNew client', os.getpid())
    sleep(3)
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 8089))
    for i in range(50):
        print("Client %d sending %d" % (os.getpid(), i))
        clientsocket.send(('Hello ' + str(i) + '\n').encode())
        sleep(5)
    os._exists(0)

def server():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 8089))
    serversocket.listen(1)

newpid = os.fork()



