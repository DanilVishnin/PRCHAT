import socket
from _thread import *

def client_thread(con):
    while True:
        data = con.recv(1024) # получаем данные от клиента
        message = data.decode() # преобразуем байты в строку
        print(f"Client sent: {message}")
        message = message[::-1] # инвертируем строку
        con.send(message.encode()) # отправляем сообщение клиенту
        if message == "exit":
            con.close()  # закрываем подключение
            break

server = socket.socket() # создаем объект сокета сервера
hostname = socket.gethostname() # получаем имя хоста локальной машины
port = 12345 # устанавливаем порт сервера
server.bind((hostname, port)) # привязываем сокет сервера к хосту и порту
server.listen(5) # начинаем прослушиваение входящих подключений

print("Server running")

while True:
    client, _ = server.accept() # принимаем клиента
    start_new_thread(client_thread, (client,)) # запускаем поток клиента

