import socket

FORMAT = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = "192.168.100.39"
PORT = 5050
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
client.connect(ADDR)

def send(msg : str):
    message = msg.encode(FORMAT)
    client.send(message)

send("Hello World")
input()
send(DISCONNECT_MESSAGE)