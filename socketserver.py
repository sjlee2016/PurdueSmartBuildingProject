import socket
import functions

HOST = "192.168.20.92"
PORT = 5522
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
s.bind((HOST, PORT))
print ('Socket bind complete')
s.listen(1)
print ('Socket now listening')

# pi control function
def do_some_stuffs_with_input(input_string):
	#Raspberry Pi control
	if input_string == "down":
		input_string = "shutter down"
		functions.servo()
	elif input_string == "up":
		input_string = "shutter Up"
		# gate down func
	elif input_string == "capture":
		input_string = "take a picture"
		#  take pic func
	else :
		input_string = input_string + " <-- incorrect message"
		
	print(input_string)

	return input_string

while True:
	
	conn, addr = s.accept()
	print("Connected by", addr)

	data = conn.recv(1024)
	data = data.decode("utf8").strip()
	if not data: break
	print("Received : " + data)
	
	res = do_some_stuffs_with_input(data)
	print("Pi work :" + res)

	conn.sendall(res.encode("utf8"))
	conn.close()
s.close()
