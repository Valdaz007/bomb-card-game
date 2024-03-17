import socket
import threading
from datetime import datetime

id = datetime.now().strftime('%Y%m%d%H%M%S')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

def rx():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == "id":
                client.send(id.encode('ascii'))
            else:
                print(msg)
        except:
            print("An Error Occured!")
            client.close()
            break

def tx():
    while True:
        try:
            msg = f"{id}: {input(f'{id}: ')}"
            client.send(msg.encode('ascii'))
        except:
            print(f'Error: ', msg)



rx_thread = threading.Thread(target=rx)
tx_thread = threading.Thread(target=tx)
rx_thread.start()
tx_thread.start()