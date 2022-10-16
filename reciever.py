import socket 
import os
import time

PORT = 5050
senderIP = input('Enter server IP: ')
# senderIP = '192.168.1.116'
ADDR = (senderIP, PORT)
reciever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    reciever_socket.connect(ADDR)
    print(f'[CONNECTED] Connected to sender {ADDR}')
except:
    print('[FAIL] Unable to Connect')
    exit(0)

file_name = reciever_socket.recv(100).decode()
# file_size = int.from_bytes(reciever_socket.recv(100), "little")
# file_size = int.from_bytes(file_size,"little")
# print(file_size)

with open('./rec/'+str(file_name), 'wb') as f:
    # c=0
    # while c <= int(file_size):
    #     dat = reciever_socket.recv(1024)
    #     if not dat:
    #         break
    #     f.write(dat)
    #     c += len(dat)
    d = reciever_socket.recv(1024)
    while d:   
        f.write(d)
        d = reciever_socket.recv(1024)

print('[RECIEVED] file recieved')

time.sleep(5)


reciever_socket.close()