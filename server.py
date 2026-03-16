import socket
import os

#Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen()
print("Server is On...")

#File Path, File Name and File Size
file = input(r"File: ").strip('"')
fileName = os.path.basename(file)
fileSize = os.path.getsize(file)

if not os.path.exists(file):
    print("Error: File not found!")
    exit()

#Client Acceptance
conn, addr = server.accept()
print(f"{addr} is Connected!")

#Sending Files
with conn:
    conn.send(f"{fileName}|{fileSize}".encode("utf-8") + b'\n')
    with open(file, "rb") as f:
        conn.sendfile(f)

print(f"{f} file sent.")