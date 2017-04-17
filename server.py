# -*- coding:utf-8 -*-
import socket
import threading
import time

host = "0.0.0.0"#yout ip address
port = 8000     #your fabortite port
BUFF = 1        # treated data is 0 or 1 which length is 1
listen_num = 5  #int, socket listen num
time_out = 10   #int, time to close
search_time = 60 * 12#10分だと、接続待ちしたとき、不安定かなと

class ThreadedServer(object):
    #initialize
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.user = []

    def check(self, cur_time):
        for x in self.user.keys():
            if self.user[x][1] < (cur_time - search_time):
                self.user[x] = ("0".encode('utf-8'), cur_time)
                print(self.user)


    def listen(self):
        self.sock.listen(listen_num)
        while True:
            client, address = self.sock.accept()
            client.settimeout(10)
            #make thread to adapt the multi threading process
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = BUFF
        old_time = time.time()
        while True:
            #ちょっと重い処理かも？
            #for checking shutdown error
            #check updates every search_time
            cur_time = time.time()
            if old_time < (cur_time - search_time):
                self.check(cur_time)

            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data

                    #make user data (hashmap)
                    try:
                        self.user[address[0]] = (data, time.time())
                    except TypeError:
                        self.user = {address[0]:(data, time.time())}
                    except KeyError:
                        self.user.update({address[0]:(data, time.time())})

                    #count user's presence
                    num = 0
                    for x in self.user.values():
                        if x[0] == "1".encode('utf-8'):
                            num += 1
                    print(self.user)
                    print(num)
            except:
                client.close()
                return False



if __name__ == "__main__":
    ThreadedServer(host, port).listen()
