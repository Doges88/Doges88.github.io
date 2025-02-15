import socket as s
import sys


IP = open("ip.txt", 'r').read()

while True:
    client = s.socket(s.AF_INET, s.SOCK_STREAM)
    client.connect((IP, 8888))
    command = input("Command: ")
    client.send(command.encode())
    if command == "EXIT":
        sys.exit("Quitting")
    else:
        result = client.recv(3000).decode()
        print(result)
    client.close()