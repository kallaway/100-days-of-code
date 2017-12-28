import socket

target_host = "127.0.0.1"
target_port = 80

#create a socket object
client.sendto("AAABBBCCC",(target_host,target_port))

#receive some data
data, addr = client.recvfrom(4096)

print data 1