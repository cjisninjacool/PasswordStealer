import socket
import time
import sys

HOST = "192.168.177.129"

PORT = 5454
filename = sys.argv[1]
file1 = open(filename) 
data = file1.read()
file1.close()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST,PORT))
s.sendto(str.encode(data),(HOST,PORT))
print ("send: "+ data)
time.sleep(1)