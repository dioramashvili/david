import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from calculator import Ui_MainWindow
import math


class MainWidget(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.ui = loadUi("ui/calculator.ui", self)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.main_page)
        self.select.clicked.connect(self.selects)
        self.index = -1
        self.color = ''
        self.backButton.clicked.connect(self.back)
        self.calculate.clicked.connect(self.calc)

        self.radio_buttons = {'circle': (self.ui.circle, 1),
                              'rect': (self.ui.rectangle, 2),
                              'triangle': (self.ui.triangle, 3),
                              'trap': (self.ui.trapezoid, 4)}

    def back(self):
        self.stackedWidget.setCurrentWidget(self.main_page)
        self.index = -1

    def selects(self):
        self.select_shape()
        self.get_checked_color()
        self.change_color()

    def calc(self):
        match self.index:
            case 1:
                self.calculate_circle()
            case 2:
                self.calculate_rect()
            case 3:
                self.calculate_triangle()
            case 4:
                self.calculate_trap()

    def select_shape(self):
        for rb in self.radio_buttons.items():
            if rb[1][0].isChecked():
                self.stackedWidget.setCurrentIndex(rb[1][1])
                self.index = rb[1][1]
                break

    def get_checked_color(self):
        for x in (self.blue, self.red, self.yellow, self.green):
            if x.isChecked():
                self.color = x
                break

    def change_color(self):
        if self.index == -1 and self.color == self.blue:
            self.shape_group.setStyleSheet("background-color: rgb(98, 160, 234);")
            self.color_group.setStyleSheet("background-color: rgb(98, 160, 234);")
        elif self.index == -1 and self.color == self.red:
            self.shape_group.setStyleSheet("background-color: rgb(237, 51, 59);")
            self.color_group.setStyleSheet("background-color: rgb(237, 51, 59);")
        elif self.index == -1 and self.color == self.yellow:
            self.shape_group.setStyleSheet("background-color: rgb(248, 228, 92);")
            self.color_group.setStyleSheet("background-color: rgb(248, 228, 92);")
        elif self.index == -1 and self.color == self.green:
            self.shape_group.setStyleSheet("background-color: rgb(87, 227, 137);")
            self.color_group.setStyleSheet("background-color: rgb(87, 227, 137);")
        elif self.color == self.blue:
            for i in range(1, 8):
                exec(f'self.groupBox_{i}.setStyleSheet("background-color: rgb(98, 160, 234);")')
        elif self.color == self.red:
            for i in range(1, 8):
                exec(f'self.groupBox_{i}.setStyleSheet("background-color: rgb(237, 51, 59);")')
        elif self.color == self.yellow:
            for i in range(1, 8):
                exec(f'self.groupBox_{i}.setStyleSheet("background-color: rgb(248, 228, 92);")')
        elif self.color == self.green:
            for i in range(1, 8):
                exec(f'self.groupBox_{i}.setStyleSheet("background-color: rgb(87, 227, 137);")')

    def calculate_circle(self):
        radius = float(self.r.text().replace(',', '.'))

        if radius == 0:
            self.c_area.display(-1)
            self.c_length.display(-1)
        else:
            self.c_area.display(math.pi * (radius ** 2))
            self.c_length.display(2 * math.pi * radius)

    def calculate_rect(self):
        a = float(self.r_a.text().replace(',', '.'))
        b = float(self.r_b.text().replace(',', '.'))

        if 0 in (a, b):
            self.r_area.display(-1)
            self.r_p.display(-1)
        else:
            self.r_area.display(a * b)
            self.r_p.display(2 * (a + b))

    def calculate_triangle(self):
        a = float(self.side1.text().replace(',', '.'))
        b = float(self.side2.text().replace(',', '.'))
        c = float(self.side3.text().replace(',', '.'))

        if 0 in (a, b, c):
            self.t_area.display(-1)
            self.t_p.display(-1)
        else:
            p = a + b + c
            s = p / 2
            self.t_area.display(math.sqrt(s*(s-a)*(s-b)*(s-c)))
            self.t_p.display(p)

    def calculate_trap(self):
        a = float(self.tr_a.text().replace(',', '.'))
        b = float(self.tr_b.text().replace(',', '.'))
        c = float(self.tr_side_1.text().replace(',', '.'))
        d = float(self.tr_side_2.text().replace(',', '.'))
        h = float(self.tr_h.text().replace(',', '.'))

        if 0 in (a, b, c, d, h):
            self.tr_area.display(-1)
            self.tr_p.display(-1)
        else:
            p = a + b + c + d
            self.tr_area.display((a+b)/2*h)
            self.tr_p.display(p)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()

    sys.exit(app.exec_())
