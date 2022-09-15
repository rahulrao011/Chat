import socket
import threading

SERVER_IP_ADDR = socket.gethostbyname(socket.gethostname())
#SERVER_IP_ADDR = socket.gethostbyname('localhost')
PORT = 9090
DISCONNECT_MSG = '<DISCONNECT>'
MSG_LEN = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP_ADDR, PORT))

def listen_for_msg():
    while True:
        msg_recved = client.recv(MSG_LEN).decode()
        if len(msg_recved):
            print(f'Message received: {msg_recved}')

thread = threading.Thread(target=listen_for_msg)
thread.start()

connected = True
while connected:
    msg_to_send = input('')
    client.send(msg_to_send.encode())