import socket

HEADER = 64
PORT = 5050
format = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
address = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

def send(message):
    message = message.enconde(format)
    message_length = len(message)
    send_length = str(message_length).encode(format)
    send_length += b'' * len(send_length)
    client.send(send_length)
    client.send(message)

send("hello everyone!")
input()
send(DISCONNECT_MESSAGE)