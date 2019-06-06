
'''
    Count-It-First - Server HARD
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
    '''

from socket import *
import re
import sys
import random
from time import gmtime, strftime
from datetime import datetime

hardSocket = socket(AF_INET, SOCK_STREAM) #TCP
hardSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable

# checks whether sufficient arguments have been provided
if len(sys.argv) != 2:
    print("Correct usage: script, IP address")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])
# takes second argument from command prompt as port number
Port2 = 43505       #Port for Hard mode

#accept up to 2 connections from clients, which
#must connect before we can move on
TWO_CLIENTS = 2

#Connection socket for HARD mode
hardSocket.bind((IP_address, int(Port2)))
hardSocket.listen(1)

print('Server HARD is ready to accept client')

clients_hard = []

# broadcast() takes 2 parameters: a message and the connection to a client
# The function broadcasts the message to all clients whose object is not
# the same as the one sending the message
def broadcast(message, connection, receiver):
    for c in receiver:
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
        connectionSocket_Hard,addr_H = hardSocket.accept()
        #add new clients to the list
        clients_hard.append((connectionSocket_Hard,addr_H))
        #send welcome message to client
        connectionSocket_Hard.send(b'Welcome to the play room!\n')
        #Announce new connection
        welcomeMessage = "Player " + str(len(clients_hard)-1) +" connected to server HARD"
        print(welcomeMessage)
    
    ranNum = random.randint(30,50)
    print("Generated number: ",ranNum)
    sum=0
    genNumMessage = b'Generated number: ' + str(ranNum).encode('utf-8')
    for c in clients_hard:
        c[0].send(genNumMessage)
    #Prompt the first client to start the chat
    clients_hard[0][0].send(b'\nSTART! ')
    #the loop makes the chat last infinitely
    while 1:
        for i in range(0,len(clients_hard)):
            #receive message from client
            sentence = clients_hard[i][0].recv(2048).decode('utf-8')
            print("Player ", i, " entered: ", sentence)
            sum+= int(sentence)
            print("Current Number: ", sum)
            if sum == ranNum or sum > ranNum:
                print("THE WINNER IS PLAYER ",i)
                clients_hard[i][0].send(b'YOU WIN')
                broadcast(b'YOU LOSE',clients_hard[i][0],clients_hard)
                for c in clients_hard:
                    c[0].close()
                exit()
            else:
                curNumberMsg = b'Current Number: ' + str(sum).encode('utf-8')
                for c in clients_hard:
                    c[0].send(curNumberMsg)
