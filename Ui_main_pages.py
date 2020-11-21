# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_ccir.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 800))
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 600))
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1001, 601))
        self.stackedWidget.setMinimumSize(QtCore.QSize(950, 500))
        self.stackedWidget.setAcceptDrops(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("background-color:white")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.start_page = QtWidgets.QWidget()
        self.start_page.setStyleSheet("background-color:white")
        self.start_page.setObjectName("start_page")
        self.label_2 = QtWidgets.QLabel(self.start_page)
        self.label_2.setGeometry(QtCore.QRect(280, 70, 471, 311))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/title we bare bear.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btn_startApp = QtWidgets.QPushButton(self.start_page)
        self.btn_startApp.setGeometry(QtCore.QRect(380, 420, 281, 61))
        self.btn_startApp.setStyleSheet("background-color:gray;\n"
"font: 13pt \"Shiny Signature\", \"Arial\";\n"
"color: white;")
        self.btn_startApp.setObjectName("btn_startApp")
        self.stackedWidget.addWidget(self.start_page)
        self.insert_page = QtWidgets.QWidget()
        self.insert_page.setAcceptDrops(True)
        self.insert_page.setStyleSheet("background-color:white")
        self.insert_page.setObjectName("insert_page")
        self.btn_chooseImage = QtWidgets.QPushButton(self.insert_page)
        self.btn_chooseImage.setGeometry(QtCore.QRect(330, 420, 181, 51))
        self.btn_chooseImage.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_chooseImage.setObjectName("btn_chooseImage")
        self.frame_dragDrop = QtWidgets.QFrame(self.insert_page)
        self.frame_dragDrop.setGeometry(QtCore.QRect(320, 120, 401, 271))
        self.frame_dragDrop.setAcceptDrops(True)
        self.frame_dragDrop.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_dragDrop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dragDrop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dragDrop.setObjectName("frame_dragDrop")
        self.cartoon_image = QtWidgets.QLabel(self.frame_dragDrop)
        self.cartoon_image.setGeometry(QtCore.QRect(20, 20, 361, 231))
        self.cartoon_image.setAcceptDrops(True)
        self.cartoon_image.setAutoFillBackground(False)
        self.cartoon_image.setStyleSheet("background-color:white;\n"
"border-radius: 0;\n"
"border: 2px dashed gray;\n"
"font-size: 11pt;\n"
"color: gray;")
        self.cartoon_image.setScaledContents(True)
        self.cartoon_image.setObjectName("cartoon_image")
        self.text1 = QtWidgets.QPlainTextEdit(self.insert_page)
        self.text1.setGeometry(QtCore.QRect(140, 30, 104, 31))
        self.text1.setObjectName("text1")
        self.btn_confirmImage = QtWidgets.QPushButton(self.insert_page)
        self.btn_confirmImage.setGeometry(QtCore.QRect(540, 420, 181, 51))
        self.btn_confirmImage.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_confirmImage.setObjectName("btn_confirmImage")
        self.stackedWidget.addWidget(self.insert_page)
        self.match_page = QtWidgets.QWidget()
        self.match_page.setStyleSheet("background-color:white")
        self.match_page.setObjectName("match_page")
        self.frame_3 = QtWidgets.QFrame(self.match_page)
        self.frame_3.setGeometry(QtCore.QRect(290, 100, 431, 261))
        self.frame_3.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.match_page_image = QtWidgets.QLabel(self.frame_3)
        self.match_page_image.setGeometry(QtCore.QRect(20, 20, 391, 221))
        self.match_page_image.setAutoFillBackground(False)
        self.match_page_image.setStyleSheet("background-color:white;\n"
"border-radius: 0;\n"
"")
        self.match_page_image.setText("")
        self.match_page_image.setScaledContents(True)
        self.match_page_image.setObjectName("match_page_image")
        self.btn_matchCharacter = QtWidgets.QPushButton(self.match_page)
        self.btn_matchCharacter.setGeometry(QtCore.QRect(520, 390, 201, 41))
        self.btn_matchCharacter.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_matchCharacter.setObjectName("btn_matchCharacter")
        self.btn_changeImage = QtWidgets.QPushButton(self.match_page)
        self.btn_changeImage.setGeometry(QtCore.QRect(300, 390, 201, 41))
        self.btn_changeImage.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_changeImage.setObjectName("btn_changeImage")
        self.pushButton_foundPage = QtWidgets.QPushButton(self.match_page)
        self.pushButton_foundPage.setGeometry(QtCore.QRect(470, 480, 161, 41))
        self.pushButton_foundPage.setStyleSheet("background-color:palegreen;\n"
"font: 8pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"")
        self.pushButton_foundPage.setObjectName("pushButton_foundPage")
        self.pushButton_notFoundPage = QtWidgets.QPushButton(self.match_page)
        self.pushButton_notFoundPage.setGeometry(QtCore.QRect(640, 480, 161, 41))
        self.pushButton_notFoundPage.setStyleSheet("background-color:pink;\n"
"font: 8pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"")
        self.pushButton_notFoundPage.setObjectName("pushButton_notFoundPage")
        self.text_2 = QtWidgets.QPlainTextEdit(self.match_page)
        self.text_2.setGeometry(QtCore.QRect(30, 20, 104, 31))
        self.text_2.setObjectName("text_2")
        self.stackedWidget.addWidget(self.match_page)
        self.not_found_page = QtWidgets.QWidget()
        self.not_found_page.setStyleSheet("background-color:white")
        self.not_found_page.setObjectName("not_found_page")
        self.label = QtWidgets.QLabel(self.not_found_page)
        self.label.setGeometry(QtCore.QRect(60, 50, 601, 41))
        self.label.setStyleSheet("background-color:pink;\n"
"border: 2px solid red;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label.setObjectName("label")
        self.btn_insertAnotherImage1 = QtWidgets.QPushButton(self.not_found_page)
        self.btn_insertAnotherImage1.setGeometry(QtCore.QRect(710, 480, 221, 71))
        self.btn_insertAnotherImage1.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Shiny Signature\", \"Arial\";\n"
"color: white;")
        self.btn_insertAnotherImage1.setObjectName("btn_insertAnotherImage1")
        self.frame = QtWidgets.QFrame(self.not_found_page)
        self.frame.setGeometry(QtCore.QRect(60, 110, 291, 211))
        self.frame.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_inputImage1 = QtWidgets.QLabel(self.frame)
        self.label_inputImage1.setGeometry(QtCore.QRect(10, 10, 271, 151))
        self.label_inputImage1.setAutoFillBackground(False)
        self.label_inputImage1.setStyleSheet("background-color:white;\n"
"border-radius: 0;")
        self.label_inputImage1.setText("")
        self.label_inputImage1.setPixmap(QtGui.QPixmap("images/we bare bear sticker medium.png"))
        self.label_inputImage1.setScaledContents(True)
        self.label_inputImage1.setObjectName("label_inputImage1")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 181, 31))
        self.label_4.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_4.setObjectName("label_4")
        self.frame_9 = QtWidgets.QFrame(self.not_found_page)
        self.frame_9.setGeometry(QtCore.QRect(370, 110, 291, 211))
        self.frame_9.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_20 = QtWidgets.QLabel(self.frame_9)
        self.label_20.setGeometry(QtCore.QRect(30, 80, 231, 61))
        self.label_20.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_20.setObjectName("label_20")
        self.label_6 = QtWidgets.QLabel(self.not_found_page)
        self.label_6.setGeometry(QtCore.QRect(70, 420, 441, 41))
        self.label_6.setStyleSheet("background-color:lightgray;\n"
"border: 2px solid gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.not_found_page)
        self.label_7.setGeometry(QtCore.QRect(70, 460, 441, 41))
        self.label_7.setStyleSheet("background-color:white;\n"
"border: 2px solid gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label_7.setObjectName("label_7")
        self.frame_10 = QtWidgets.QFrame(self.not_found_page)
        self.frame_10.setGeometry(QtCore.QRect(690, 110, 291, 251))
        self.frame_10.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_22 = QtWidgets.QLabel(self.frame_10)
        self.label_22.setGeometry(QtCore.QRect(30, 80, 231, 61))
        self.label_22.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_22.setObjectName("label_22")
        self.frame.raise_()
        self.label.raise_()
        self.btn_insertAnotherImage1.raise_()
        self.frame_9.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.frame_10.raise_()
        self.stackedWidget.addWidget(self.not_found_page)
        self.found_page = QtWidgets.QWidget()
        self.found_page.setObjectName("found_page")
        self.frame_7 = QtWidgets.QFrame(self.found_page)
        self.frame_7.setGeometry(QtCore.QRect(50, 100, 291, 211))
        self.frame_7.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_inputImage2 = QtWidgets.QLabel(self.frame_7)
        self.label_inputImage2.setGeometry(QtCore.QRect(10, 10, 261, 151))
        self.label_inputImage2.setAutoFillBackground(False)
        self.label_inputImage2.setStyleSheet("background-color:white;\n"
"border-radius: 0;")
        self.label_inputImage2.setText("")
        self.label_inputImage2.setPixmap(QtGui.QPixmap("images/we bare bear sticker medium.png"))
        self.label_inputImage2.setScaledContents(True)
        self.label_inputImage2.setObjectName("label_inputImage2")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 181, 31))
        self.label_3.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_3.setObjectName("label_3")
        self.label_15 = QtWidgets.QLabel(self.found_page)
        self.label_15.setGeometry(QtCore.QRect(50, 40, 291, 41))
        self.label_15.setStyleSheet("background-color:palegreen;\n"
"border: 2px solid green;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label_15.setObjectName("label_15")
        self.btn_insertAnotherImage2 = QtWidgets.QPushButton(self.found_page)
        self.btn_insertAnotherImage2.setGeometry(QtCore.QRect(740, 480, 211, 71))
        self.btn_insertAnotherImage2.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Shiny Signature\", \"Arial\";\n"
"color: white;")
        self.btn_insertAnotherImage2.setObjectName("btn_insertAnotherImage2")
        self.label_characterName = QtWidgets.QLabel(self.found_page)
        self.label_characterName.setGeometry(QtCore.QRect(370, 40, 291, 41))
        self.label_characterName.setStyleSheet("background-color:palegreen;\n"
"border: 2px solid green;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label_characterName.setObjectName("label_characterName")
        self.frame_8 = QtWidgets.QFrame(self.found_page)
        self.frame_8.setGeometry(QtCore.QRect(370, 100, 291, 211))
        self.frame_8.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_17 = QtWidgets.QLabel(self.frame_8)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 271, 151))
        self.label_17.setAutoFillBackground(False)
        self.label_17.setStyleSheet("background-color:white;\n"
"border-radius: 0;")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("images/title we bare bear.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_8)
        self.label_18.setGeometry(QtCore.QRect(10, 170, 271, 31))
        self.label_18.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_18.setObjectName("label_18")
        self.text_3 = QtWidgets.QPlainTextEdit(self.found_page)
        self.text_3.setGeometry(QtCore.QRect(140, 430, 191, 31))
        self.text_3.setObjectName("text_3")
        self.text_4 = QtWidgets.QPlainTextEdit(self.found_page)
        self.text_4.setGeometry(QtCore.QRect(790, 360, 104, 31))
        self.text_4.setObjectName("text_4")
        self.frame_11 = QtWidgets.QFrame(self.found_page)
        self.frame_11.setGeometry(QtCore.QRect(690, 100, 291, 251))
        self.frame_11.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_23 = QtWidgets.QLabel(self.frame_11)
        self.label_23.setGeometry(QtCore.QRect(30, 80, 231, 61))
        self.label_23.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_23.setObjectName("label_23")
        self.stackedWidget.addWidget(self.found_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cartoon Character Image Retrieval"))
        self.btn_startApp.setText(_translate("MainWindow", "START APPLICATION"))
        self.btn_chooseImage.setText(_translate("MainWindow", "Choose Image"))
        self.cartoon_image.setText(_translate("MainWindow", "         Choose an image to search"))
        self.text1.setPlainText(_translate("MainWindow", "insert page"))
        self.btn_confirmImage.setText(_translate("MainWindow", "Confirm Image"))
        self.btn_matchCharacter.setText(_translate("MainWindow", "Match Character"))
        self.btn_changeImage.setText(_translate("MainWindow", "Change Image"))
        self.pushButton_foundPage.setText(_translate("MainWindow", "Found page"))
        self.pushButton_notFoundPage.setText(_translate("MainWindow", "Not Found page"))
        self.text_2.setPlainText(_translate("MainWindow", "match page"))
        self.label.setText(_translate("MainWindow", "Character Not Found"))
        self.btn_insertAnotherImage1.setText(_translate("MainWindow", "INSERT ANOTHER\n"
"IMAGE"))
        self.label_4.setText(_translate("MainWindow", "Input Image"))
        self.label_20.setText(_translate("MainWindow", "No Retrieved \n"
"Character"))
        self.label_6.setText(_translate("MainWindow", "No Appearance Time"))
        self.label_7.setText(_translate("MainWindow", " - "))
        self.label_22.setText(_translate("MainWindow", "No Video Match"))
        self.label_3.setText(_translate("MainWindow", "Input Image"))
        self.label_15.setText(_translate("MainWindow", "Character Found"))
        self.btn_insertAnotherImage2.setText(_translate("MainWindow", "INSERT ANOTHER\n"
"IMAGE"))
        self.label_characterName.setText(_translate("MainWindow", "naruto"))
        self.label_18.setText(_translate("MainWindow", "Retrieved Character"))
        self.text_3.setPlainText(_translate("MainWindow", "list time appearance"))
        self.text_4.setPlainText(_translate("MainWindow", "video play"))
        self.label_23.setText(_translate("MainWindow", "Video Match"))
