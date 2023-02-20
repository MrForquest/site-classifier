import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QComboBox, QTableView, QVBoxLayout, QTableWidget, QFileDialog, QTableWidgetItem, QPlainTextEdit
from PyQt5.QtGui import QFont, QIcon, QStandardItemModel, QStandardItem, QColor
from PyQt5.QtCore import QRect, Qt
from subprocess import Popen, call
import csv


first_style = ("background-color: rgb(100, 255, 100);\n"
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

second_style = ("background-color: rgb(255, 150, 150);\n"
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
        self.screen_table()

    def screen_table(self, tablica=False, sec_tablica=False):
        self.bkgrnd = """
            QWidget {
                background-image: url("boroda.jpg");
                background-repeat: no-repeat; 
                background-position: center;
            }
        """
        self.phone_space = QPlainTextEdit(self)
        self.phone_space.resize(1000, 1000)
        self.phone_space.setStyleSheet(self.bkgrnd)
        self.setGeometry(100, 100, 1000, 1000)
        self.again = QPushButton('Заново', self)
        self.again.setGeometry(100, 370, 200, 30)
        self.again.move(0, 30)
        self.again.clicked.connect(self.again_funk)
        self.again.resize(150, 30)
        self.again.setStyleSheet(first_style)
        self.again.setFont(QFont("Times New Roman", 15))
        self.csv_save_btn = QPushButton(self)
        self.csv_save_btn.setText('Сохранить csv')
        self.csv_save_btn.move(350, 150)
        self.csv_save_btn.resize(200, 45)
        self.csv_save_btn.setFont(QFont("Times New Roman", 15))
        self.csv_save_btn.setStyleSheet(third_style)
        self.csv_save_btn.clicked.connect(self.csv_saver_func)
        self.csv_save_btn.hide()
        self.comeback_to_menu = QPushButton('Вернуться', self)
        self.comeback_to_menu.move(0, 0)
        self.comeback_to_menu.resize(150, 30)
        self.comeback_to_menu.setStyleSheet(second_style)
        self.comeback_to_menu.setFont(QFont("Times New Roman", 15))
        self.comeback_to_menu.clicked.connect(self.go_back)
        self.error_lable = QLabel(self)
        self.error_lable.move(330, 228)
        self.error_lable.setText('Выбранный вами csv файл\nне соответствует стандартам категории')
        self.error_lable.setStyleSheet("color: rgb(255, 0, 0);")
        self.error_lable.setAlignment(Qt.AlignCenter)
        self.error_lable.setFont(QFont('Times', 15, QFont.Bold))
        self.error_lable.hide()

        if not sec_tablica:
            self.pioneer_btn = QPushButton('Запустить', self)
            self.pioneer_btn.move(350, 150)
            self.pioneer_btn.resize(200, 45)
            self.pioneer_btn.setStyleSheet(third_style)
            self.pioneer_btn.setFont(QFont("Times New Roman", 15))
            self.pioneer_btn.hide()
            self.pioneer_btn.clicked.connect(self.feel_in)



        if not tablica:
            self.download_button = QPushButton(self)
            self.download_button.setText("Выберите csv файл")
            self.download_button.clicked.connect(self.dialog)
            self.download_button.resize(228, 60)
            self.download_button.move(350, 150)
            self.download_button.setStyleSheet(third_style)
            self.download_button.setFont(QFont("Times New Roman", 15))
            self.proverka_na_pustotu = False
        else:
            if all(len(z) == 1 for z in self.csv_in):
                self.error_lable.hide()
                self.inside_csv = [i[0] for i in self.csv_in]
                self.pioneer_btn.show()
                self.download_button.hide()
                self.main_table.setRowCount(len(self.csv_in))
                self.main_table.setHidden(False)

                for i in range(len(self.csv_in)):
                    self.main_table.setItem(i, 0, QTableWidgetItem(self.inside_csv[i]))
                if sec_tablica:
                    self.csv_save_btn.show()
                    for i in range(len(self.second_table)):
                        self.main_table.setItem(i, 1, QTableWidgetItem(self.second_table[i]))
                        if self.main_table.item(i, 1).text().strip() == 'error':
                            self.main_table.item(i, 1).setBackground(QColor(255, 0, 0))
                            self.main_table.item(i, 0).setBackground(QColor(255, 0, 0))
                        else:
                            self.main_table.item(i, 1).setBackground(QColor(0, 255, 0))

            else:
                self.error_lable.show()

        self.main_table = QTableWidget(self)
        self.main_table.setGeometry(QRect(350, 228, 310, 430))
        self.main_table.setColumnCount(2)
        self.main_table.setHorizontalHeaderLabels(['Url', 'Результат'])
        self.main_table.setHidden(True)


    def dialog(self):
        self.error_lable.hide()

        self.file, self.checker = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                  "", "All Files (*.csv)")
        if self.checker:
            self.csv_in = []
            with open(self.file, encoding="utf8") as f:
                reader = csv.reader(f, delimiter=';')
                #print(all(len(z) == 2 for z in reader))
                for i, j in enumerate(reader):
                    if i > 0:
                        self.csv_in.append(j)
            #if all(len(z) == 2 for z in self.inside_csv):
            #self.error_lable.hide()
            #print(self.csv_in)
            self.screen_table(tablica=True, sec_tablica=False)


    def feel_in(self):
        self.second_table = ['error', '1']
        self.screen_table(tablica=True, sec_tablica=True)
        self.pioneer_btn.hide()

    def csv_saver_func(self):
        self.path = QFileDialog.getSaveFileName(self, 'Open File', '', '(*.csv)')
        with open(self.path[0], 'w') as opened_file:
            opened_file.write('site;result')
            for i in range(len(self.second_table)):
                opened_file.write(f'\n{self.csv_in[i]};{self.second_table[i]}')


    def again_funk(self):
        self.setGeometry(0, 0, 0, 0)
        call(["python", "csv_progon.py"])

    def go_back(self):
        Popen(['python', 'menu.py'])
        sys.exit('csv_progon.py')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec_())