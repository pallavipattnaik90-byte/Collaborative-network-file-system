import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

FILE_PATH = "shared/shared.txt"

def handle_client(conn, addr):
    print("Client connected:", addr)

    data = conn.recv(4096).decode()
    parts = data.split("\n", 2)

    command = parts[0]
    client_name = parts[1]

    print("Client:", client_name)

    if command == "EDIT_FILE":
        content = parts[2]

        with open(FILE_PATH, "w") as file:
            file.write(content)

        print(client_name, "edited the shared file.")

        conn.sendall(b"File updated successfully.")

    elif command == "GET_FILE":
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
