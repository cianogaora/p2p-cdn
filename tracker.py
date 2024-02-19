import socket


class Tracker:
    def __init__(self, subnet_name):
        self.peers = {}
        self.subnet_name = subnet_name

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 5555))
        s.listen()
        while True:
            conn, addr = s.accept()
            data = conn.recv(1024)
            conn.send('forwarding you to ')

    def add_peer(self, id, ip):
        self.peers[id] = ip


tracker = Tracker("rendezvous")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_addr = s.getsockname()[0]
s.close()

with open("ipconfig.txt", "w") as f:
    f.write(server_addr)
    f.close()


