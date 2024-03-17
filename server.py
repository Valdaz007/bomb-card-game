import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5555))
server.listen()

clients = []
ids = []

def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg)

def handle(client): #! Todo
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg, client)
        except:
            indx = clients.index(client)
            clients.remove(client)
            client.close()
            id = ids[indx]
            broadcast(f'Client <{id}> Disconnected!'.encode('ascii'), client)
            print(f'Client <{id}> Disconnected!')
            ids.remove(id)
            break

def main():

    print('Server Started ==> Waiting for connnection...')

    while True:
        client, addr = server.accept()
        print(f"Connected To Server: {str(addr)}")

        client.send("id".encode('ascii'))
        id = client.recv(1024).decode('ascii')
        ids.append(id)
        clients.append(client)

        print(f"Client <{id}>: Connected")
        broadcast(f"Client <{id}>: Connected".encode('ascii'), client)
        client.send('Connected Successfully'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

main()