#!/usr/bin/python

import sys, socket

def main():
	print sys.argv
	if len(sys.argv) < 2:
		print "Supply address"
		return
	
	server_addr = sys.argv[1]
	print "Server address:", server_addr
	
	destination = (server_addr, 12345)
	print "Connecting to:", destination
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(destination)
	
	print "Connected"
	
	while True:
		my_str = raw_input()
		s.send(my_str + '\n')
	
	s.close()

if __name__ == '__main__':
	main()
