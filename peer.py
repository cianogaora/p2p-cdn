import socket

class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def connect(self):
        pass

    def disconnect(self):
        pass

    def send_request(self, data):
        pass

    def send_response(self, data):
        pass


if __name__ == '__main__':
    peer = Peer('')