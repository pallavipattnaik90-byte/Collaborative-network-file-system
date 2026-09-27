import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Enter new content for the shared file:")
content = input()

client.sendall(b"EDIT_FILE")
client.sendall(content.encode())

response = client.recv(1024)

print("Server:", response.decode())

client.close()
