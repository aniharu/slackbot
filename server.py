# -*- coding:utf-8 -*-
import socket
import threading

host = "0.0.0.0"#yout ip address
port = 8000     #your fabortite port
BUFF = 1        # treated data is 0 or 1 which length is 1
listen_num = 5  #int, socket listen num
time_out = 10   #int, time to close

class ThreadedServer(object):
    #initialize
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.user = []

    def listen(self):
        self.sock.listen(listen_num)
        while True:
            client, address = self.sock.accept()
            client.settimeout(10)
            #make thread to adapt the multi threading process
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = BUFF
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data

                    #make user data (hashmap)
                    try:
                        self.user[address[0]] = data
                    except TypeError:
                        self.user = {address[0]:data}
                    except KeyError:
                        self.user.update({address[0]:data})

                    #count user's presence
                    num = 0
                    for x in self.user.values():
                        if x == "1".encode('utf-8'):
                            num += 1
                    print(self.user)
                    print(num)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False



if __name__ == "__main__":
    ThreadedServer(host, port).listen()
