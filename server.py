#Tai Doan
#CPE4750 - Lab1: Chat program
#Partner: Huyen Nguyen

from socket import *
import re
import sys
import random
from time import gmtime, strftime
from datetime import datetime

serverSocket1 = socket(AF_INET, SOCK_STREAM) #TCP
serverSocket1.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable

serverSocket2 = socket(AF_INET, SOCK_STREAM) #TCP
serverSocket2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable

# checks whether sufficient arguments have been provided
if len(sys.argv) != 2:
    print("Correct usage: script, IP address, port number")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port1 = 43500
Port2 = 10000

MAX_CLIENTS = 2 #Max client for this program is 2

# binds the server to an entered IP address and at the
# specified port number.
# The client must be aware of these parameters
serverSocket1.bind((IP_address, int(Port1)))
serverSocket1.listen(1)
print('The server EASY is ready to accept players')

# binds the server to an entered IP address and at the
# specified port number.
# The client must be aware of these parameters
serverSocket2.bind((IP_address, Port2))
serverSocket2.listen(1)
print('The server HARD is ready to accept clients')

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

#
#def game(num):
#    sum = 0
#    sum += num
#    if sum <= ranNum:
#        print("Current number: ",sum)
#        print("\n")
#        if sum == ranNum or sum == ranNum+1:
#            print("Winner is Player " + str(len(clients)-1))
#        for i in range(1,3):
#            if sum == ranNum-i :
#                print("Player " + str(len(clients)-1) +" is about to win")

    return sum

while 1:
    for i in range(0, int(MAX_CLIENTS)):
        #accept the connection from client
        connectionSocket,addr = serverSocket1.accept()
        #add new clients to the list
        clients.append((connectionSocket,addr))
        #send welcome message to client
        num = int(len(clients)-1)
        connectionSocket.send(b'Welcome to the chatroom!\n')
        #Announce new connection
        welcomeMessage = "Player " + str(len(clients)-1) +" connected to server EASY"
        print(welcomeMessage)
    
    ranNum = random.randint(10,30)
    print(ranNum)
    sum=0
    genNumMessage = b'Generated number: ' + str(ranNum).encode('utf-8')
    for c in clients:
        c[0].send(genNumMessage)
    #Prompt the first client to start the chat
    clients[0][0].send(b'\nSTART!')
    #the loop makes the chat last infinitely
    while 1:
        for i in range(0,len(clients)):
            #receive message from client
            sentence = clients[i][0].recv(2048).decode('utf-8')
            print("Player ", i, " entered: ", sentence)
            sum+= int(sentence)
            print("Current Number: ", sum)
            #check if the message is "/close", if so, then close the connection
            if sentence == "/close":
                print("Client ",i," disconnected!")
                clients[i][0].send(b'Good Bye!')
                msg = b"Other client has disconnected. Chat ended"
                broadcast(msg,clients[i][0])
                clients[i][0].close()
                remove(clients[i][0])

                #check if the message is "/shutdown", if so, shut down the server
            elif sentence == "/shutdown":
                print("Server is shutting down!")
                for c in clients:
                    c[0].send(b'Server is shutting down!')

                    c[0].close()
                exit()
            else:
                #send received message to other client
                if sum == ranNum or sum == ranNum +1:
                    #print("Player ", clients[i][0], " WIN")
                    #winner = b'Player' ,str(i).encode('utf-8'), b'WIN'
                    
                    clients[i][0].send(b'You Win. End Game')
                    broadcast(b'You Lose. End Game',clients[i][0])
                #broadcast(sentence.encode('utf-8'),clients[i][0])
                else:
                    curNumberMsg = b'Current Number: ' + str(sum).encode('utf-8')
                    for c in clients:
                        c[0].send(curNumberMsg)

