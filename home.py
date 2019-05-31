# -*- coding: utf-8 -*-

'''
    Count-It-First - Server
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
'''

from socket import *
import re
import sys
import random,time
from time import gmtime, strftime
from datetime import datetime

# --GUI import library--
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QScrollBar,QSplitter,QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, QPushButton, QApplication, QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit)
from PyQt5.QtCore import QCoreApplication

#Connection between Home Page and Game Page
from game import Ui_gameWindow

#Threads
from threading import Thread 
from socketserver import ThreadingMixIn 

class Ui_MainWindow(object):
    def openEasyGame(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_gameWindow() #connect with game.py
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 327)
        MainWindow.setStyleSheet("background: #151515;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gameLabel = QtWidgets.QLabel(self.centralwidget)
        self.gameLabel.setGeometry(QtCore.QRect(80, 10, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.gameLabel.setFont(font)
        self.gameLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"text-align: center;\n"
"color: #e7e7e7;\n"
"letter-spacing: 5px;")
        self.gameLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameLabel.setObjectName("gameLabel")
        self.easyButton = QtWidgets.QPushButton(self.centralwidget)
        self.easyButton.setGeometry(QtCore.QRect(150, 100, 111, 41))
        self.easyButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.easyButton.setObjectName("easyButton")

        self.easyButton.clicked.connect(self.openEasyGame)

        self.hardButton = QtWidgets.QPushButton(self.centralwidget)
        self.hardButton.setGeometry(QtCore.QRect(150, 150, 111, 41))
        self.hardButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")

        self.hardButton.setObjectName("hardButton")
        self.practiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.practiceButton.setGeometry(QtCore.QRect(150, 200, 111, 41))
        self.practiceButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.practiceButton.setObjectName("practiceButton")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(340, 250, 51, 32))
        self.quitButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: red;")
        self.quitButton.setObjectName("quitButton")
        self.gameModeLabel = QtWidgets.QLabel(self.centralwidget)
        self.gameModeLabel.setGeometry(QtCore.QRect(120, 70, 181, 16))
        self.gameModeLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.gameModeLabel.setObjectName("gameModeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gameLabel.setText(_translate("MainWindow", "Welcome to Count-It-First"))
        self.easyButton.setText(_translate("MainWindow", "EASY"))
        self.hardButton.setText(_translate("MainWindow", "HARD"))
        self.practiceButton.setText(_translate("MainWindow", "PRACTICE"))
        self.quitButton.setText(_translate("MainWindow", "QUIT"))
        self.gameModeLabel.setText(_translate("MainWindow", "Choose your game mode:"))


""" class ServerThread(Thread):
    def __init__(self,window): 
        Thread.__init__(self) 
        self.window=window

 
    def run(self): 
        TCP_IP = '0.0.0.0' 
        TCP_PORT = 80 
        BUFFER_SIZE = 20  
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        tcpServer.bind((TCP_IP, TCP_PORT)) 
        threads = [] 
        
        tcpServer.listen(4) 
        while True:
            print("Multithreaded Python server : Waiting for connections from TCP clients...") 
            global conn
            (conn, (ip,port)) = tcpServer.accept() 
            newthread = ClientThread(ip,port,window) 
            newthread.start() 
            threads.append(newthread) 
        
 
        for t in threads: 
            t.join() 



class ClientThread(Thread): 
 
    def __init__(self,ip,port,window): 
        Thread.__init__(self) 
        self.window=window
        self.ip = ip 
        self.port = port 
        print("[+] New server socket thread started for " + ip + ":" + str(port)) 
 
    def run(self): 
        while True : 
            
            #(conn, (self.ip,self.port)) = serverThread.tcpServer.accept() 
            global conn
            data = conn.recv(2048) 
            window.chat.append(data.decode("utf-8"))
            print(data)

 """

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
