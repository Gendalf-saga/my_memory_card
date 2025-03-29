import PyQt5.QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык бразилии?', 'Португальский', 'Английский', 'Французский', 'Испанский'))
question_list.append(Question('Какого цвета нет на флаге России?','Зелёный', 'Красный', 'Синий', 'Белый'))
question_list.append(Question('Национальная хижина Якутов:', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
#создай приложение для запоминания информации
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

#Кнопка
answer_button_1 = QPushButton('Ответить')
answer_Label = QLabel('Какой национальности не существует?')


#Группа с кнопками
RadioGroupBox = QGroupBox('Варианты ответов')



#Кнопки
rbn1 = QRadioButton('Энцы')
rbn2 = QRadioButton('Чулмынцы')
rbn3 = QRadioButton('Смурфы')
rbn4 = QRadioButton('Алеуты')

#Привязка кнопок к группе RadioGroup()
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbn1)
RadioGroup.addButton(rbn2)
RadioGroup.addButton(rbn3)
RadioGroup.addButton(rbn4)

#Линии
line_1 = QHBoxLayout()
line_2 = QVBoxLayout()
line_3 = QVBoxLayout()



#Привязка
"Привязка первых двух кнопок к вертикали"
line_2.addWidget(rbn1)
line_2.addWidget(rbn2)
"Привязка двух других кнопок к вертикали"
line_3.addWidget(rbn3)
line_3.addWidget(rbn4)
"Прявязка вертикалей к горизонтали"
line_1.addLayout(line_2)
line_1.addLayout(line_3)
#P.S. Вертикалей две, горизонталь одна и к ней привязываются две вертикали

#Привязка к горизонтали
RadioGroupBox.setLayout(line_1)

AnswerGroupBox = QGroupBox('Результаты теста')
LBResult = QLabel('Прав ты или нет?')
LBCorrect = QLabel('Ответ будет тут!')


answer_line_1 = QVBoxLayout()
answer_line_1.addWidget(LBResult)
answer_line_1.addWidget(LBCorrect)

AnswerGroupBox.setLayout(answer_line_1)


#Еще линии
line_4 = QHBoxLayout()
line_5 = QHBoxLayout()
line_6 = QHBoxLayout()

#Привязка к другой горизонтали
line_4.addWidget(answer_Label)
line_5.addWidget(RadioGroupBox)
line_6.addWidget(answer_button_1)
line_5.addWidget(AnswerGroupBox)

setLayout = QVBoxLayout()
setLayout.addLayout(line_4)
setLayout.addLayout(line_5)
setLayout.addLayout(line_6)

main_win.setLayout(setLayout)


def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    answer_button_1.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    answer_button_1.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbn1.setChecked(False)
    rbn2.setChecked(False)
    rbn3.setChecked(False)
    rbn4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbn1, rbn2, rbn3, rbn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    answer_Label.setText(q.question)
    LBCorrect.setText(q.right_answer)
    show_question()

def show_correct(res):
    LBResult.setText(res)
    show_result()
    
def next_question():
    main_win.total += 1
    cur_question = randint (0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)
    
def click_OK():
    if answer_button_1.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Верно!')
        main_win.score += 1
        print('Всего вопросов:', main_win.total)
        print('Верных ответов:', main_win.score)
        print('Рейтинг:', (main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

main_win.cur_question = -1



answer_button_1.clicked.connect(click_OK)

main_win.total = 0
main_win.score = 0


next_question()

#!______ЗАПУСК ОКНА________!
main_win.resize(400, 300)
main_win.show()
app.exec_()