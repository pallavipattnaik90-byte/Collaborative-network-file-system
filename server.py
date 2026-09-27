import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

FILE_PATH = "shared/shared.txt"

def handle_client(conn, addr):
    print("Client connected:", addr)

    data = conn.recv(4096).decode()

    if data.startswith("EDIT_FILE\n"):
        content = data.split("\n", 1)[1]

        with open(FILE_PATH, "w") as file:
            file.write(content)

        conn.sendall(b"File updated successfully.")

    elif data == "GET_FILE":
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
