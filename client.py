import socket

class Client:
    def __init__(self) -> None:
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server = "192.168.143.194"
        self._port = 5555
        self._addr = (self._server, self._port)
        self._id = self.connect()
        print(self._id)

    def connect(self):
        try:
            self._client.connect(self._addr)
            return self._client.recv(1024).decode()
        except:
            pass

    def send(self, data):
        try:
            self._client.send(str.encode(data))
            return self._client.recv(1024).decode()
        except socket.error as e:
            print(e)

client = Client()
print(client.send('Hello'))