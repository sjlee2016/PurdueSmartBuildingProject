import socket

UDP_IP = "192.168.20.86"

UDP_PORT = 5005
MESSAGE = " "
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#sock.bind(MESSAGE, (UDP_IP, UDP_PORT))

while True:

	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

print "received message:", data
