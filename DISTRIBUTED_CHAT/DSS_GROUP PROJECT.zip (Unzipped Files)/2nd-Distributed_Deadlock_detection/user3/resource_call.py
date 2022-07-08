import random
from C_U import *
import os
import sys
import socket
import subprocess
import pickle

n=6
num_res=random.randint(0,n//2)
res=[]
res=random.sample(range(1,n+1),num_res)
pes=[]
for i in range(len(res)):
    # only take in res[i] who is not user_cur
    if res[i]!=int(user_cur[4:]):
        pes.append(res[i])
res=pes
print("I need to send these resources:",res)
for i in range(len(res)):
    res[i]=f"{user_cur[4:]} {res[i]}"


# send to writer.py
ip = subprocess.check_output(["ifconfig", "wlo1"]).decode("utf-8").split("\n")[1].split()[1]

def send(message):
    # send the message until the receiver sends an ACK
    while True:
      #  print("Hel")
        # make connection using socket
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.connect((ip, int(3220)))
            # send the message
            sock.send(pickle.dumps(message))
            # receive the ACK
            ack = sock.recv(1024)
            sock.close()
            # if the ACK is received, break the loop
            break
        except:
            pass


# send res to writer.py
send(res)