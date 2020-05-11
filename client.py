import sys
import argparse
import socket
import config_funcs
import configparser

parser = argparse.ArgumentParser(description='Client to send and receive files')
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('-r', action='store_true', help="receive file")
group.add_argument('-s',  action='store_true', help="send file")

args, _ = parser.parse_known_args()

def receive():
    pass

def send():
    pass

s = socket.socket()
host = "localhost"
port = 8000

config = configparser.ConfigParser()
config.read('config.ini')

# First time client
if not config.sections():
    config['NAME'] = input("What's your name?\n")
    # write config details to file
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

NAME = config['NAME']

s.connect((host, port))
s.send(config_funcs.send_server_msg(f"{NAME} has connected"))

if args.r:
    receive()

if args.s:
    send()


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