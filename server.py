'''
    Count-It-First - Server
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
'''

from socket import *
import re
import sys
import random
from time import gmtime, strftime
from datetime import datetime

easySocket = socket(AF_INET, SOCK_STREAM) #TCP
easySocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable

hardSocket = socket(AF_INET, SOCK_STREAM) #TCP
hardSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable

# checks whether sufficient arguments have been provided
if len(sys.argv) != 2:
    print("Correct usage: script, IP address")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port1 = 43500       #Port for Easy mode
Port2 = 43505       #Port for Hard mode
Port3 = 43510       #Port for Practice mode

TWO_CLIENTS = 2
'''
 binds the server to an entered IP address and at the specified port number.
 The client must be aware of these parameters
 '''
#Connection socket for EASY mode
easySocket.bind((IP_address, int(Port1)))
easySocket.listen(1)

#Connection socket for HARD mode
serverSocket2.bind((IP_address, Port2))
serverSocket2.listen(1)

print('All servers are ready to accept clients')

clients = []
#accept up to 2 connections from clients, which
#must connect before we can move on

# broadcast() takes 2 parameters: a message and the connection to a client
# The function broadcasts the message to all clients whose object is not
# the same as the one sending the message
def broadcast(message, connection):
    for c in clients:
        if c[0] != connection:
            c[0].send(message)

# remove() takes 1 parameters: the connection
# The function removes the object from the list
def remove(connection):
    if connection in clients:
        clients.remove(connection)

while 1:
    for i in range(0, int(TWO_CLIENTS)):
        #accept the connection from client
        connectionSocket,addr = easySocket.accept()
        #add new clients to the list
        clients.append((connectionSocket,addr))
        #send welcome message to client
        num = int(len(clients)-1)
        connectionSocket.send(b'Welcome to the play room!\n')
        #Announce new connection
        welcomeMessage = "Player " + str(len(clients)-1) +" connected to server EASY"
        print(welcomeMessage)
    
    ranNum = random.randint(10,30)
    print("Generated number: ",ranNum)
    sum=0
    genNumMessage = b'Generated number: ' + str(ranNum).encode('utf-8')
    for c in clients:
        c[0].send(genNumMessage)
    #Prompt the first client to start the chat
    clients[0][0].send(b'\nSTART! ')
    #the loop makes the chat last infinitely
    while 1:
        for i in range(0,len(clients)):
            #receive message from client
            sentence = clients[i][0].recv(2048).decode('utf-8')
            print("Player ", i, " entered: ", sentence)
            sum+= int(sentence)
            print("Current Number: ", sum)
            #check if the message is "/close", if so, then close the connection
#            if sentence == "/close":
#                print("Client ",i," disconnected!")
#                clients[i][0].send(b'Good Bye!')
#                msg = b"Other client has disconnected. Chat ended"
#                broadcast(msg,clients[i][0])
#                clients[i][0].close()
#                remove(clients[i][0])
#
#                #check if the message is "/shutdown", if so, shut down the server
#            elif sentence == "/shutdown":
#                print("Server is shutting down!")
#                for c in clients:
#                    c[0].send(b'Server is shutting down!')
#
#                    c[0].close()
#                exit()
#            else:
#                #send received message to other client
            if sum == ranNum or sum == ranNum +1:
                print("THE WINNER IS PLAYER ",i)
                clients[i][0].send(b'YOU WIN')
                broadcast(b'YOU LOSE',clients[i][0])
                for c in clients:
                    c[0].close()
                exit()
            else:
                curNumberMsg = b'Current Number: ' + str(sum).encode('utf-8')
                for c in clients:
                    c[0].send(curNumberMsg)


