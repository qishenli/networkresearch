import socket, sys , random
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

MAX=65535
PORT=1060
input=sys.argv[1:]
if input == ['server']:
	s.bind(('127.0.0.1',PORT))
	while True:
        	data,address= s.recvfrom(MAX)
        	print 'The client', 'says', repr(data)
		if random.randint(0,1):
			print('The server decides to send data to client')
        		s.sendto('Your data was %d bytes' % len(data), address)	
elif (len(input) == 2) and (input[0] == 'client'):
	while True:
        	s.sendto(input[1], ('127.0.0.1',PORT))
        	data, address = s.recvfrom(MAX)
        	print 'The server', 'says', repr(data)
else:
        print >>sys.stderr, 'usage: udp_local.py server|client [content]'
