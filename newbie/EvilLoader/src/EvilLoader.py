import socket
import threading
import random 
import string
import time 

bind_ip = "0.0.0.0"
bind_port = 31337
 
server = socket.socket()
server.bind((bind_ip,bind_port))
server.listen(5)
print(f"[*] Listening on {bind_ip}:{bind_port}")

# this is our client-handling thread
def handle_client(client_socket):
   
        try:
            time.sleep(2)
            client_socket.send(b"Please wait")
            time.sleep(2)
            
            for _ in range(3):
                    client_socket.send(b".")
                    time.sleep(2)
            client_socket.send(b"\n")
            
            client_socket.send(b" Your machine is being rooted")
            
            for _ in range(3):
                    client_socket.send(b".")
                    time.sleep(2)
            client_socket.send(b"\n")
            
            client_socket.send(b"  [")
            
            for _ in range(30):
                    client_socket.send(b"=")
                    time.sleep(0.1)
            client_socket.send(b"]\n")

            client_socket.send(b"   Welcome to Our botnet. Here's your flag!\n")
            time.sleep(2)
            client_socket.send( b'   PermCTF{now_it_is_a_time_to_hack_the_planet}' )
            client_socket.close()

        except BrokenPipeError:
            pass
    
while True:
    try:
        client,addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}{addr[1]}")
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()
    except:
        break
