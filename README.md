# Count-It-First
# Networked counting game
# CSC/CPE 4750
# Author: Tai Doan, Hung Nguyen, Huyen Nguyen

## 1. Features:
Server-client based  using TCP socket connection.
There are 2 servers always be running concurrently for 2 game modes Easy and Hard.
When starting the application, player is able to choose game mode.
	Mode Easy: Random number generated in range [10,30], add +1 or +2.
	Mode Hard: Random number generated in range [30,50], add +1, +3 or +5
The game will start when 2 players connect to the same room (i.e. the server)
Players will be announced what the "Win number" is from the server. Each player will take turn to input a number and send it to the server, the number will be added up to the sum. Whoever reaches the generated number first will win the game.


## 2. Installation:
Run server: Change directory to the folder contains the server files	
```bash
python3   server-Easy.py   IP-address
```
Server Easy will run on Port 43500
	
```bash
python3   server-Hard.py   IP-address
```
Server Hard will run on Port 43505

Run client: Change directory to the folder contains the file (client.py)
```bash
python3   client.py   IP-address/hostname 
```
Choose game mode: 1. Easy     2. Hard. 
-> The player will be connected to the chosen 	server accordingly.

Repeat the process for another client

			


