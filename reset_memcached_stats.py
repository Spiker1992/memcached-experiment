import socket

# Connect to Memcached
HOST = 'localhost'
PORT = 11211

# Create a socket connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'stats reset\r\n')
    data = s.recv(4096)

# Decode the response
response = data.decode('utf-8')
print(response)
