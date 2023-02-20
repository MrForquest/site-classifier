import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLineEdit

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QFileDialog, QTableWidgetItem, QPlainTextEdit
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import QRect, Qt
import csv

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

fourth_style = '''
QPushButton[text='X'] {
    color: rgb(255, 0, 0);
    font-size: 25px;
}
QPushButton[text='O'] {
    color: rgb(0, 0, 255);
    font-size: 25px;
}
'''

class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 200, 600, 600)
        self.setWindowTitle('Главная форма')

        stylesheet = """
            QWidget {
                background-image: url("shish.jpg");
                background-repeat: no-repeat; 
                background-position: center;
            }
        """

        self.my_font = QFont("Times New Roman", 13)

        self.background = QPlainTextEdit(self)
        self.background.resize(600, 600)
        self.background.setStyleSheet(stylesheet)

        self.menu_label = QLabel("Классификатор сайтов\n\tBy Turbotoster team", self)
        self.menu_label.move(184, 30)
        self.menu_label.resize(1000, 60)
        self.menu_label.setAutoFillBackground(True)
        self.menu_label.setFont((QFont('Times New sefif', 12)))
        self.menu_label.setStyleSheet("""
            background-color: rgb(255, 255, 127);
            font: 87 14pt Segoe UI Black;
        """)



        self.main_func_btn = QPushButton('Одиночный Url', self)
        self.main_func_btn.resize(250, 30)
        self.main_func_btn.move(160, 150)
        self.main_func_btn.setToolTip('Нажмите, если у вас один url')
        self.main_func_btn.setStyleSheet(third_style)
        self.main_func_btn.setFont(self.my_font)


        self.pioneer_csv_btn = QPushButton('CSV с URL', self)
        self.pioneer_csv_btn.resize(250, 30)
        self.pioneer_csv_btn.setToolTip('Нажмите, если у вас готовый csv файл с пачкой url')
        self.pioneer_csv_btn.move(160, 200)
        self.pioneer_csv_btn.setStyleSheet(third_style)
        self.pioneer_csv_btn.setFont(self.my_font)


        self.pioneer_test_csv_btn = QPushButton('Тестовый', self)
        self.pioneer_test_csv_btn.resize(250, 30)
        self.pioneer_test_csv_btn.setToolTip('Нажмите, если это тестовый прогон')
        self.pioneer_test_csv_btn.move(160, 250)
        self.pioneer_test_csv_btn.setStyleSheet(third_style)
        self.pioneer_test_csv_btn.setFont(self.my_font)



        self.main_func_btn.clicked.connect(self.open_second_form)
        self.pioneer_csv_btn.clicked.connect(self.csv_ne_test)
        self.pioneer_test_csv_btn.clicked.connect(self.csv_test)



    def open_second_form(self):
        self.second_form = SecondForm(self, "")
        self.second_form.show()
        self.close()

    def play_again_btn_pushed(self):
        self.second_form = SecondForm(self, "")
        self.second_form.show()
        self.close()

    def csv_ne_test(self):
        self.second_form = Csv_progon(self, "")
        self.second_form.show()
        self.close()

    def csv_test(self):
        self.second_form = Csv_test_progon(self, "")
        self.second_form.show()
        self.close()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)


    def initUI(self, args):
        font = QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.func_fon = """
            QWidget {
                background-image: url("boroda.jpg");
                background-repeat: no-repeat; 
                background-position: center;
            }
        """
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle('Вторая форма')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()
        self.space_for_bckg = QPlainTextEdit(self)
        self.space_for_bckg.resize(1000, 1000)
        self.space_for_bckg.setStyleSheet(self.func_fon)
        self.comeback_btn = QPushButton(self)
        self.comeback_btn.clicked.connect(self.nazad_vernutsya)
        self.comeback_btn.setText('Назад')
        self.comeback_btn.setFont(QFont("Times New Roman", 11))
        self.comeback_btn.setStyleSheet('background: rgb(255,0,0);')
        self.again_btn = QPushButton(self)
        self.again_btn.setText('Заново')
        self.again_btn.setFont(QFont("Times New Roman", 11))
        self.again_btn.move(0, 25)
        self.again_btn.resize(80, 25)
        self.again_btn.setStyleSheet(second_style)
        self.again_btn.clicked.connect(self.play_again_btn_pushed)
        self.csv_save_btn = QPushButton(self)
        self.csv_save_btn.setText('Сохранить csv')
        self.csv_save_btn.setFont(QFont("Times New Roman", 15))
        self.csv_save_btn.move(800, 222)
        self.csv_save_btn.resize(170, 40)
        self.csv_save_btn.setStyleSheet(third_style)
        self.csv_save_btn.clicked.connect(self.csv_saver_func)
        self.csv_save_btn.hide()
        self.url_input = QLineEdit(self)
        self.url_input.move(380, 220)
        self.url_input.resize(350, 40)
        self.url_input.setStyleSheet("    QLineEdit{\n"
"    border-radius: 10px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    background: pink;\n"
"}\n"
"\n"
"    QLineEdit:hover {\n"
"    border: 3px solid rgb(61,181,233);\n"
"    }")
        self.url_input.setAlignment(Qt.AlignCenter)

        self.starter_btn = QPushButton(self)
        self.starter_btn.setText('Запуск')
        self.starter_btn.setFont(QFont("Times New Roman", 15))
        self.starter_btn.move(465, 310)
        self.starter_btn.resize(180, 60)
        self.starter_btn.setStyleSheet(third_style)
        self.starter_btn.clicked.connect(self.afterzapusk)

        self.end_btn = QLabel(self)
        self.end_btn.move(184, 30)
        self.end_btn.resize(1000, 60)
        self.end_btn.setAutoFillBackground(True)
        self.end_btn.setFont((QFont('Times New sefif', 12)))
        self.end_btn.setStyleSheet("""
            background-color: rgb(255, 255, 127);
            font: 87 14pt Segoe UI Black;
        """)

    def nazad_vernutsya(self):
        self.go_back_btn = FirstForm()
        self.go_back_btn.show()
        self.close()


    def play_again_btn_pushed(self):
        self.second_form = SecondForm(self, "")
        self.second_form.show()
        self.close()


    def afterzapusk(self):
        self.tip_sayta = 'ECONOMIKA'
        self.end_btn.setText(f'Тип вашего сайта:\n {self.tip_sayta}')
        self.csv_save_btn.show()

    def csv_saver_func(self):
        self.path = QFileDialog.getSaveFileName(self, 'Open File', '', '(*.csv)')
        with open(self.path[0], 'w') as opened_file:
            opened_file.write('site;result')
            opened_file.write(f'\n{self.url_input.text()};{self.tip_sayta}')

class Csv_test_progon(QWidget):

    def __init__(self, *args):
        super().__init__()
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
        self.csv_save_btn.setFont(QFont("Times New Roman", 15))
        self.csv_save_btn.move(350, 150)
        self.csv_save_btn.resize(228, 60)
        self.csv_save_btn.setStyleSheet(third_style)
        self.csv_save_btn.clicked.connect(self.csv_saver_func)
        self.csv_save_btn.hide()
        self.back_to_menu_btn = QPushButton('Вернуться', self)
        self.back_to_menu_btn.move(0, 0)
        self.back_to_menu_btn.resize(150, 30)
        self.back_to_menu_btn.setStyleSheet(first_style)
        self.back_to_menu_btn.setFont(QFont("Times New Roman", 15))
        self.back_to_menu_btn.clicked.connect(self.go_back)
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
            self.pioneer_btn.resize(228, 60)
            self.pioneer_btn.setStyleSheet(third_style)
            self.pioneer_btn.setFont(QFont("Times New Roman", 15))
            self.pioneer_btn.hide()
            self.pioneer_btn.clicked.connect(self.fill_in)



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
            if all(len(z) == 2 for z in self.inside_csv):
                self.pioneer_btn.show()
                self.download_button.hide()
                self.main_table.setRowCount(len(self.inside_csv))
                self.main_table.setHidden(False)


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

            else:
                self.error_lable.show()




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
                #print(all(len(z) == 2 for z in reader))
                for i, j in enumerate(reader):
                    if i > 0:
                        self.inside_csv.append(j)
            #if all(len(z) == 2 for z in self.inside_csv):
            self.error_lable.hide()
            self.ecran(tablica=True, sec_tablica=False)
            print(self.inside_csv)
            # else:
            #     self.ecran(tablica=True, sec_tablica=False)

    def csv_saver_func(self):
        self.path = QFileDialog.getSaveFileName(self, 'Open File', '', '(*.csv)')
        with open(self.path[0], 'w') as opened_file:
            opened_file.write('site;result')
            for i in range(len(self.vtoroy_stolbec)):
                opened_file.write(f'\n{self.inside_csv[i][0]};{self.vtoroy_stolbec[i]}')


    def fill_in(self):
        self.vtoroy_stolbec = ['Экономика', 'error', '1']
        self.ecran(tablica=True, sec_tablica=True)
        self.pioneer_btn.hide()

    def again_func(self):
        self.second_form = Csv_test_progon(self, "")
        self.second_form.show()
        self.close()

    def go_back(self):
        self.go_back_btn = FirstForm()
        self.go_back_btn.show()
        self.close()


class Csv_progon(QWidget):

    def __init__(self, *args):
        super().__init__()
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
        self.second_form = Csv_progon(self, "")
        self.second_form.show()
        self.close()

    def go_back(self):
        self.go_back_btn = FirstForm()
        self.go_back_btn.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())