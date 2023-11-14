import socket

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.listen()

client,addr=server.accept()

flg=False

while not flg:
    msg=client.recv(1024).decode('utf-8')
    if msg=='quit':
        flg=True
    else:
        print(msg)
        client.send(input("Message: ").encode('utf-8'))

client.close()
server.close()
