import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.1.105"
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MASSAGE = "DISCONNECT"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode()
    send_length += b" " *(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Chamly")
#send("DISCONNECT")
