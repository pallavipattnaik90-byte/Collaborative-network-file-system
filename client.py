import socket

HOST = "127.0.0.1"
PORT = 5000

client_name = input("Enter client name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:

    print("\n1. View shared file")
    print("2. Edit shared file")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        client.sendall(("GET_FILE\n" + client_name).encode())

        data = client.recv(4096)

        print("\nShared file:")
        print(data.decode())

    elif choice == "2":

        print("Enter new content:")
        content = input()

        message = "EDIT_FILE\n" + client_name + "\n" + content

        client.sendall(message.encode())

        response = client.recv(1024)

        print("Server:", response.decode())

    elif choice == "3":

        client.close()
        print("Disconnected from server.")
        break

    else:

        print("Invalid choice")
