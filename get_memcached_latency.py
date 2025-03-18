import socket

# Connect to Memcached
HOST = 'localhost'
PORT = 11211

# Create a socket connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'stats\r\n')
    data = s.recv(4096)

# Decode the response
response = data.decode('utf-8')

# Parse the response to get total requests and total time
lines = response.split('\n')
total_requests = 0
total_time = 0
# https://github.com/memcached/memcached/blob/master/doc/protocol.txt
for line in lines:
    if 'cmd_get' in line: # The number of get commands the cache has received.
        total_requests = int(line.split()[2])
    if 'rusage_user' in line: # Accumulated user time for this process
        total_time = float(line.split()[2])

# Calculate average latency
if total_requests > 0:
    average_latency = total_time / total_requests
    print(f'Average Latency: {average_latency} seconds')
else:
    print('No requests found')
