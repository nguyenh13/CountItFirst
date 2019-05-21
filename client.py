#Tai Doan
#CPE4750 - Lab1: Chat Program
#Partner: Huyen Nguyen

from socket import *
import sys


clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket

# checks whether sufficient arguments have been provided
if len(sys.argv) != 2:
    print("Correct usage: script, IP address/host name")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

while 1:
    mode = input("Please choose mode (Enter 1 or 2):  1. Easy        2. Hard\n")
    if mode == "1":
        Port = 43500
        break
    elif mode == "2":
        Port = 10000
        break
    else:
        print("Invalid input")
print("Port is:", Port)

# connect to the server
connection = clientSocket.connect((IP_address,Port))

#After connected, client is welcomed by the server
welcomeMessage = clientSocket.recv(2048).decode('utf-8')
print(welcomeMessage)

#Get the message of generated number
number = clientSocket.recv(2048).decode('utf-8')
print(number)

#Get the message to start the chat
start = clientSocket.recv(2048).decode('utf-8')
print(start)

while 1:
    while 1:
        sentence = input('Enter 1 or 2: ')
        if sentence == "1" or sentence == "2":
            break
        else:
            print("Invalid input")
    try:
        clientSocket.send(sentence.encode('utf-8'))
        
        currentNumber = clientSocket.recv(2048).decode('utf-8')
        print(currentNumber)

        #if input is "close", close connection
        if sentence == "/close":
            closeMsg = clientSocket.recv(2048).decode('utf-8')
            print(closeMsg)
            clientSocket.close()
            exit()
        else:
            #receive message from server, print it
            fromServer = clientSocket.recv(2048).decode('utf-8')
            print(fromServer)

                

    #If cannot connect to server, close the connection
    except IOError:
        print("Server is shutting down!")
        clientSocket.close()
        exit()
clientSocket.close() #close connection
