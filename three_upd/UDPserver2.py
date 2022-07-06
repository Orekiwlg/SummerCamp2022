import socket

udpSocket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destinationSe2 = ('10.10.0.3', 8888)
destinationSe1 = ('192.168.0.12', 8888)
destinationRe = ('192.168.99.122', 8888)
udpSocket1.bind(destinationRe)

while True:
    receive = udpSocket1.recvfrom(1024)
    data = receive[0].decode('utf-8')
    address = str(receive[1])
    print(data, ' from ', address)
    udpSocket2.sendto(data.encode('utf-8'), destinationSe1)
    udpSocket3.sendto(data.encode('utf-8'), destinationSe2)
    if data == 'quit':
        break

print('program finished')

udpSocket1.close()