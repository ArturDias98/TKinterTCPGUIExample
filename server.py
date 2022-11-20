import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
FORMAT = "utf-8"

def SetServerParams(ip: str, port: str):

    Port = 5050
    Ip = socket.gethostbyname(socket.gethostname())

    if len(ip) > 0:
        Ip = ip

    if port.isnumeric():
        Port = int(port)

    ADDR = (Ip, Port)
    server.bind(ADDR) 

    print("[STARTING] Server is starting...")

    thread = threading.Thread(target=start, args=(Ip, Port))
    thread.start()
    

def handle_client(conn : socket, addr : any):

    print(f"[NEW CONNECTION] {addr} connected.")

    DISCONNECT_MESSAGE = "!DISCONNECT"
    connected = True

    while connected:
        msg = conn.recv(1024).decode(FORMAT)

        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")

    conn.close()        

def start(ip : str, port : int):

    server.listen()

    print(f"[LISTENING] Server is listening on {ip}")

    while True :
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

