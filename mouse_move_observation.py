# -*- coding:utf-8 -*-
import ctypes
import time
import socket
import errno

host = "your ip address"
port = 8000
#BUFF  = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def try_connection():
    while(True):
        try:
            client.connect((host, port))
            break
        except socket.error as exc:
            print("Caught exception socket.error : %s" % exc)
            #for reconnection error not to continue connecting
            if exc.errno == errno.WSAEISCONN:#10056
                break
            continue

#for reconnection error
#client needs to wait time until socket deletes
#and be created again ?
#it is not stable
#the concept of this method is remedy to restart a server

#上手くいかないところ
def reconnection(exc):
    if exc.errno == errno.WSAECONNABORTED:#10053
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif exc.errno == errno.WSAECONNRESET:#10054
        time.sleep(60)
    try_connection()
    weight = 0

# define pointer class
class _pointer(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_long),
        ('y', ctypes.c_long),
    ]

try_connection()

# initialize class
before_point = _pointer()
after_point = _pointer()

weight = -1
state_on = "0"
time_weight = [15, 15,15,15,15]#[15, 60, 180, 120, 180]

while (1):
    before_point.x = after_point.x
    before_point.y = after_point.y
    ctypes.windll.user32.GetCursorPos(ctypes.byref(after_point))

    if int(before_point.x) == int(after_point.x) and int(before_point.y) == int(after_point.y):
        weight = weight - 1 if weight >= 0 and state_on == "1" else 0
    elif weight != 3:
        weight += 1
        if weight == 1 and state_on != "1":
            state_on = "1"
            try:
                client.send(state_on.encode("utf-8"))
            except socket.error as exc:
                print("Caught exception socket.error : %s" % exc)
                reconnection(exc)
                continue

    if weight == -1:
        state_on = "0"
        try:
            client.send(state_on.encode("utf-8"))
        except socket.error as exc:
            print("Caught exception socket.error : %s" % exc)
            reconnection(exc)
            continue

    time.sleep(time_weight[weight + 1]/15)
