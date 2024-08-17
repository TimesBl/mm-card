from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([]) 


# -----------------------------------------------------------------------
# Основне вікно
# -----------------------------------------------------------------------
main_win = QWidget()                                                   # Створення вікна
main_win.resize(600, 500)                                              # Задавання розмирів вікна
main_win.move(300, 300)                                                # Задавання місце спавну вікна 
main_win.setWindowTitle("Питання")                                     # Зазва вікна



# -----------------------------------------------------------------------
# Створюємо потрібні віджети Кнопки - таймер - надпис
# -----------------------------------------------------------------------
btn_Menu = QPushButton('Меню')                                         # Кнопка повернення 
btn_Sleep = QPushButton('Відпочити')                                   # Кнопка прибирає вікно 
btn_OK = QPushButton('Відповісти')                                     # Кнопка відповіді
box_Minutes = QSpinBox()                                               # Введення кількості хвилин
box_Minutes.setValue(30)                                               # Встановлення по дефолту значення
lb_Question = QLabel('')                                               # Текст питання


# -----------------------------------------------------------------------
#  Створюємо панель  - із варіантами відповідей - групуємо
# -----------------------------------------------------------------------
RadioGroupBox = QGroupBox("Варіанти відповідей:")                      # Створення панелі-рамки для блоку 
RadioGroup = QButtonGroup()                                            # Організація в групу віджетів (кнопок)


rbtn_1 = QRadioButton('')                                              # Радіо кнопка 1
rbtn_2 = QRadioButton('')                                              # Радіо кнопка 2
rbtn_3 = QRadioButton('')                                              # Радіо кнопка 3
rbtn_4 = QRadioButton('')                                              # Радіо кнопка 4


RadioGroup.addButton(rbtn_1)    
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# -----------------------------------------------------------------------
#  Створюємо рамку
# -----------------------------------------------------------------------

layout_ans1 = QHBoxLayout()                                            # Вертикальні будуть усередині горизонтального
layout_ans2 = QVBoxLayout()                                            # Вертикальні будуть усередині горизонтального
layout_ans3 = QVBoxLayout()                                            # Вертикальні будуть усередині горизонтального


layout_ans2.addWidget(rbtn_1)                                          
layout_ans2.addWidget(rbtn_2)                                          # відповідь в перший стовпець
layout_ans3.addWidget(rbtn_3)                                          # відповідь в перший стовпець
layout_ans3.addWidget(rbtn_4)                                          # відповідь в другий стовпецьь
layout_ans3.addWidget(rbtn_4)                                          # відповідь в другий стовпець

                                             #----------------------- Тепер перемикачі прив'язані до однієї горизонтальної направляючої лінії -----------------------

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)


# -----------------------------------------------------------------------
# Створюємо панель із результатом тесту:
# -----------------------------------------------------------------------
AnsGroupBox = QGroupBox("Результат тесту:")
lb_Result = QLabel('')                                                 # Напис "правильно"/"неправильно"
lb_Correct = QLabel('')                                                # Текст правильної відповіді

                                              #----------------------- Розміщуемо -------------------
layout_res = QVBoxLayout() 
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()                                                     # Можна приховати віджет     


# -----------------------------------------------------------------------
# Розміщуемо віджети в головному вікні
# -----------------------------------------------------------------------
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

                                            #----------------------- Розмінюємо на першій лінії (кнопки меню,сну,і надпис) ------------------- 

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel("хвилин"))

                                            #----------------------- Розмінюємо на другій лінії надпис - питання ------------------- 
layout_line2.addWidget(lb_Question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

                                            #----------------------- Розмінюємо на третій лінії рамки ------------------- 
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)
                                            #----------------------- розмінюємо на 4 тій лінії кнопку відповісти -------------------
layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK,stretch=2)
layout_line4.addStretch(1)

                                            #----------------------- 4 горизонтальні на 1 вертикальну -------------------
layout_cards = QVBoxLayout()
layout_cards.addLayout(layout_line1,stretch=1)
layout_cards.addLayout(layout_line2,stretch=2)
layout_cards.addLayout(layout_line3,stretch=8)

layout_cards.addStretch(1)
layout_cards.addLayout(layout_line4,stretch=1)
layout_cards.addStretch(1)
layout_cards.setSpacing(5)                                           # прогалини між вмістом

main_win.setLayout(layout_cards)                                     # передаємо на головне вікно основний макет



main_win.show()
app.exec_()
