import socket
import threading
from client import Client

SERVER_IP_ADDR = socket.gethostbyname(socket.gethostname())
#SERVER_IP_ADDR = socket.gethostbyname('localhost')
PORT = 9090
DISCONNECT_MSG = '<DISCONNECT>'
MSG_LEN = 1024

clients = {}
max_client_id = 0
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP_ADDR, PORT))

def start():
    global max_client_id
    server.listen()
    print('[SERVER]: Server is listening...')
    while True:
        conn, addr = server.accept()
        clients[max_client_id] = Client(conn, addr)
        thread = threading.Thread(target=handle_client, args=(max_client_id,))
        thread.start()
        max_client_id += 1
        print(f'[SERVER]: # of active connections: {threading.active_count() - 1}')

def handle_client(client_id):
    client_x = clients[client_id]
    connected = True
    while connected:
        msg = client_x.recv()
        print(f'[SERVER]: client-{client_id}: {msg}')
        if msg == DISCONNECT_MSG:
            connected = False
            clients.pop(client_id)
        else:
            clients[(client_id + 1) % 2].send(msg)
    client_x.close()
    print('connection disconnected')
    print(f'# of active connections: {threading.active_count() - 2}')

start()