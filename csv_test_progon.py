import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QComboBox, QTableView, QVBoxLayout, QTableWidget, QFileDialog, QTableWidgetItem, QPlainTextEdit
from PyQt5.QtGui import QFont, QIcon, QStandardItemModel, QStandardItem, QColor
from PyQt5.QtCore import QRect
from subprocess import Popen
import csv


second_style = ("background-color: rgb(100, 255, 100);\n"
"border-radius: 0px;\n"
"\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(191, 191, 191);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(1, 5)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)")

first_style = ("background-color: rgb(255, 150, 150);\n"
"border-radius: 0px;\n"
"\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(191, 191, 191);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(1, 5)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)")

third_style = ("background-color: rgb(255, 255, 0);\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(191, 191, 191);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)")



class FirstForm(QWidget):

    def __init__(self):
        super(FirstForm, self).__init__()
        self.ecran()

    def ecran(self, tablica=False, sec_tablica=False):
        self.bkgrnd = """
            QWidget {
                background-image: url("boroda.jpg");
                background-repeat: no-repeat; 
                background-position: center;
            }
        """
        self.bckgd_space = QPlainTextEdit(self)
        self.bckgd_space.resize(1000, 1000)
        self.bckgd_space.setStyleSheet(self.bkgrnd)
        self.setGeometry(100, 100, 1000, 1000)
        self.zanovo_baton = QPushButton('Заново', self)
        self.zanovo_baton.setGeometry(100, 370, 200, 30)
        self.zanovo_baton.move(0, 30)
        self.zanovo_baton.clicked.connect(self.again_func)
        self.zanovo_baton.resize(150, 30)
        self.zanovo_baton.setStyleSheet(second_style)
        self.zanovo_baton.setFont(QFont("Times New Roman", 15))
        self.csv_save_btn = QPushButton(self)
        self.csv_save_btn.setText('Сохранить csv')
        self.csv_save_btn.move(350, 150)
        self.csv_save_btn.resize(200, 45)
        self.csv_save_btn.setStyleSheet(third_style)
        self.csv_save_btn.clicked.connect(self.csv_saver_func)
        self.csv_save_btn.hide()
        self.back_to_menu_btn = QPushButton('Вернуться', self)
        self.back_to_menu_btn.move(0, 0)
        self.back_to_menu_btn.resize(150, 30)
        self.back_to_menu_btn.setStyleSheet(first_style)
        self.back_to_menu_btn.setFont(QFont("Times New Roman", 15))
        self.back_to_menu_btn.clicked.connect(self.go_back)

        if not sec_tablica:
            self.pioneer_btn = QPushButton('Запустить', self)
            self.pioneer_btn.move(350, 150)
            self.pioneer_btn.resize(200, 45)
            self.pioneer_btn.setStyleSheet(third_style)
            self.pioneer_btn.setFont(QFont("Times New Roman", 15))
            self.pioneer_btn.hide()
            self.pioneer_btn.clicked.connect(self.fill_in)



        if not tablica:
            self.download_button = QPushButton(self)
            self.download_button.setText("Выберите csv файл")
            self.download_button.clicked.connect(self.dialog)
            self.download_button.resize(228, 60)
            self.download_button.move(450, 150)
            self.download_button.setStyleSheet(third_style)
            self.download_button.setFont(QFont("Times New Roman", 15))
            self.proverka_na_pustotu = False
        else:
            self.pioneer_btn.show()
            self.download_button.hide()
            self.main_table.setRowCount(len(self.inside_csv))
            for i in range(len(self.inside_csv)):
                self.main_table.setItem(i, 0, QTableWidgetItem(self.inside_csv[i][0]))
                self.main_table.setItem(i, 2, QTableWidgetItem(self.inside_csv[i][1]))
                self.main_table.item(i, 2).setBackground(QColor(0, 250, 0))
            if sec_tablica:
                self.csv_save_btn.show()
                for i in range(len(self.vtoroy_stolbec)):
                    self.main_table.setItem(i, 1, QTableWidgetItem(self.vtoroy_stolbec[i]))
                    if self.main_table.item(i, 1).text().strip() == self.main_table.item(i, 2).text().strip():
                        self.main_table.item(i, 1).setBackground(QColor(0, 250, 0))
                    else:
                        self.main_table.item(i, 1).setBackground(QColor(250, 0, 0))
                    if self.main_table.item(i, 1).text().strip() == 'error':
                        self.main_table.item(i, 0).setBackground(QColor(250, 0, 0))
                        self.main_table.item(i, 1).setBackground(QColor(250, 0, 0))
                        self.main_table.item(i, 2).setBackground(QColor(250, 0, 0))



            self.main_table.setHidden(False)

            #self.zapustit_btn.hide()


        self.main_table = QTableWidget(self)
        self.main_table.setGeometry(QRect(350, 228, 510, 430))
        self.main_table.setColumnCount(3)
        self.main_table.setHorizontalHeaderLabels(['Url', 'Результат', 'Правильный'])
        self.main_table.setHidden(True)


    def dialog(self):
        self.file, self.checker = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                  "", "All Files (*.csv)")
        if self.checker:
            self.inside_csv = []
            with open(self.file, encoding="utf8") as f:
                reader = csv.reader(f, delimiter=';')
                for i, j in enumerate(reader):
                    if i > 0:
                        self.inside_csv.append(j)
            self.ecran(tablica=True, sec_tablica=False)


    def csv_saver_func(self):
        self.path = QFileDialog.getSaveFileName(self, 'Open File', '', '(*.csv)')
        with open(self.path[0], 'w') as opened_file:
            opened_file.write('site;result')
            for i in range(len(self.vtoroy_stolbec)):
                opened_file.write(f'\n{self.inside_csv[i]};{self.vtoroy_stolbec[i]}')


    def fill_in(self):
        self.vtoroy_stolbec = ['Экономика', 'error', '1']
        self.ecran(tablica=True, sec_tablica=True)
        self.pioneer_btn.hide()

    def again_func(self):
        Popen(['python', 'csv_test_progon.py'])
        sys.exit('csv_progon.py')

    def go_back(self):
        Popen(['python', 'menu.py'])
        sys.exit('csv_progon.py')






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec_())