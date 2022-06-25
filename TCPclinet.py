import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destination = ('192.168.57.1', 8888)
tcpSocket.connect(destination)

while True:
    sendData = input('send:')
    tcpSocket.send(sendData.encode('utf-8'))
    recvData = tcpSocket.recv(1024)
    print(recvData.decode('utf8'))
    if sendData == 'quit':
        break

print('program finished')

tcpSocket.close()