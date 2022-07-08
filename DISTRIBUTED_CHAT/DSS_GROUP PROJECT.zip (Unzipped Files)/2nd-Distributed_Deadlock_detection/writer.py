import os
import sys
from user import *
import socket
import subprocess
import pickle


with open("tpoint.txt", "w") as f:
        pass
ip = subprocess.check_output(["ifconfig", "wlo1"]).decode("utf-8").split("\n")[1].split()[1]
def receive():
    # make connection using socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # do this
    sock.bind((ip, int(3220)))
    sock.listen(1)
    # accept the connection
    conn, addr = sock.accept()
    # receive the message
    message = conn.recv(1024)
    message = pickle.loads(message)
    # write this message in tpoint.txt
    with open("tpoint.txt", "a") as f:
        for mess in message:
            f.write(f"{mess}\n")

    conn.close()

while True:
    receive()
