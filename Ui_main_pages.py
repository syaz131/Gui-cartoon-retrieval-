# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ccir.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 605)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 800))
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1011, 661))
        self.stackedWidget.setMinimumSize(QtCore.QSize(950, 500))
        self.stackedWidget.setStyleSheet("background-color:white")
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
        self.insert_page.setStyleSheet("background-color:white")
        self.insert_page.setObjectName("insert_page")
        self.btn_insertImage = QtWidgets.QPushButton(self.insert_page)
        self.btn_insertImage.setGeometry(QtCore.QRect(390, 390, 181, 51))
        self.btn_insertImage.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_insertImage.setObjectName("btn_insertImage")
        self.frame_dragDrop = QtWidgets.QFrame(self.insert_page)
        self.frame_dragDrop.setGeometry(QtCore.QRect(330, 150, 291, 211))
        self.frame_dragDrop.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_dragDrop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dragDrop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dragDrop.setObjectName("frame_dragDrop")
        self.label_dragDrop = QtWidgets.QLabel(self.frame_dragDrop)
        self.label_dragDrop.setGeometry(QtCore.QRect(50, 90, 191, 61))
        self.label_dragDrop.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_dragDrop.setObjectName("label_dragDrop")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.insert_page)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 30, 104, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.stackedWidget.addWidget(self.insert_page)
        self.match_page = QtWidgets.QWidget()
        self.match_page.setStyleSheet("background-color:white")
        self.match_page.setObjectName("match_page")
        self.frame_3 = QtWidgets.QFrame(self.match_page)
        self.frame_3.setGeometry(QtCore.QRect(320, 100, 391, 221))
        self.frame_3.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(60, 20, 281, 171))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-color:white;\n"
"border-radius: 0;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("images/we bare bear sticker medium.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.btn_matchCharacter = QtWidgets.QPushButton(self.match_page)
        self.btn_matchCharacter.setGeometry(QtCore.QRect(520, 350, 201, 41))
        self.btn_matchCharacter.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_matchCharacter.setObjectName("btn_matchCharacter")
        self.btn_changeImage = QtWidgets.QPushButton(self.match_page)
        self.btn_changeImage.setGeometry(QtCore.QRect(300, 350, 201, 41))
        self.btn_changeImage.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_changeImage.setObjectName("btn_changeImage")
        self.pushButton_foundPage = QtWidgets.QPushButton(self.match_page)
        self.pushButton_foundPage.setGeometry(QtCore.QRect(540, 410, 161, 41))
        self.pushButton_foundPage.setStyleSheet("background-color:gray;\n"
"font: 10pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.pushButton_foundPage.setObjectName("pushButton_foundPage")
        self.pushButton_notFoundPage = QtWidgets.QPushButton(self.match_page)
        self.pushButton_notFoundPage.setGeometry(QtCore.QRect(540, 470, 161, 41))
        self.pushButton_notFoundPage.setStyleSheet("background-color:gray;\n"
"font: 10pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.pushButton_notFoundPage.setObjectName("pushButton_notFoundPage")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.match_page)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(30, 20, 104, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.stackedWidget.addWidget(self.match_page)
        self.not_found_page = QtWidgets.QWidget()
        self.not_found_page.setStyleSheet("background-color:white")
        self.not_found_page.setObjectName("not_found_page")
        self.label = QtWidgets.QLabel(self.not_found_page)
        self.label.setGeometry(QtCore.QRect(60, 50, 501, 41))
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
        self.frame.setGeometry(QtCore.QRect(60, 120, 291, 211))
        self.frame.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 261, 151))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color:white;\n"
"border-radius: 0;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/we bare bear sticker medium.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 181, 31))
        self.label_4.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_4.setObjectName("label_4")
        self.frame.raise_()
        self.label.raise_()
        self.btn_insertAnotherImage1.raise_()
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
        self.label_13 = QtWidgets.QLabel(self.frame_7)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 261, 151))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("background-color:white;\n"
"border-radius: 0;")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("images/we bare bear sticker medium.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_7)
        self.label_14.setGeometry(QtCore.QRect(50, 170, 181, 31))
        self.label_14.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_14.setObjectName("label_14")
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
        self.label_16 = QtWidgets.QLabel(self.found_page)
        self.label_16.setGeometry(QtCore.QRect(370, 40, 291, 41))
        self.label_16.setStyleSheet("background-color:palegreen;\n"
"border: 2px solid green;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label_16.setObjectName("label_16")
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
        self.stackedWidget.addWidget(self.found_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cartoon Character Image Retrieval"))
        self.btn_startApp.setText(_translate("MainWindow", "START APPLICATION"))
        self.btn_insertImage.setText(_translate("MainWindow", "Insert Image"))
        self.label_dragDrop.setText(_translate("MainWindow", "Drag and drop \n"
"image"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "insert page"))
        self.btn_matchCharacter.setText(_translate("MainWindow", "Match Character"))
        self.btn_changeImage.setText(_translate("MainWindow", "Change Image"))
        self.pushButton_foundPage.setText(_translate("MainWindow", "Found page"))
        self.pushButton_notFoundPage.setText(_translate("MainWindow", "Not Found page"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "match page"))
        self.label.setText(_translate("MainWindow", "Character Not Found"))
        self.btn_insertAnotherImage1.setText(_translate("MainWindow", "INSERT ANOTHER\n"
"IMAGE"))
        self.label_4.setText(_translate("MainWindow", "Input Image"))
        self.label_14.setText(_translate("MainWindow", "Input Image"))
        self.label_15.setText(_translate("MainWindow", "Character Found"))
        self.btn_insertAnotherImage2.setText(_translate("MainWindow", "INSERT ANOTHER\n"
"IMAGE"))
        self.label_16.setText(_translate("MainWindow", "naruto"))
        self.label_18.setText(_translate("MainWindow", "Retrieved Character"))
