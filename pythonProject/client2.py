import socket

client = socket.socket()
hostname = socket.gethostname()
port = 12345
client.connect((hostname, port))

while True:
    message = input("Input a text: ")
    client.send(message.encode())
    data = client.recv(1024)
    print("Server sent: ", data.decode())

    if message == "exit":
        client.close()
        break