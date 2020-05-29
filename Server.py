import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "192.168.1.105"
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MASSAGE = "DISCONNECT"
#SERVER = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_clinet(conn,addr):
    print("[NEW CONNECTION] {addr} connected")

    conneced = True
    while conneced:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MASSAGE:
                conneced  = False
            print(f"[{addr}] {msg}")
            conn.send("Massage Receive".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading .Thread(target=handle_clinet,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print(f"[STARTING] server is starting")

start()
