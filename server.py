import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server started...")
print("Waiting for a client...")

conn, addr = server.accept()

print("Client connected:", addr)

conn.sendall(b"Connected to Collaborative File Server")

conn.close()
server.close()
