import socket

target_host = "www.google.com"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print response 1