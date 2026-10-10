import socket
import json
import struct

HOST = "127.0.0.1"
PORT = 5000


def send_message(sock, message):
    data = json.dumps(message).encode()
    header = struct.pack("!I", len(data))
    sock.sendall(header + data)


def receive_message(sock):
    header = b""

    while len(header) < 4:
        chunk = sock.recv(4 - len(header))
        if not chunk:
            raise ConnectionError("Server disconnected")
        header += chunk

    length = struct.unpack("!I", header)[0]
    data = b""

    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if not chunk:
            raise ConnectionError("Server disconnected")
        data += chunk

    return json.loads(data.decode())


client_name = input("Enter client name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    print("Connected to server.")

    while True:
        print("\n1. View shared file")
        print("2. Edit shared file")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            send_message(client, {
                "command": "GET_FILE",
                "client_name": client_name
            })

            response = receive_message(client)

            print("\nShared file:")
            print(response.get("content", response.get("message", "")))

        elif choice == "2":
            print("Enter new content:")
            content = input()

            send_message(client, {
                "command": "EDIT_FILE",
                "client_name": client_name,
                "content": content
            })

            response = receive_message(client)
            print("Server:", response.get("message", ""))

        elif choice == "3":
            print("Disconnecting...")
            break

        else:
            print("Invalid choice.")

except (ConnectionError, OSError, json.JSONDecodeError) as error:
    print("Error:", error)

finally:
    client.close()
    print("Disconnected from server.")
