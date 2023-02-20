import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDoubleSpinBox
from PyQt5.QtWidgets import QLabel, QLineEdit, QSpinBox, QPlainTextEdit, QComboBox, QVBoxLayout, QFileDialog, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from subprocess import call
import os

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

        self.menu_label = QLabel("Тут могла быть ваша реклама\n\t8 800 555 35 35", self)
        self.menu_label.move(184, 30)
        self.menu_label.resize(1000, 60)
        self.menu_label.setAutoFillBackground(True)
        self.menu_label.setFont((QFont('Times New sefif', 12)))
        self.menu_label.setStyleSheet("""
            background-color: rgb(255, 255, 127);
            font: 87 14pt Segoe UI Black;
        """)

        self.btn = QPushButton('противник', self)
        self.btn.resize(80, 30)
        self.btn.move(150, 100)
        self.btn.setToolTip('Нажмите, если первый ход за соперником')
        self.btn.setStyleSheet(first_style)
        self.btn.setFont(self.my_font)
        self.btn.hide()

        self.main_func_btn = QPushButton('Начать', self)
        self.main_func_btn.resize(80, 30)
        self.main_func_btn.move(210, 100)
        self.main_func_btn.setToolTip('Нажмите, если у вас один url')
        self.main_func_btn.setStyleSheet(second_style)
        self.main_func_btn.setFont(self.my_font)


        self.pioneer_csv_btn = QPushButton('CSV прогон', self)
        self.pioneer_csv_btn.resize(210, 30)
        self.pioneer_csv_btn.setToolTip('Нажмите, если у вас готовый csv файл с пачкой url')
        self.pioneer_csv_btn.move(75, 500)
        self.pioneer_csv_btn.setStyleSheet(third_style)
        self.pioneer_csv_btn.setFont(self.my_font)


        self.pioneer_test_csv_btn = QPushButton('Тестовый', self)
        self.pioneer_test_csv_btn.resize(250, 30)
        self.pioneer_test_csv_btn.setToolTip('Нажмите, если это тестовый прогон')
        self.pioneer_test_csv_btn.move(100, 550)
        self.pioneer_test_csv_btn.setStyleSheet(third_style)
        self.pioneer_test_csv_btn.setFont(self.my_font)



        self.main_func_btn.clicked.connect(self.open_second_form)
        self.pioneer_csv_btn.clicked.connect(self.csv_ne_test)
        self.pioneer_test_csv_btn.clicked.connect(self.csv_test)



    def open_second_form(self):
        self.second_form = SecondForm(self, "")
        self.second_form.show()
        self.setGeometry(0, 0, 0, 0)

    def play_again_btn_pushed(self):
        self.second_form = SecondForm(self, "")
        self.second_form.show()
        self.setGeometry(0, 0, 0, 0)

    def csv_ne_test(self):
        self.setGeometry(0, 0, 0, 0)
        call(["python", "csv_progon.py"])

    def csv_test(self):
        self.setGeometry(0, 0, 0, 0)
        call(["python", "csv_test_progon.py"])


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
        self.comeback_btn.setText('Вернуться')
        self.comeback_btn.setStyleSheet('background: rgb(255,0,0);')
        self.again_btn = QPushButton(self)
        self.again_btn.setText('Заново')
        self.again_btn.move(0, 25)
        self.again_btn.resize(80, 25)
        self.again_btn.setStyleSheet(second_style)
        self.again_btn.clicked.connect(self.play_again_btn_pushed)
        self.csv_save_btn = QPushButton(self)
        self.csv_save_btn.setText('Сохранить csv')
        self.csv_save_btn.move(800, 222)
        self.csv_save_btn.resize(140, 40)
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
        self.setGeometry(0, 0, 0, 0)


    def play_again_btn_pushed(self):
        self.second_form = SecondForm(self, "")
        self.second_form.show()
        self.setGeometry(0, 0, 0, 0)


    def afterzapusk(self):
        self.tip_sayta = 'ECONOMIKA'
        self.end_btn.setText(f'Тип вашего сайта:\n {self.tip_sayta}')
        self.csv_save_btn.show()

    def csv_saver_func(self):
        self.path = QFileDialog.getSaveFileName(self, 'Open File', '', '(*.csv)')
        with open(self.path[0], 'w') as opened_file:
            opened_file.write('site;result')
            opened_file.write(f'\n{self.url_input.text()};{self.tip_sayta}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())