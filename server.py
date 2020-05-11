import socket


host = "localhost"
port = 8000

def send_server_msg(message):
    return str.encode(message)


s = socket.socket()
s.bind((host, port))
s.listen(5)

print("Server listening....")


while True:
    conn, addr = s.accept()
    print("Got connection from {addr}")
    data = conn.recv(1024)
    print("Server received", repr(data))

    filename = "test.png"
    with open(filename, 'rb') as f:
        l = f.read(1024)
        while l:
           conn.send(l)
           print("Sent ",repr(l))
           l = f.read(1024)

    print('Done sending')
    conn.send(send_server_msg("Thank you for connecting"))
    conn.close()