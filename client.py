import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect()

flg=0

while not flg:
    client.send(input("Message:").encode('utf-8'))
    msg=client.recv(1024).decode('utf-8')
    if msg=='quit':
        flg=True
    else:
        print(msg)
