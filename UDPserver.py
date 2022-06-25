import socket

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destination = ('192.168.57.1', 8888)
udpSocket.bind(destination)

while True:
    receive = udpSocket.recvfrom(1024)
    data = receive[0].decode('utf-8')
    address = str(receive[1])
    print(data, ' from ', address)
    if data == 'quit':
        break

print('program finished')

udpSocket.close()