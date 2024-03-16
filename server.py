import socket
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = {}

def broadcast(msg):
    for client in clients.values():
        client.send(msg)

def client_Msg(client): #! Todo
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            pass #! Todo

    print("Lost connection")
    msg.close()

def main():
    try:
        server.bind(("192.168.143.194", 5555))
    except socket.error as e:
        str(e)

    server.listen(5)
    print('Server Started ==> Waiting for connnection...')

    while True:
        client, addr = server.accept()
        print(f"Connected To Server: {str(addr)}")

        client.send('id'.encode('ascii'))
        id = client.recv(1024).decode('ascii')

        clients[id] = client