# -*- coding:utf-8 -*-
import ctypes
import time
import socket
import errno
import subprocess

host = "your ip address"
port = 8000
#BUFF  = 1024

# define pointer class
class _pointer(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_long),
        ('y', ctypes.c_long),
    ]

class client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.error = dict({ "ERROR_10053":"exc.errno == errno.WSAECONNABORTED",
                            "ERROR_10054":"exc.errno == errno.WSAECONNRESET",
                            "ERROR_10056":"exc.errno == errno.WSAEISCONN",
                            "ERROR_10057":"exc.errno == errno.WSAENOTCONN" })
        self.try_connection()

    def try_connection(self):
        while(1):
            try:
                self.client.connect((self.host, self.port))
                break
            except socket.error as exc:
                print("Caught exception socket.error : %s" % exc)
                #for reconnection error not to continue connecting
                if self.error["ERROR_10056"] or self.error["ERROR_10057"]:
                    break
                continue

    def observe(self):
        # initialize pointer
        before_point = _pointer()
        after_point = _pointer()

        weight = -1
        state_on = 0
        time_weight = [15, 60, 180, 120, 180]#待ち時間

        while (1):
            before_point.x = after_point.x
            before_point.y = after_point.y
            ctypes.windll.user32.GetCursorPos(ctypes.byref(after_point))

            if before_point.x == after_point.x and before_point.y == after_point.y:
                weight = weight - 1 if weight >= 0 and state_on else 0
            elif weight != 3:
                weight += 1
                if weight == 1 and state_on != 1:
                    state_on = 1
                    try:
                        self.client.send(str(state_on).encode("utf-8"))
                    except socket.error as exc:
                        print("Caught exception socket.error : %s" % exc)
                        if self.error["ERROR_10053"] or self.error["ERROR_10054"]:
                            break

            if weight == -1:
                state_on = 0
                try:
                    self.client.send(str(state_on).encode("utf-8"))
                except socket.error as exc:
                    print("Caught exception socket.error : %s" % exc)
                    if self.error["ERROR_10053"] or self.error["ERROR_10054"]:
                        break

            time.sleep(time_weight[weight + 1])

    def repeat(self):
        # remedy to error
        #本来はエラー対策だけでなく、サーバーが落ちた時の再アクセス用にループさせたかったのだが無理そう
        #(サーバーが落ちてもsocketが残るため、プログラムを落とさないと、通信しなおせない)
        #socketのclose, shutdown, timeoutなどは効果なしだった。
        #クライアントの再起動をせずに済む案あれば。。。
        while(1):
            self.observe()

if __name__ == "__main__":
    client(host, port).repeat()
