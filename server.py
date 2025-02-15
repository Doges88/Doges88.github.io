# set up the server
import socket as s
import subprocess
import sys
import os

server = s.socket(s.AF_INET,s.SOCK_STREAM)

HOST = "0.0.0.0"
PORT = 8888
server.bind((HOST, PORT))
server.listen(1)

print(f"Listening on {PORT}")

while True:
    client, addr = server.accept()
    print(f"Someone connected!")
    command = client.recv(1024).decode()
    print(f"Running {command}")
    if command == "EXIT":
        sys.exit("Server closed by client")
    elif command.startswith("cd "):
        directory = command.removeprefix("cd ")
        os.chdir(directory)
    else:
        result = str(subprocess.run(command, shell=True, capture_output=True, check=False).stdout.decode())
    client.send(result.encode())
    client.close()