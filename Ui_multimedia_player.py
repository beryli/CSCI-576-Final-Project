# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Beryl\USC\20231_CSCI576_Multimedia_Systems_Design\Final_Project\GUI\multimedia_player.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QStyle
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QAudioDeviceInfo, QAudio
from PyQt5.QtMultimediaWidgets import QVideoWidget

# input_audio_deviceInfos = QAudioDeviceInfo.availableDevices(QAudio.AudioInput)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.content = QtWidgets.QWidget(self.centralwidget)
        self.content.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.content.setObjectName("content")
        self.scrollArea = QtWidgets.QScrollArea(self.content)
        self.scrollArea.setGeometry(QtCore.QRect(30, 50, 361, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1359, 338, 1857))
        self.scrollAreaWidgetContents.setAcceptDrops(False)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 90))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 90))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 90))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 90))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 90))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 90))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.display = QtWidgets.QWidget(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(400, 0, 600, 600))
        self.display.setObjectName("display")
        self.widget = QtWidgets.QWidget(self.display)
        self.widget.setGeometry(QtCore.QRect(60, 50, 502, 491))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.video = QtWidgets.QWidget(self.widget)
        # self.video.setMinimumSize(QtCore.QSize(480, 270))
        # self.video.setMaximumSize(QtCore.QSize(500, 300))
        # self.video.setStyleSheet("background-color: rgb(65, 65, 65)")
        # self.video.setObjectName("video")
        # self.verticalLayout.addWidget(self.video)
        # below is temporal code
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        videoWidget.setMinimumSize(QtCore.QSize(480, 270))
        videoWidget.setMaximumSize(QtCore.QSize(500, 300))
        self.verticalLayout.addWidget(videoWidget)
        # above is temporal code

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Play = QtWidgets.QPushButton(self.widget)
        self.Play.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Play.setFont(font)
        self.Play.setStyleSheet("QPushButton{\n"
"border: 1px solid rgb(50, 50, 50); border-radius:10px; padding:2px 4px;\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"QPushButton:hover{background-color: rgb(170, 170, 170); color: black;}\n"
"QPushButton:pressed{background-color:rgb(200, 200, 200); border-style: inset; }")
        self.Play.setObjectName("Play")
        self.horizontalLayout.addWidget(self.Play)
        self.Pause = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Pause.setFont(font)
        self.Pause.setStyleSheet("QPushButton{\n"
"border: 1px solid rgb(50, 50, 50); border-radius:10px; padding:2px 4px;\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"QPushButton:hover{background-color: rgb(170, 170, 170); color: black;}\n"
"QPushButton:pressed{background-color:rgb(200, 200, 200); border-style: inset; }")
        self.Pause.setObjectName("Pause")
        self.horizontalLayout.addWidget(self.Pause)
        self.Stop = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Stop.setFont(font)
        self.Stop.setStyleSheet("QPushButton{\n"
"border: 1px solid rgb(50, 50, 50); border-radius:10px; padding:2px 4px;\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"QPushButton:hover{background-color: rgb(170, 170, 170); color: black;}\n"
"QPushButton:pressed{background-color:rgb(200, 200, 200); border-style: inset; }")
        self.Stop.setObjectName("Stop")
        self.horizontalLayout.addWidget(self.Stop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        """ Video """
        self.Play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.Play.clicked.connect(self.play)
        self.Pause.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        self.Pause.clicked.connect(self.pause)
        self.Stop.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.Stop.clicked.connect(self.stop)
        self.mediaPlayer.setVideoOutput(videoWidget)
        filename = "InputVideo.avi"
        self.mediaPlayer.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(filename)))
        """ Audio  """
        filename = "InputAudio.mp3"
        self.audioPlayer = QMediaPlayer()
        self.audioPlayer.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(filename)))
        self.is_stop = False
        """ Table of Content """
        self.pushButton.clicked.connect(lambda: self.jump(1))
        self.pushButton_2.clicked.connect(lambda: self.jump(2))
        self.pushButton_3.clicked.connect(lambda: self.jump(3))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mediaPlayer.pause()
        self.audioPlayer.pause()

        
    def play(self):
        if self.is_stop == True:
            self.mediaPlayer.setPosition(0) # to start at the beginning of the video every time
            self.audioPlayer.setPosition(0) # to start at the beginning of the video every time
        self.is_stop = False

        if self.mediaPlayer.state() != QMediaPlayer.PlayingState:
            self.audioPlayer.play()
            self.mediaPlayer.play()
            # if self.audioPlayer.state() == QMediaPlayer.PlayingState:
            print(self.mediaPlayer.position())
            print(self.audioPlayer.position())
            print()
                
        
    def pause(self):
        self.mediaPlayer.pause()
        self.audioPlayer.pause()
    
    def stop(self):
        self.is_stop = True
        self.mediaPlayer.pause()
        self.audioPlayer.pause()


    def jump(self, id):
        if id == 1:
            self.audioPlayer.setPosition(100000*3)
            self.mediaPlayer.setPosition(100000)
            self.pushButton.setStyleSheet("QPushButton{background-color: rgb(170, 170, 170); color: black;}")
            self.pushButton_2.setStyleSheet("QPushButton{background-color: rgb(50, 50, 50);}")
        if id == 2:
            self.pushButton.setStyleSheet("QPushButton{background-color: rgb(50, 50, 50);}")
            self.pushButton_2.setStyleSheet("QPushButton{background-color: rgb(170, 170, 170); color: black;}")
            self.audioPlayer.setPosition(200000*3)
            self.mediaPlayer.setPosition(200000)
        if id == 3:
            self.audioPlayer.setPosition(10000)
            self.mediaPlayer.setPosition(10000)
        self.mediaPlayer.pause()
        self.audioPlayer.pause()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interactive Media Player"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.Play.setText(_translate("MainWindow", "Play"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.Stop.setText(_translate("MainWindow", "Stop"))

