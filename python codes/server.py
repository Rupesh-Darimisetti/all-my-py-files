import socket

HOST='0.0.0.0' #means server will bind to any ip
PORT=12345

server_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)#creaes server tcp
server_socket.setSockopt(socket.SOL_SOCKET,socke.SO_REUSEADDR,1)#prevents from getting timeout issues
server_socket.blind((HOST,PORT))
server_socket.listen(5) #5 connections max in queue at a time
#see socketdocumentation to understand how socket.accept works
client_socket,(client_ip,client_port)=server_socket.accept() #accepts incoming connection

while True:
    command=raw_input(">")
    client_socket.send(command)
    if(command=="quit"):
      break
    
  data = client_socket.recv(1024)
  
print(data)
client_socket.close()
