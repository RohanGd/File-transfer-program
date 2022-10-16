import os
import socket
from telnetlib import SE
import time
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "0.0.0.0"
SOCK_ADDR = (SERVER, PORT)
# "152.57.223.30"
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender_socket.bind(SOCK_ADDR)
print(f'[STARTING] Server Starting at {SOCK_ADDR}')

sender_socket.listen()
print('Waiting for Connection')

client, addr = sender_socket.accept()

file_path = "imgs.jpg"
file_size = os.path.getsize(file_path)
client.send(file_path.encode())
# client.send(bytes(file_size))

# print(file_size)
with open(file_path, 'rb') as f:
    c=0
    print('[SENDING] File is being sent...')
    while c<= file_size:
        dat = f.read(1024)
        if not dat:
            break
        client.sendall(dat)
        c += len(dat)

print('[SENT] File transfer is completed')


time.sleep(10)

sender_socket.close()



