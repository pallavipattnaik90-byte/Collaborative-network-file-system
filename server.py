import socket
import threading
import json
import struct

HOST = "127.0.0.1"
PORT = 5000

FILE_PATH = "shared/shared.txt"
file_lock = threading.Lock()


def receive_message(conn):
    header = b""

    while len(header) < 4:
        chunk = conn.recv(4 - len(header))
        if not chunk:
            return None
        header += chunk

    length = struct.unpack("!I", header)[0]
    data = b""

    while len(data) < length:
        chunk = conn.recv(length - len(data))
        if not chunk:
            return None
        data += chunk

    return json.loads(data.decode())


def send_message(conn, message):
    data = json.dumps(message).encode()
    header = struct.pack("!I", len(data))
    conn.sendall(header + data)


def handle_client(conn, addr):
    print("Client connected:", addr)

    try:
        while True:
            request = receive_message(conn)

            if request is None:
                break

            command = request.get("command")
            client_name = request.get("client_name", "Unknown")

            print("Client:", client_name)

            if command == "GET_FILE":
                with file_lock:
                    with open(FILE_PATH, "r") as file:
                        content = file.read()

                send_message(conn, {"status": "OK", "content": content})

            elif command == "EDIT_FILE":
                content = request.get("content", "")

                with file_lock:
                    with open(FILE_PATH, "w") as file:
                        file.write(content)

                print(client_name, "updated the shared file.")
                send_message(conn, {
                    "status": "OK",
                    "message": "File updated successfully."
                })

            else:
                send_message(conn, {
                    "status": "ERROR",
                    "message": "Unknown command."
                })

    except (ConnectionError, OSError, ValueError, json.JSONDecodeError) as error:
        print("Connection error:", error)

    finally:
        conn.close()
        print("Client disconnected:", addr)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Server started...")
print("Waiting for clients...")

while True:
    conn, addr = server.accept()
    threading.Thread(
        target=handle_client,
        args=(conn, addr),
        daemon=True
    ).start()
