'''
    Count-It-First - Client
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
    '''

from socket import *
import sys


def checkResult(message):
    if message == "YOU WIN" or message == "YOU LOSE":
        return 0


clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket

# checks whether sufficient arguments have been provided
if len(sys.argv) != 2:
    print("Correct usage: script, IP address/host name")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

#Mode selection
while 1:
    mode = input("Please choose mode (Enter 1 or 2):  1. Easy        2. Hard\n")
    if mode == "1":
        Port = 43500
        print("You have chosen EASY mode!")
        break
    elif mode == "2":
        Port = 43505
        print("You have chosen HARD mode!")
        break
    else:
        print("Invalid input")

#connect to the server
connection = clientSocket.connect((IP_address,Port))

#After connected, player is welcomed by the server
welcomeMessage = clientSocket.recv(2048).decode('utf-8')
print(welcomeMessage)

#Get the message of generated number
number = clientSocket.recv(2048).decode('utf-8')
print(number)

#Get the message to start the game
start = clientSocket.recv(2048).decode('utf-8')
print(start)

#Game loop
while 1:
    print("\nYOUR TURN")
    #Valid input is only 1 or 2
    while 1:
        inputNumber = input('Enter 1 or 2: ')
        if inputNumber == "1" or inputNumber == "2":
            break
        else:
            print("Invalid input")
    try:
        #Send player's input
        clientSocket.send(inputNumber.encode('utf-8'))
        #Receive current total number from server
        currentNumber = clientSocket.recv(2048).decode('utf-8')
        print(currentNumber)
        if checkResult(currentNumber) == 0:
            clientSocket.close()
            exit()

        #if input is "close", close connection
        if inputNumber == "/close":
            closeMsg = clientSocket.recv(2048).decode('utf-8')
            print(closeMsg)
            clientSocket.close()
            exit()
        else:
            #receive message from server, print it
            fromServer = clientSocket.recv(2048).decode('utf-8')
            print(fromServer)
            if checkResult(fromServer) == 0:
                clientSocket.close()
                exit()
    #If cannot connect to server, close the connection
    except IOError:
        print("Connection error")
        clientSocket.close()
        exit()
clientSocket.close() #close connection
