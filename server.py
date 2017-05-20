#!/usr/bin/env python

import threading
import socket
import select
import sys
import errno
import sync
import signal

BUFFER_SIZE = 1024 # change this for a faster response , default: 1024

PORT_TeltonikaFXXXX = 20020
PORT_Atrack = 20030

SERVER_LIST = []

threads = []

class Server(object):
	""" TCP Server class"""
	
	def __init__(self, tcp_ip='127.0.0.1', backlog=10):
		self.connections = 0
		self.server_addr = (tcp_ip, PORT_TeltonikaFXXXX)
		# output socket list
		self.outputs = []
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)			
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind(self.server_addr)
		# Create a TCP/IP socket
		print ('starting up tcp server on %s port %s' % self.server_addr)
		# Listen for incoming connections
		self.server.listen(backlog)
		#KeyboardInterrupt
		signal.signal(signal.SIGINT, self.sighandler)
		
	def sighandler(self, frame):
		# close the server
		print ("shutting down the server...")
		for o in self.outputs:
			o.close()
		
		self.server.close()
		
	def worker(self, conn):
		buffer=""
		while True:
			data = conn.recv(8192)
			if data:
				print (data)
		#conn.sendall(reply)
		conn.close()
		return
		
	def serve(self):
		running = 1
		
		while running:
		
			# accept connection from outside
			conn, addr = self.server.accept()
			print ('connection from', addr)
			t = threading.Thread(target=self.worker, args=(conn,))
			threads.append(t)
			t.start()
			
		
		self.server.close()