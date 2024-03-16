from bomb.client import *
from _thread import *

client = Client()

def recv():
    while True:
        msg = client.onRecv()
        if msg != False:
            print(msg)
        else:
            break

def send():
    while True:
        msg = f"{client.id}: {input('')}"
        client.send(msg)

if __name__ == "__main__":
    start_new_thread(recv)
    start_new_thread(send)