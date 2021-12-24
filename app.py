import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the socket.
mysocket.connect(("data.pr4e.org", 80)) # "Dial the phone", as in start connecting/calling. The port is the 2nd parameter (80).
cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode() # Encode the command in unicode UTF8. "GET URL Protocol/1.0". The \r\n is necessary and must repeat twice.
mysocket.send(cmd) # Send the command through the socket.

# Busy waiting.
while True:
    data = mysocket.recv(512) # Receive 512 bytes of data from the socket.
    if len(data) < 1:
        break
    print(data.decode(), end='') # Decode the data.

mysocket.close()