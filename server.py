import socket
from _thread import *
import sys

server = "192.168.143.194"
port = 5555

serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serve.bind((server, port))
except socket.error as e:
    str(e)

serve.listen(2)
print('Waiting for connnection... Server Started')

def client_Thread(conn):
    conn.send(str.encode("Connected..."))
    reply = ""
    while True:
        try:
            data = conn.recv(1024)
            reply = data.decode("utf-8")

            if not data:
                print("Diconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Send: ", reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost connection")
    conn.close()

while True:
    conn, addr = serve.accept()
    print('Connected to:', addr)

    start_new_thread(client_Thread, (conn,))