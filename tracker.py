import socket


class Tracker:
    def __init__(self):
        self.peers = {}

    def add_peer(self, id, ip):
        self.peers[id] = ip


tracker = Tracker()
