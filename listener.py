import socket
import argparse

parser = argparse.ArgumentParser(prog="listener.py",
                                 description="Basic listener in python through socket")
parser.add_argument("-p", "--port", default=1234, type=int, required=False, help="listening port")
args = parser.parse_args()

SERVER_IP = "0.0.0.0" #all IPv4 addresses
SERVER_PORT = args.port
BUFFER_SIZE = 1024 #1kb, maximum amount of data to be received at once

s = socket.socket()
s.bind((SERVER_IP, SERVER_PORT))
s.listen(5)
print(f"Listening as {SERVER_IP}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

while True:
    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)

client_socket.close()
s.close()