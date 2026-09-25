import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

FILE_PATH = "shared/shared.txt"


def handle_client(conn, addr):
    print("Client connected:", addr)

    request = conn.recv(1024).decode()

    if request == "GET_FILE":
        with open(FILE_PATH, "r") as file:
            content = file.read()

        conn.sendall(content.encode())

    conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen()

print("Server started...")
print("Waiting for clients...")

while True:
    conn, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )

    thread.start()