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
        MainWindow.resize(1282, 753)
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
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 1261, 711))
        self.stackedWidget.setMinimumSize(QtCore.QSize(950, 500))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setAcceptDrops(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("background-color:white")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.start_page = QtWidgets.QWidget()
        self.start_page.setStyleSheet("background-color:white")
        self.start_page.setObjectName("start_page")
        self.label_ico_bear = QtWidgets.QLabel(self.start_page)
        self.label_ico_bear.setGeometry(QtCore.QRect(320, 110, 611, 361))
        self.label_ico_bear.setText("")
        self.label_ico_bear.setScaledContents(True)
        self.label_ico_bear.setObjectName("label_ico_bear")
        self.btn_startApp = QtWidgets.QPushButton(self.start_page)
        self.btn_startApp.setGeometry(QtCore.QRect(470, 510, 311, 71))
        self.btn_startApp.setStyleSheet("background-color:gray;\n"
"font: 16pt \"Shiny Signature\", \"Arial\";\n"
"color: white;")
        self.btn_startApp.setObjectName("btn_startApp")
        self.btn_howToUse = QtWidgets.QPushButton(self.start_page)
        self.btn_howToUse.setGeometry(QtCore.QRect(1010, 30, 201, 41))
        self.btn_howToUse.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_howToUse.setObjectName("btn_howToUse")
        self.frame_6 = QtWidgets.QFrame(self.start_page)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 321, 711))
        self.frame_6.setStyleSheet("background-color:white")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_ico_bear.raise_()
        self.btn_startApp.raise_()
        self.frame_6.raise_()
        self.btn_howToUse.raise_()
        self.stackedWidget.addWidget(self.start_page)
        self.howToUse_page = QtWidgets.QWidget()
        self.howToUse_page.setObjectName("howToUse_page")
        self.text1_3 = QtWidgets.QPlainTextEdit(self.howToUse_page)
        self.text1_3.setGeometry(QtCore.QRect(40, 40, 191, 31))
        self.text1_3.setObjectName("text1_3")
        self.frame_14 = QtWidgets.QFrame(self.howToUse_page)
        self.frame_14.setGeometry(QtCore.QRect(920, 180, 201, 461))
        self.frame_14.setStyleSheet("background-color:lightyellow")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.stackedWidget.addWidget(self.howToUse_page)
        self.insert_page = QtWidgets.QWidget()
        self.insert_page.setAcceptDrops(True)
        self.insert_page.setStyleSheet("background-color:white")
        self.insert_page.setObjectName("insert_page")
        self.btn_chooseImage = QtWidgets.QPushButton(self.insert_page)
        self.btn_chooseImage.setGeometry(QtCore.QRect(280, 450, 211, 51))
        self.btn_chooseImage.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"background-color: none;")
        self.btn_chooseImage.setObjectName("btn_chooseImage")
        self.frame_dragDrop = QtWidgets.QFrame(self.insert_page)
        self.frame_dragDrop.setGeometry(QtCore.QRect(170, 130, 431, 301))
        self.frame_dragDrop.setAcceptDrops(True)
        self.frame_dragDrop.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_dragDrop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dragDrop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dragDrop.setObjectName("frame_dragDrop")
        self.insertPage_cartoonImage = QtWidgets.QLabel(self.frame_dragDrop)
        self.insertPage_cartoonImage.setGeometry(QtCore.QRect(10, 10, 411, 281))
        self.insertPage_cartoonImage.setAcceptDrops(True)
        self.insertPage_cartoonImage.setAutoFillBackground(False)
        self.insertPage_cartoonImage.setStyleSheet("background-color:white;\n"
"border-radius: 0;\n"
"border: 2px dashed gray;\n"
"font-size: 11pt;\n"
"color: gray;")
        self.insertPage_cartoonImage.setScaledContents(True)
        self.insertPage_cartoonImage.setObjectName("insertPage_cartoonImage")
        self.text1 = QtWidgets.QPlainTextEdit(self.insert_page)
        self.text1.setGeometry(QtCore.QRect(30, 20, 104, 31))
        self.text1.setObjectName("text1")
        self.btn_confirmImageVideo = QtWidgets.QPushButton(self.insert_page)
        self.btn_confirmImageVideo.setGeometry(QtCore.QRect(710, 580, 331, 61))
        self.btn_confirmImageVideo.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Shiny Signature\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_confirmImageVideo.setObjectName("btn_confirmImageVideo")
        self.frame_dragDrop_2 = QtWidgets.QFrame(self.insert_page)
        self.frame_dragDrop_2.setGeometry(QtCore.QRect(660, 130, 431, 301))
        self.frame_dragDrop_2.setAcceptDrops(True)
        self.frame_dragDrop_2.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_dragDrop_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dragDrop_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dragDrop_2.setObjectName("frame_dragDrop_2")
        self.insertPage_cartoonVideo = QtWidgets.QLabel(self.frame_dragDrop_2)
        self.insertPage_cartoonVideo.setGeometry(QtCore.QRect(10, 10, 411, 281))
        self.insertPage_cartoonVideo.setAcceptDrops(True)
        self.insertPage_cartoonVideo.setAutoFillBackground(False)
        self.insertPage_cartoonVideo.setStyleSheet("background-color:white;\n"
"border-radius: 0;\n"
"border: 2px dashed gray;\n"
"font-size: 11pt;\n"
"color: gray;")
        self.insertPage_cartoonVideo.setScaledContents(True)
        self.insertPage_cartoonVideo.setObjectName("insertPage_cartoonVideo")
        self.btn_chooseVideo = QtWidgets.QPushButton(self.insert_page)
        self.btn_chooseVideo.setGeometry(QtCore.QRect(770, 450, 211, 51))
        self.btn_chooseVideo.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"background-color: none;")
        self.btn_chooseVideo.setObjectName("btn_chooseVideo")
        self.btn_advanceSearch = QtWidgets.QPushButton(self.insert_page)
        self.btn_advanceSearch.setGeometry(QtCore.QRect(1020, 30, 201, 41))
        self.btn_advanceSearch.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_advanceSearch.setObjectName("btn_advanceSearch")
        self.btn_chooseImage.raise_()
        self.frame_dragDrop.raise_()
        self.btn_confirmImageVideo.raise_()
        self.frame_dragDrop_2.raise_()
        self.btn_chooseVideo.raise_()
        self.btn_advanceSearch.raise_()
        self.text1.raise_()
        self.stackedWidget.addWidget(self.insert_page)
        self.advanceSearch_page = QtWidgets.QWidget()
        self.advanceSearch_page.setObjectName("advanceSearch_page")
        self.text1_2 = QtWidgets.QPlainTextEdit(self.advanceSearch_page)
        self.text1_2.setGeometry(QtCore.QRect(50, 30, 171, 31))
        self.text1_2.setObjectName("text1_2")
        self.frame_16 = QtWidgets.QFrame(self.advanceSearch_page)
        self.frame_16.setGeometry(QtCore.QRect(410, 10, 171, 701))
        self.frame_16.setStyleSheet("background-color:lightyellow")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.stackedWidget.addWidget(self.advanceSearch_page)
        self.loading_page = QtWidgets.QWidget()
        self.loading_page.setObjectName("loading_page")
        self.label_10 = QtWidgets.QLabel(self.loading_page)
        self.label_10.setGeometry(QtCore.QRect(80, 50, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_buffer = QtWidgets.QLabel(self.loading_page)
        self.label_buffer.setGeometry(QtCore.QRect(390, 160, 201, 211))
        self.label_buffer.setText("")
        self.label_buffer.setObjectName("label_buffer")
        self.frame_17 = QtWidgets.QFrame(self.loading_page)
        self.frame_17.setGeometry(QtCore.QRect(710, 40, 171, 701))
        self.frame_17.setStyleSheet("background-color:lightyellow")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.stackedWidget.addWidget(self.loading_page)
        self.match_page = QtWidgets.QWidget()
        self.match_page.setStyleSheet("background-color:white")
        self.match_page.setObjectName("match_page")
        self.frame_3 = QtWidgets.QFrame(self.match_page)
        self.frame_3.setGeometry(QtCore.QRect(170, 130, 431, 301))
        self.frame_3.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.matchPage_inputImage = QtWidgets.QLabel(self.frame_3)
        self.matchPage_inputImage.setGeometry(QtCore.QRect(10, 10, 411, 241))
        self.matchPage_inputImage.setAutoFillBackground(False)
        self.matchPage_inputImage.setStyleSheet("background-color:white;\n"
"border-radius: 0;\n"
"")
        self.matchPage_inputImage.setText("")
        self.matchPage_inputImage.setScaledContents(True)
        self.matchPage_inputImage.setObjectName("matchPage_inputImage")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 411, 41))
        self.label_8.setStyleSheet("background-color:gray;\n"
"font: 10pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 150px;")
        self.label_8.setObjectName("label_8")
        self.btn_findMatchCharacter = QtWidgets.QPushButton(self.match_page)
        self.btn_findMatchCharacter.setGeometry(QtCore.QRect(730, 600, 291, 61))
        self.btn_findMatchCharacter.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Shiny Signature\", \"Arial\";\n"
"color: white;\n"
"")
        self.btn_findMatchCharacter.setObjectName("btn_findMatchCharacter")
        self.btn_changeImage = QtWidgets.QPushButton(self.match_page)
        self.btn_changeImage.setGeometry(QtCore.QRect(280, 450, 211, 51))
        self.btn_changeImage.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"background-color: none;")
        self.btn_changeImage.setObjectName("btn_changeImage")
        self.pushButton_notFoundPage = QtWidgets.QPushButton(self.match_page)
        self.pushButton_notFoundPage.setEnabled(False)
        self.pushButton_notFoundPage.setGeometry(QtCore.QRect(360, 610, 161, 41))
        self.pushButton_notFoundPage.setStyleSheet("background-color:pink;\n"
"font: 8pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"")
        self.pushButton_notFoundPage.setObjectName("pushButton_notFoundPage")
        self.text_2 = QtWidgets.QPlainTextEdit(self.match_page)
        self.text_2.setGeometry(QtCore.QRect(30, 20, 104, 31))
        self.text_2.setObjectName("text_2")
        self.frame_4 = QtWidgets.QFrame(self.match_page)
        self.frame_4.setGeometry(QtCore.QRect(660, 130, 431, 301))
        self.frame_4.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.matchPage_inputVideo = QtWidgets.QLabel(self.frame_4)
        self.matchPage_inputVideo.setGeometry(QtCore.QRect(10, 10, 411, 241))
        self.matchPage_inputVideo.setAutoFillBackground(False)
        self.matchPage_inputVideo.setStyleSheet("background-color:white;\n"
"border-radius: 0;\n"
"")
        self.matchPage_inputVideo.setText("")
        self.matchPage_inputVideo.setScaledContents(True)
        self.matchPage_inputVideo.setObjectName("matchPage_inputVideo")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(10, 250, 411, 41))
        self.label_9.setStyleSheet("background-color:gray;\n"
"font: 10pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 160px;")
        self.label_9.setObjectName("label_9")
        self.btn_changeVIdeo = QtWidgets.QPushButton(self.match_page)
        self.btn_changeVIdeo.setGeometry(QtCore.QRect(770, 450, 211, 51))
        self.btn_changeVIdeo.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"background-color: none;")
        self.btn_changeVIdeo.setObjectName("btn_changeVIdeo")
        self.pushButton_foundPage = QtWidgets.QPushButton(self.match_page)
        self.pushButton_foundPage.setEnabled(False)
        self.pushButton_foundPage.setGeometry(QtCore.QRect(180, 610, 161, 41))
        self.pushButton_foundPage.setStyleSheet("background-color:palegreen;\n"
"font: 8pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"")
        self.pushButton_foundPage.setObjectName("pushButton_foundPage")
        self.stackedWidget.addWidget(self.match_page)
        self.not_found_page = QtWidgets.QWidget()
        self.not_found_page.setStyleSheet("background-color:white")
        self.not_found_page.setObjectName("not_found_page")
        self.label = QtWidgets.QLabel(self.not_found_page)
        self.label.setGeometry(QtCore.QRect(50, 50, 1151, 51))
        self.label.setStyleSheet("background-color:pink;\n"
"border: 2px solid red;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label.setObjectName("label")
        self.btn_insertAnotherImage1 = QtWidgets.QPushButton(self.not_found_page)
        self.btn_insertAnotherImage1.setGeometry(QtCore.QRect(830, 620, 371, 61))
        self.btn_insertAnotherImage1.setStyleSheet("font: 12pt \"Shiny Signature\", \"Arial\";\n"
"background-color: none;")
        self.btn_insertAnotherImage1.setObjectName("btn_insertAnotherImage1")
        self.frame = QtWidgets.QFrame(self.not_found_page)
        self.frame.setGeometry(QtCore.QRect(830, 380, 371, 221))
        self.frame.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_inputImage1 = QtWidgets.QLabel(self.frame)
        self.label_inputImage1.setGeometry(QtCore.QRect(10, 10, 271, 161))
        self.label_inputImage1.setAutoFillBackground(False)
        self.label_inputImage1.setStyleSheet("background-color:white;\n"
"border-radius: 0;")
        self.label_inputImage1.setText("")
        self.label_inputImage1.setPixmap(QtGui.QPixmap("images/we bare bear sticker medium.png"))
        self.label_inputImage1.setScaledContents(True)
        self.label_inputImage1.setObjectName("label_inputImage1")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 271, 41))
        self.label_4.setStyleSheet("background-color:gray;\n"
"font: 9pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 80px;")
        self.label_4.setObjectName("label_4")
        self.frame_9 = QtWidgets.QFrame(self.not_found_page)
        self.frame_9.setGeometry(QtCore.QRect(830, 130, 371, 231))
        self.frame_9.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_20 = QtWidgets.QLabel(self.frame_9)
        self.label_20.setGeometry(QtCore.QRect(40, 80, 291, 61))
        self.label_20.setStyleSheet("\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: gray;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_20.setObjectName("label_20")
        self.label_6 = QtWidgets.QLabel(self.not_found_page)
        self.label_6.setGeometry(QtCore.QRect(50, 130, 751, 51))
        self.label_6.setStyleSheet("background-color:lightgray;\n"
"border: 2px solid gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.not_found_page)
        self.label_7.setGeometry(QtCore.QRect(50, 180, 751, 181))
        self.label_7.setStyleSheet("background-color:white;\n"
"border: 2px solid gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.frame_10 = QtWidgets.QFrame(self.not_found_page)
        self.frame_10.setGeometry(QtCore.QRect(170, 380, 511, 301))
        self.frame_10.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_22 = QtWidgets.QLabel(self.frame_10)
        self.label_22.setGeometry(QtCore.QRect(140, 120, 231, 61))
        self.label_22.setStyleSheet("\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: gray;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_22.setObjectName("label_22")
        self.label_3 = QtWidgets.QLabel(self.not_found_page)
        self.label_3.setGeometry(QtCore.QRect(80, 190, 71, 31))
        self.label_3.setStyleSheet("font-size: 12pt")
        self.label_3.setObjectName("label_3")
        self.frame.raise_()
        self.label.raise_()
        self.btn_insertAnotherImage1.raise_()
        self.frame_9.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.frame_10.raise_()
        self.label_3.raise_()
        self.stackedWidget.addWidget(self.not_found_page)
        self.found_page = QtWidgets.QWidget()
        self.found_page.setObjectName("found_page")
        self.label_15 = QtWidgets.QLabel(self.found_page)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 1221, 41))
        self.label_15.setStyleSheet("background-color:palegreen;\n"
"border: 2px solid green;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label_15.setObjectName("label_15")
        self.btn_insertAnotherImage2 = QtWidgets.QPushButton(self.found_page)
        self.btn_insertAnotherImage2.setGeometry(QtCore.QRect(870, 620, 371, 61))
        self.btn_insertAnotherImage2.setStyleSheet("font: 12pt \"Shiny Signature\", \"Arial\";\n"
"background-color: none;")
        self.btn_insertAnotherImage2.setObjectName("btn_insertAnotherImage2")
        self.tabWidget_foundPage = QtWidgets.QTabWidget(self.found_page)
        self.tabWidget_foundPage.setGeometry(QtCore.QRect(20, 80, 1221, 521))
        self.tabWidget_foundPage.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_foundPage.setObjectName("tabWidget_foundPage")
        self.tab_frame_table = QtWidgets.QWidget()
        self.tab_frame_table.setObjectName("tab_frame_table")
        self.frame_8 = QtWidgets.QFrame(self.tab_frame_table)
        self.frame_8.setGeometry(QtCore.QRect(710, 110, 491, 331))
        self.frame_8.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frameFound = QtWidgets.QLabel(self.frame_8)
        self.frameFound.setGeometry(QtCore.QRect(10, 10, 471, 271))
        self.frameFound.setAutoFillBackground(False)
        self.frameFound.setStyleSheet("background-color:white;\n"
"border-radius: 0;\n"
"font-size: 11pt;\n"
"color: gray;")
        self.frameFound.setScaledContents(True)
        self.frameFound.setObjectName("frameFound")
        self.label_frameTitle = QtWidgets.QLabel(self.frame_8)
        self.label_frameTitle.setGeometry(QtCore.QRect(10, 280, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold,Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_frameTitle.setFont(font)
        self.label_frameTitle.setStyleSheet("background-color:gray;\n"
"font: 10pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_frameTitle.setObjectName("label_frameTitle")
        self.tableFrameFound = QtWidgets.QTableWidget(self.tab_frame_table)
        self.tableFrameFound.setGeometry(QtCore.QRect(20, 50, 671, 391))
        self.tableFrameFound.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableFrameFound.setAlternatingRowColors(True)
        self.tableFrameFound.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableFrameFound.setObjectName("tableFrameFound")
        self.tableFrameFound.setColumnCount(3)
        self.tableFrameFound.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableFrameFound.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFrameFound.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFrameFound.setHorizontalHeaderItem(2, item)
        self.tableFrameFound.horizontalHeader().setDefaultSectionSize(189)
        self.tableFrameFound.verticalHeader().setCascadingSectionResizes(False)
        self.label_characterName = QtWidgets.QLabel(self.tab_frame_table)
        self.label_characterName.setGeometry(QtCore.QRect(710, 50, 491, 51))
        self.label_characterName.setStyleSheet("background-color:palegreen;\n"
"border: 2px solid green;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:180px;\n"
"border-radius: 6px;\n"
"")
        self.label_characterName.setObjectName("label_characterName")
        self.tabWidget_foundPage.addTab(self.tab_frame_table, "")
        self.tab_video_play = QtWidgets.QWidget()
        self.tab_video_play.setObjectName("tab_video_play")
        self.frame_11 = QtWidgets.QFrame(self.tab_video_play)
        self.frame_11.setGeometry(QtCore.QRect(100, 30, 471, 311))
        self.frame_11.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_videoPlay = QtWidgets.QLabel(self.frame_11)
        self.label_videoPlay.setGeometry(QtCore.QRect(10, 10, 451, 221))
        self.label_videoPlay.setStyleSheet("background-color:white; border-radius: 0;")
        self.label_videoPlay.setObjectName("label_videoPlay")
        self.horizontalSlider_video = QtWidgets.QSlider(self.frame_11)
        self.horizontalSlider_video.setGeometry(QtCore.QRect(80, 270, 381, 21))
        self.horizontalSlider_video.setStyleSheet("background-color:white;\n"
" border-radius:0;")
        self.horizontalSlider_video.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_video.setObjectName("horizontalSlider_video")
        self.pushButton_playVideo = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_playVideo.setGeometry(QtCore.QRect(10, 260, 61, 41))
        self.pushButton_playVideo.setStyleSheet("background-color:white; border-radius:5px;")
        self.pushButton_playVideo.setObjectName("pushButton_playVideo")
        self.pushButton_pauseVideo = QtWidgets.QPushButton(self.tab_video_play)
        self.pushButton_pauseVideo.setGeometry(QtCore.QRect(610, 80, 93, 28))
        self.pushButton_pauseVideo.setObjectName("pushButton_pauseVideo")
        self.pushButton_runVideoDirectly = QtWidgets.QPushButton(self.tab_video_play)
        self.pushButton_runVideoDirectly.setGeometry(QtCore.QRect(610, 120, 93, 28))
        self.pushButton_runVideoDirectly.setObjectName("pushButton_runVideoDirectly")
        self.label_23 = QtWidgets.QLabel(self.tab_video_play)
        self.label_23.setGeometry(QtCore.QRect(160, 350, 161, 41))
        self.label_23.setStyleSheet("background-color:gray;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 30px;")
        self.label_23.setObjectName("label_23")
        self.text_4 = QtWidgets.QPlainTextEdit(self.tab_video_play)
        self.text_4.setGeometry(QtCore.QRect(330, 350, 104, 31))
        self.text_4.setObjectName("text_4")
        self.frame_12 = QtWidgets.QFrame(self.tab_video_play)
        self.frame_12.setGeometry(QtCore.QRect(590, 190, 381, 251))
        self.frame_12.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.graphicsView_video = QtWidgets.QGraphicsView(self.frame_12)
        self.graphicsView_video.setGeometry(QtCore.QRect(10, 10, 361, 231))
        self.graphicsView_video.setStyleSheet("background-color:lightyellow")
        self.graphicsView_video.setObjectName("graphicsView_video")
        self.tabWidget_foundPage.addTab(self.tab_video_play, "")
        self.tab_statistics = QtWidgets.QWidget()
        self.tab_statistics.setObjectName("tab_statistics")
        self.frame_7 = QtWidgets.QFrame(self.tab_statistics)
        self.frame_7.setGeometry(QtCore.QRect(580, 40, 291, 201))
        self.frame_7.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.inputImage_found = QtWidgets.QLabel(self.frame_7)
        self.inputImage_found.setGeometry(QtCore.QRect(10, 10, 271, 151))
        self.inputImage_found.setAutoFillBackground(False)
        self.inputImage_found.setStyleSheet("background-color:white;\n"
"border-radius: 0;")
        self.inputImage_found.setText("")
        self.inputImage_found.setScaledContents(True)
        self.inputImage_found.setObjectName("inputImage_found")
        self.label_accuracy = QtWidgets.QLabel(self.frame_7)
        self.label_accuracy.setGeometry(QtCore.QRect(10, 160, 271, 31))
        self.label_accuracy.setStyleSheet("background-color:gray;\n"
"font: 9pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 60px;")
        self.label_accuracy.setObjectName("label_accuracy")
        self.frame_13 = QtWidgets.QFrame(self.tab_statistics)
        self.frame_13.setGeometry(QtCore.QRect(40, 330, 1111, 161))
        self.frame_13.setStyleSheet("background-color:lightgray;\n"
"border-radius: 10px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.inputImage_found_2 = QtWidgets.QLabel(self.frame_13)
        self.inputImage_found_2.setGeometry(QtCore.QRect(10, 10, 241, 141))
        self.inputImage_found_2.setAutoFillBackground(False)
        self.inputImage_found_2.setStyleSheet("background-color:white;\n"
"border-radius: 0;")
        self.inputImage_found_2.setText("")
        self.inputImage_found_2.setScaledContents(True)
        self.inputImage_found_2.setObjectName("inputImage_found_2")
        self.label_characterName2 = QtWidgets.QLabel(self.frame_13)
        self.label_characterName2.setGeometry(QtCore.QRect(260, 10, 191, 51))
        self.label_characterName2.setStyleSheet("background-color:palegreen;\n"
"border: 2px solid green;\n"
"font: 12pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"padding-left:10px;\n"
"")
        self.label_characterName2.setObjectName("label_characterName2")
        self.label_accuracy_2 = QtWidgets.QLabel(self.frame_13)
        self.label_accuracy_2.setGeometry(QtCore.QRect(260, 50, 191, 101))
        self.label_accuracy_2.setStyleSheet("background-color:gray;\n"
"font: 10pt \"Arial Rounded MT Bold\", \"Arial\";\n"
"color: white;\n"
"border-radius: 0;\n"
"align:center;\n"
"padding-left: 10px;")
        self.label_accuracy_2.setObjectName("label_accuracy_2")
        self.label_accuracy_2.raise_()
        self.inputImage_found_2.raise_()
        self.label_characterName2.raise_()
        self.tabWidget_foundPage.addTab(self.tab_statistics, "")
        self.label_15.raise_()
        self.tabWidget_foundPage.raise_()
        self.btn_insertAnotherImage2.raise_()
        self.stackedWidget.addWidget(self.found_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget_foundPage.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cartoon Character Image Retrieval"))
        self.btn_startApp.setText(_translate("MainWindow", "START APPLICATION"))
        self.btn_howToUse.setText(_translate("MainWindow", "How To Use"))
        self.text1_3.setPlainText(_translate("MainWindow", "how to use page"))
        self.btn_chooseImage.setText(_translate("MainWindow", "Choose Image"))
        self.insertPage_cartoonImage.setText(_translate("MainWindow", "              Choose an image to search"))
        self.text1.setPlainText(_translate("MainWindow", "insert page"))
        self.btn_confirmImageVideo.setText(_translate("MainWindow", "CONFIRM IMAGE AND VIDEO"))
        self.insertPage_cartoonVideo.setText(_translate("MainWindow", "                Choose a video to search"))
        self.btn_chooseVideo.setText(_translate("MainWindow", "Choose Video"))
        self.btn_advanceSearch.setText(_translate("MainWindow", "Advance Search"))
        self.text1_2.setPlainText(_translate("MainWindow", "advance search page"))
        self.label_10.setText(_translate("MainWindow", "loading page"))
        self.label_8.setText(_translate("MainWindow", "Input Image"))
        self.btn_findMatchCharacter.setText(_translate("MainWindow", "FIND MATCH CHARACTER"))
        self.btn_changeImage.setText(_translate("MainWindow", "Change Image"))
        self.pushButton_notFoundPage.setText(_translate("MainWindow", "Not Found page"))
        self.text_2.setPlainText(_translate("MainWindow", "match page"))
        self.label_9.setText(_translate("MainWindow", "Input Video"))
        self.btn_changeVIdeo.setText(_translate("MainWindow", "Change Video"))
        self.pushButton_foundPage.setText(_translate("MainWindow", "Found page"))
        self.label.setText(_translate("MainWindow", "Character Not Found"))
        self.btn_insertAnotherImage1.setText(_translate("MainWindow", "INSERT ANOTHER MATCH"))
        self.label_4.setText(_translate("MainWindow", "Input Image"))
        self.label_20.setText(_translate("MainWindow", "No Retrieved Character"))
        self.label_6.setText(_translate("MainWindow", "No Appearance Time"))
        self.label_22.setText(_translate("MainWindow", "No Video Match"))
        self.label_3.setText(_translate("MainWindow", "_"))
        self.label_15.setText(_translate("MainWindow", "Character Found"))
        self.btn_insertAnotherImage2.setText(_translate("MainWindow", "INSERT ANOTHER MATCH"))
        self.frameFound.setText(_translate("MainWindow", "             Double click on Data to change Frame"))
        self.label_frameTitle.setText(_translate("MainWindow", "      Time : 123.000 sec          Accuracy : 10.10%"))
        item = self.tableFrameFound.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Frame Name"))
        item = self.tableFrameFound.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time Appearance"))
        item = self.tableFrameFound.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Accuracy"))
        self.label_characterName.setText(_translate("MainWindow", "doraemon"))
        self.tabWidget_foundPage.setTabText(self.tabWidget_foundPage.indexOf(self.tab_frame_table), _translate("MainWindow", "Video Frames"))
        self.label_videoPlay.setText(_translate("MainWindow", "Video"))
        self.pushButton_playVideo.setText(_translate("MainWindow", "Play"))
        self.pushButton_pauseVideo.setText(_translate("MainWindow", "Pause"))
        self.pushButton_runVideoDirectly.setText(_translate("MainWindow", "Play Video"))
        self.label_23.setText(_translate("MainWindow", "Video Match"))
        self.text_4.setPlainText(_translate("MainWindow", "video play"))
        self.tabWidget_foundPage.setTabText(self.tabWidget_foundPage.indexOf(self.tab_video_play), _translate("MainWindow", "Play Video"))
        self.label_accuracy.setText(_translate("MainWindow", "Accuracy : 88.88%"))
        self.label_characterName2.setText(_translate("MainWindow", "doraemon"))
        self.label_accuracy_2.setText(_translate("MainWindow", "Input Image \n"
"Accuracy : 88.88%"))
        self.tabWidget_foundPage.setTabText(self.tabWidget_foundPage.indexOf(self.tab_statistics), _translate("MainWindow", "Character Statistics"))
