import socket
from config import NAME

s = socket.socket()
host = "localhost"
port = 8000

# Check
if not NAME:


def send_server_msg(message):
    return str.encode(message)


s.connect((host, port))
s.send(send_server_msg("Hello server!"))

with open("received_file", 'wb') as f:
    print("file opened")
    while True:
        print("receiving data...")
        data = s.recv(1024)
        print(f"data={data}")
        if not data:
            break
        # write data to a file
        f.write(data)

print("Successfully get the file")
s.close()
print("connection closed")