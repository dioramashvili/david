# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(555, 556)
        MainWindow.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 551, 481))
        self.stackedWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.shape_group = QtWidgets.QGroupBox(self.main_page)
        self.shape_group.setGeometry(QtCore.QRect(120, 70, 120, 171))
        self.shape_group.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.shape_group.setObjectName("shape_group")
        self.triangle = QtWidgets.QRadioButton(self.shape_group)
        self.triangle.setGeometry(QtCore.QRect(20, 130, 91, 23))
        self.triangle.setObjectName("triangle")
        self.trapezoid = QtWidgets.QRadioButton(self.shape_group)
        self.trapezoid.setGeometry(QtCore.QRect(20, 100, 91, 23))
        self.trapezoid.setObjectName("trapezoid")
        self.circle = QtWidgets.QRadioButton(self.shape_group)
        self.circle.setGeometry(QtCore.QRect(20, 40, 91, 23))
        self.circle.setObjectName("circle")
        self.rectangle = QtWidgets.QRadioButton(self.shape_group)
        self.rectangle.setGeometry(QtCore.QRect(20, 70, 91, 23))
        self.rectangle.setObjectName("rectangle")
        self.color_group = QtWidgets.QGroupBox(self.main_page)
        self.color_group.setGeometry(QtCore.QRect(310, 70, 120, 171))
        self.color_group.setStyleSheet("background-color: rgb(192, 97, 203);")
        self.color_group.setObjectName("color_group")
        self.yellow = QtWidgets.QRadioButton(self.color_group)
        self.yellow.setGeometry(QtCore.QRect(20, 130, 91, 23))
        self.yellow.setObjectName("yellow")
        self.red = QtWidgets.QRadioButton(self.color_group)
        self.red.setGeometry(QtCore.QRect(20, 100, 91, 23))
        self.red.setObjectName("red")
        self.blue = QtWidgets.QRadioButton(self.color_group)
        self.blue.setGeometry(QtCore.QRect(20, 40, 91, 23))
        self.blue.setObjectName("blue")
        self.green = QtWidgets.QRadioButton(self.color_group)
        self.green.setGeometry(QtCore.QRect(20, 70, 91, 23))
        self.green.setObjectName("green")
        self.select = QtWidgets.QPushButton(self.main_page)
        self.select.setGeometry(QtCore.QRect(230, 280, 89, 25))
        self.select.setStyleSheet("color: rgb(255, 255, 255);")
        self.select.setObjectName("select")
        self.stackedWidget.addWidget(self.main_page)
        self.circle_page = QtWidgets.QWidget()
        self.circle_page.setObjectName("circle_page")
        self.groupBox_1 = QtWidgets.QGroupBox(self.circle_page)
        self.groupBox_1.setGeometry(QtCore.QRect(200, 100, 201, 241))
        self.groupBox_1.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.groupBox_1.setTitle("")
        self.groupBox_1.setObjectName("groupBox_1")
        self.splitter = QtWidgets.QSplitter(self.groupBox_1)
        self.splitter.setGeometry(QtCore.QRect(0, 10, 171, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.r = QtWidgets.QDoubleSpinBox(self.splitter)
        self.r.setObjectName("r")
        self.splitter_5 = QtWidgets.QSplitter(self.groupBox_1)
        self.splitter_5.setGeometry(QtCore.QRect(0, 60, 171, 71))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_9 = QtWidgets.QLabel(self.splitter_5)
        self.label_9.setObjectName("label_9")
        self.c_area = QtWidgets.QLCDNumber(self.splitter_5)
        self.c_area.setObjectName("c_area")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox_1)
        self.splitter_3.setGeometry(QtCore.QRect(0, 140, 171, 71))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        self.label_3.setObjectName("label_3")
        self.c_length = QtWidgets.QLCDNumber(self.splitter_3)
        self.c_length.setObjectName("c_length")
        self.stackedWidget.addWidget(self.circle_page)
        self.rectangle_page = QtWidgets.QWidget()
        self.rectangle_page.setObjectName("rectangle_page")
        self.groupBox_2 = QtWidgets.QGroupBox(self.rectangle_page)
        self.groupBox_2.setGeometry(QtCore.QRect(110, 120, 126, 141))
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setStyleSheet("background-color: rgb(87, 227, 137);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.splitter_25 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_25.setGeometry(QtCore.QRect(10, 90, 106, 25))
        self.splitter_25.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_25.setObjectName("splitter_25")
        self.label_25 = QtWidgets.QLabel(self.splitter_25)
        self.label_25.setObjectName("label_25")
        self.r_b = QtWidgets.QDoubleSpinBox(self.splitter_25)
        self.r_b.setObjectName("r_b")
        self.splitter_27 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_27.setGeometry(QtCore.QRect(10, 50, 106, 25))
        self.splitter_27.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_27.setObjectName("splitter_27")
        self.label_27 = QtWidgets.QLabel(self.splitter_27)
        self.label_27.setObjectName("label_27")
        self.r_a = QtWidgets.QDoubleSpinBox(self.splitter_27)
        self.r_a.setObjectName("r_a")
        self.groupBox_3 = QtWidgets.QGroupBox(self.rectangle_page)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 120, 191, 161))
        self.groupBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_3.setStyleSheet("background-color: rgb(87, 227, 137);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.r_p = QtWidgets.QLCDNumber(self.groupBox_3)
        self.r_p.setGeometry(QtCore.QRect(90, 90, 71, 41))
        self.r_p.setObjectName("r_p")
        self.label_28 = QtWidgets.QLabel(self.groupBox_3)
        self.label_28.setGeometry(QtCore.QRect(10, 90, 81, 41))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(10, 30, 81, 41))
        self.label_29.setObjectName("label_29")
        self.r_area = QtWidgets.QLCDNumber(self.groupBox_3)
        self.r_area.setGeometry(QtCore.QRect(90, 30, 71, 41))
        self.r_area.setObjectName("r_area")
        self.stackedWidget.addWidget(self.rectangle_page)
        self.triangle_page = QtWidgets.QWidget()
        self.triangle_page.setObjectName("triangle_page")
        self.groupBox_4 = QtWidgets.QGroupBox(self.triangle_page)
        self.groupBox_4.setGeometry(QtCore.QRect(130, 100, 126, 215))
        self.groupBox_4.setStyleSheet("background-color: rgb(237, 51, 59);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.splitter_11 = QtWidgets.QSplitter(self.groupBox_4)
        self.splitter_11.setGeometry(QtCore.QRect(10, 90, 106, 25))
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.label_5 = QtWidgets.QLabel(self.splitter_11)
        self.label_5.setObjectName("label_5")
        self.side2 = QtWidgets.QDoubleSpinBox(self.splitter_11)
        self.side2.setObjectName("side2")
        self.splitter_12 = QtWidgets.QSplitter(self.groupBox_4)
        self.splitter_12.setGeometry(QtCore.QRect(10, 140, 106, 25))
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName("splitter_12")
        self.label_6 = QtWidgets.QLabel(self.splitter_12)
        self.label_6.setObjectName("label_6")
        self.side3 = QtWidgets.QDoubleSpinBox(self.splitter_12)
        self.side3.setObjectName("side3")
        self.splitter_13 = QtWidgets.QSplitter(self.groupBox_4)
        self.splitter_13.setGeometry(QtCore.QRect(10, 40, 106, 25))
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName("splitter_13")
        self.label_4 = QtWidgets.QLabel(self.splitter_13)
        self.label_4.setObjectName("label_4")
        self.side1 = QtWidgets.QDoubleSpinBox(self.splitter_13)
        self.side1.setObjectName("side1")
        self.groupBox_5 = QtWidgets.QGroupBox(self.triangle_page)
        self.groupBox_5.setGeometry(QtCore.QRect(310, 130, 191, 161))
        self.groupBox_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_5.setStyleSheet("background-color: rgb(237, 51, 59);")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.t_p = QtWidgets.QLCDNumber(self.groupBox_5)
        self.t_p.setGeometry(QtCore.QRect(90, 90, 71, 41))
        self.t_p.setObjectName("t_p")
        self.label_30 = QtWidgets.QLabel(self.groupBox_5)
        self.label_30.setGeometry(QtCore.QRect(10, 90, 81, 41))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.groupBox_5)
        self.label_31.setGeometry(QtCore.QRect(10, 30, 81, 41))
        self.label_31.setObjectName("label_31")
        self.t_area = QtWidgets.QLCDNumber(self.groupBox_5)
        self.t_area.setGeometry(QtCore.QRect(90, 30, 71, 41))
        self.t_area.setObjectName("t_area")
        self.stackedWidget.addWidget(self.triangle_page)
        self.trapezoid_page = QtWidgets.QWidget()
        self.trapezoid_page.setObjectName("trapezoid_page")
        self.groupBox_6 = QtWidgets.QGroupBox(self.trapezoid_page)
        self.groupBox_6.setGeometry(QtCore.QRect(120, 80, 141, 261))
        self.groupBox_6.setStyleSheet("background-color: rgb(248, 228, 92);")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.splitter_22 = QtWidgets.QSplitter(self.groupBox_6)
        self.splitter_22.setGeometry(QtCore.QRect(10, 80, 106, 25))
        self.splitter_22.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_22.setObjectName("splitter_22")
        self.label_20 = QtWidgets.QLabel(self.splitter_22)
        self.label_20.setObjectName("label_20")
        self.tr_b = QtWidgets.QDoubleSpinBox(self.splitter_22)
        self.tr_b.setObjectName("tr_b")
        self.splitter_23 = QtWidgets.QSplitter(self.groupBox_6)
        self.splitter_23.setGeometry(QtCore.QRect(10, 200, 106, 25))
        self.splitter_23.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_23.setObjectName("splitter_23")
        self.label_21 = QtWidgets.QLabel(self.splitter_23)
        self.label_21.setObjectName("label_21")
        self.tr_h = QtWidgets.QDoubleSpinBox(self.splitter_23)
        self.tr_h.setObjectName("tr_h")
        self.splitter_24 = QtWidgets.QSplitter(self.groupBox_6)
        self.splitter_24.setGeometry(QtCore.QRect(10, 40, 106, 25))
        self.splitter_24.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_24.setObjectName("splitter_24")
        self.splitter_26 = QtWidgets.QSplitter(self.splitter_24)
        self.splitter_26.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_26.setObjectName("splitter_26")
        self.label_26 = QtWidgets.QLabel(self.splitter_26)
        self.label_26.setObjectName("label_26")
        self.tr_a = QtWidgets.QDoubleSpinBox(self.splitter_26)
        self.tr_a.setObjectName("tr_a")
        self.splitter_28 = QtWidgets.QSplitter(self.groupBox_6)
        self.splitter_28.setGeometry(QtCore.QRect(10, 120, 106, 25))
        self.splitter_28.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_28.setObjectName("splitter_28")
        self.label_34 = QtWidgets.QLabel(self.splitter_28)
        self.label_34.setObjectName("label_34")
        self.tr_side_1 = QtWidgets.QDoubleSpinBox(self.splitter_28)
        self.tr_side_1.setObjectName("tr_side_1")
        self.splitter_29 = QtWidgets.QSplitter(self.groupBox_6)
        self.splitter_29.setGeometry(QtCore.QRect(10, 160, 106, 25))
        self.splitter_29.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_29.setObjectName("splitter_29")
        self.label_35 = QtWidgets.QLabel(self.splitter_29)
        self.label_35.setObjectName("label_35")
        self.tr_side_2 = QtWidgets.QDoubleSpinBox(self.splitter_29)
        self.tr_side_2.setObjectName("tr_side_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.trapezoid_page)
        self.groupBox_7.setGeometry(QtCore.QRect(310, 140, 191, 161))
        self.groupBox_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_7.setStyleSheet("background-color: rgb(248, 228, 92);")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_7.setObjectName("groupBox_7")
        self.tr_p = QtWidgets.QLCDNumber(self.groupBox_7)
        self.tr_p.setGeometry(QtCore.QRect(90, 90, 71, 41))
        self.tr_p.setObjectName("tr_p")
        self.label_32 = QtWidgets.QLabel(self.groupBox_7)
        self.label_32.setGeometry(QtCore.QRect(10, 90, 81, 41))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox_7)
        self.label_33.setGeometry(QtCore.QRect(10, 30, 81, 41))
        self.label_33.setObjectName("label_33")
        self.tr_area = QtWidgets.QLCDNumber(self.groupBox_7)
        self.tr_area.setGeometry(QtCore.QRect(90, 30, 71, 41))
        self.tr_area.setObjectName("tr_area")
        self.stackedWidget.addWidget(self.trapezoid_page)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(200, 10, 89, 25))
        self.backButton.setObjectName("backButton")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setGeometry(QtCore.QRect(290, 10, 89, 25))
        self.calculate.setObjectName("calculate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 555, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.shape_group.setTitle(_translate("MainWindow", "   Choose shape"))
        self.triangle.setText(_translate("MainWindow", "Triangle"))
        self.trapezoid.setText(_translate("MainWindow", "Trapezoid"))
        self.circle.setText(_translate("MainWindow", "Circle"))
        self.rectangle.setText(_translate("MainWindow", "Rectangle"))
        self.color_group.setTitle(_translate("MainWindow", "   Choose color"))
        self.yellow.setText(_translate("MainWindow", "Yellow"))
        self.red.setText(_translate("MainWindow", "Red"))
        self.blue.setText(_translate("MainWindow", "Blue"))
        self.green.setText(_translate("MainWindow", "Green"))
        self.select.setText(_translate("MainWindow", "Select"))
        self.label.setText(_translate("MainWindow", "   Radius"))
        self.label_9.setText(_translate("MainWindow", "     Area"))
        self.label_3.setText(_translate("MainWindow", "   Length"))
        self.label_25.setText(_translate("MainWindow", "    b"))
        self.label_27.setText(_translate("MainWindow", "    a"))
        self.label_28.setText(_translate("MainWindow", "Perimeter"))
        self.label_29.setText(_translate("MainWindow", "      Area"))
        self.label_5.setText(_translate("MainWindow", "Side 2"))
        self.label_6.setText(_translate("MainWindow", "Side 3"))
        self.label_4.setText(_translate("MainWindow", "Side 1"))
        self.label_30.setText(_translate("MainWindow", "Perimeter"))
        self.label_31.setText(_translate("MainWindow", "      Area"))
        self.label_20.setText(_translate("MainWindow", "base 2"))
        self.label_21.setText(_translate("MainWindow", "   h"))
        self.label_26.setText(_translate("MainWindow", "base 1"))
        self.label_34.setText(_translate("MainWindow", "side 1"))
        self.label_35.setText(_translate("MainWindow", "side 2"))
        self.label_32.setText(_translate("MainWindow", "Perimeter"))
        self.label_33.setText(_translate("MainWindow", "      Area"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.calculate.setText(_translate("MainWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
