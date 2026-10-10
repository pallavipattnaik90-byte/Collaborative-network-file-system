import socket
import json
import struct

HOST = "127.0.0.1"
PORT = 5000


def send_message(sock, message):
    data = json.dumps(message).encode()
    sock.sendall(struct.pack("!I", len(data)) + data)


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

last_viewed_version = None

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

            if response.get("status") == "OK":
                print("\nShared file:")
                print(response.get("content", ""))

                last_viewed_version = response.get("version")
                print("File version:", last_viewed_version)
            else:
                print("Error:", response.get("message"))

        elif choice == "2":
            if last_viewed_version is None:
                print("Please view the shared file before editing.")
                continue

            content = input("Enter new content: ")

            send_message(client, {
                "command": "EDIT_FILE",
                "client_name": client_name,
                "content": content,
                "expected_version": last_viewed_version
            })

            response = receive_message(client)

            if response.get("status") == "OK":
                last_viewed_version = response.get("version")
                print("Server:", response.get("message"))
                print("File version:", last_viewed_version)

            elif response.get("status") == "CONFLICT":
                print("\nCONFLICT DETECTED!")
                print(response.get("message"))
                print("Latest version:", response.get("version"))
                print("Choose option 1 to view the latest file before editing again.")

            else:
                print("Error:", response.get("message"))

        elif choice == "3":
            break

        else:
            print("Invalid choice.")

except (ConnectionError, OSError, ValueError, json.JSONDecodeError) as error:
    print("Error:", error)

finally:
    client.close()
    print("Disconnected from server.")
