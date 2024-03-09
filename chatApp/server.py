import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
address = (SERVER,PORT )
format = 'uft-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

def client(conn, address):
    print(f"[NEW CONNECTION] {address} connected.")

    connected = True
    while connected:
        message_length = conn.recv(HEADER).decode(format)
        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decod(format)
            if message == DISCONNECT_MESSAGE:
                connected = False
        
            print(f"[{address}] + {message}")
            conn.send("message received".encode(format))

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, address = server.accept()
        thread = threading.Thread(target=client, args=(conn,address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")




print("[STARTING] server is starting...")
start()