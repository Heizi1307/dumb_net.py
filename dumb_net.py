#! /usr/bin/python3
'''File Name: dumb_net.py
   Author: Longxin Li
   Purpose: This program will accept two arguments,
            one is host which is string, one is
            port which is integer.And will ask
            user to type in one line. This program
            will recv the message from the host and
            print it out until no more message recv from host.
   CS346'''
from socket import *
from sys import argv


def main(host, port):
    sock = socket()
    addr = (host, port)
    sock.connect(addr)
    msg = input() + "\r\n"
    sock.sendall(msg.encode())
    data = sock.recv(1024).decode()
    while data != '':
        print(data)
        data = sock.recv(1024).decode('latin-1')
    sock.close()


if __name__ == "__main__":
    host = str(argv[1])
    port = int(argv[2])
    main(host, port)
