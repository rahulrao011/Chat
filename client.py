import socket

class Client:
    
    MSG_LEN = 1024

    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
    
    def send(self, msg):
        self.conn.send(msg.encode())
        print(f'Sent: {msg}')
    
    def recv(self):
        msg = self.conn.recv(Client.MSG_LEN).decode()
        print(f'Received: {msg}')
        return msg
    
    def close(self):
        self.conn.close()