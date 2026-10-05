import socket

HOST = "127.0.0.1"
PORT = 5000

print("1. View shared file")
print("2. Edit shared file")

choice = input("Enter choice: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

if choice == "1":
    client.sendall(b"GET_FILE")

    data = client.recv(4096)

    print("\nShared file:")
    print(data.decode())

elif choice == "2":
    print("Enter new content for the shared file:")
    content = input()

    message = "EDIT_FILE\n" + content
    client.sendall(message.encode())

    response = client.recv(1024)

    print("Server:", response.decode())

else:
    print("Invalid choice")

client.close()
