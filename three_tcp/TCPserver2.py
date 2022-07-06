import socket

tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destinationRe = ('192.168.99.122', 8888)
destinationSe1 = ('192.168.0.12', 8888)
destinationSe2 = ('10.10.0.3', 8888)
tcpServerSocket.bind(destinationRe)
tcpServerSocket.listen(8)
tcpSocket1.connect(destinationSe1)
tcpSocket2.connect(destinationSe2)

while True:
    clinetSocket, clinetAddr = tcpServerSocket.accept()
    print('connected with ', clinetAddr)

    while True:
        receive = clinetSocket.recvfrom(1024)
        data = receive[0].decode('utf-8')
        print(data)
        tcpSocket1.send(data.encode('utf-8'))
        tcpSocket2.send(data.encode('utf-8'))
        clinetSocket.send('received!'.encode('utf-8'))

        if data == 'quit':
            break

    clinetSocket.close()
    break

print('program finished')

tcpServerSocket.close()
