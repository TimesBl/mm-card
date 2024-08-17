from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

#================================================================
#Створення вікна
#================================================================
app = QApplication([])
menu_wind = QWidget()
menu_wind.resize(400,300)
menu_wind.setWindowTitle('Меню')

#================================================================
#Створення ліній з запитаннями
#================================================================


txt_Qestion = QLineEdit("")
txt_Answer = QLineEdit("")
txt_Wrong1 = QLineEdit("")
txt_Wrong2 = QLineEdit("")
txt_Wrong3 = QLineEdit('')


layout_from = QFormLayout()
layout_from.addRow("Введіть запитання:",txt_Qestion)
layout_from.addRow("Введіть вірну відповідь:",txt_Answer)
layout_from.addRow("Введіть першу хибну відповідь:",txt_Wrong1)
layout_from.addRow("Введіть другу хибну відповідь:",txt_Wrong2)
layout_from.addRow("Введіть третю хибну відповідь:",txt_Wrong3)


btn_add_q = QPushButton("Додати запитання")
btn_back = QPushButton("Назад")
btn_clear = QPushButton("Очистити")

#================================================================
#Створення статистики
#================================================================
lbl_statistics = QLabel('')
lbl_statistics = QLabel('Статистика:\nПравельних відповідей: 0\nЗагальна кількість спроб: 0')


hbtn = QHBoxLayout()
hbtn.addWidget(btn_back)
hbtn.addWidget(btn_add_q)
hbtn.addWidget(btn_clear)

vline = QVBoxLayout()
vline.addLayout(layout_from)
vline.addLayout(hbtn)
vline.addWidget(lbl_statistics)


menu_wind.setLayout(vline)

#================================================================
#Очікуємо закриття вікна
#================================================================
menu_wind.show()
app.exec_()