# -*- coding:utf-8 -*-
import socket
import threading

host = "your ip address" 
port = 8000
BUFF = 1024
port_num = 2

class ThreadedServer(object):
    def __init__(self, host = "192.168.1.3", port = 8000):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = BUFF
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    print(data)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

server = ThreadedServer()

if __name__ == "__main__":
    server.listen()
