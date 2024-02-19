import socket
import threading

class Peer:
    def __init__(self):
        self.id = None

    def join_network(self, server_addr):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def disconnect(self):
        pass

    def send_request(self, data):
        pass

    def send_response(self, data):
        pass


if __name__ == '__main__':
    with open("ipconfig.txt", "r") as f:
        addr = f.read()

    peer = Peer()
    peer.join_network(addr)

