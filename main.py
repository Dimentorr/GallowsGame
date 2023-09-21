import sys
import re

from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QRect, QPoint, QSize
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.allFiguresForGame = list()
        # first_line
        self.allFiguresForGame.append(list((QPoint(290, 40), QPoint(290, 150))))
        # second_line
        self.allFiguresForGame.append(list((QPoint(310, 60), QPoint(220, 60))))
        # third_line
        self.allFiguresForGame.append(list((QPoint(220, 60), QPoint(220, 85))))
        # body
        self.allFiguresForGame.append(list((QPoint(220, 100), QPoint(220, 130))))
        # first_hand
        self.allFiguresForGame.append(list((QPoint(220, 105), QPoint(230, 115))))
        # second_hand
        self.allFiguresForGame.append(list((QPoint(220, 105), QPoint(210, 115))))
        # first_leg
        self.allFiguresForGame.append(list((QPoint(220, 130), QPoint(210, 140))))
        # second_leg
        self.allFiguresForGame.append(list((QPoint(220, 130), QPoint(230, 140))))

        self.isGame = True
        self.guessedRight = 0
        self.guessedLetters = set()
        self.notGuessed = 0
        self.words = ['ромашка', 'солнце', 'собака']
        self.hints = ['На любовь гадают обычно именно так',
                      'В начале оно вращалось вокруг, а потом оказалось, что всё иначе', 'Друг человека']
        self.new_word = random.choice(self.words)
        self.word_for_check = self.new_word
        self.dict_words = dict()
        for i in range(len(self.words)):
            self.dict_words[self.words[i]] = self.hints[i]

        self.start = 1
        self.initUI(self.dict_words[self.new_word])

    def initUI(self, text):
        self.text = text
        self.setGeometry(500, 300, 480, 370)
        self.setWindowTitle('Виселица')
        self.show()

    def mess(self, text, title):
        msg = QMessageBox()
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()

    def paintEvent(self, event):
        QWidget.paintEvent(self, event)
        qp = QPainter()
        qp.begin(self)
        match self.start:
            case 1:
                self.start += 1
                self.drawText(event, qp, self.text)
                self.drawAllForWord(qp, self.guessedRight, self.new_word)
                self.drawMan(qp, self.notGuessed)
            case _:
                self.drawText(event, qp, self.text)
                self.drawAllForWord(qp, self.guessedRight, self.new_word)
                self.drawMan(qp, self.notGuessed)
        qp.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.text() in self.new_word and self.isGame:
            if event.text() in self.guessedLetters:
                self.mess('Эта буква уже отгадана!', 'Предупреждение')
                # print('Эта буква уже отгадана!')
            else:
                self.guessedLetters.add(event.text())
                res = self.checkLetters(self.word_for_check, event.text())
                self.word_for_check.replace(event.text(), '')
                self.guessedRight += len(res)
                if self.guessedRight == len(self.new_word):
                    self.mess(f'Правильно, это {self.new_word}!', 'Победа')
                    self.isGame = False
                self.update()
        elif event.text() not in self.new_word and self.isGame:
            self.notGuessed += 1
            # потом вставить сюда переменную хранящую максимальное кол-во ошибок
            if self.notGuessed == 9:
                self.mess(f'Увы, но загаданное слово было - {self.new_word}!', 'Поражение')
                self.isGame = False
            self.update()

    def checkLetters(self, word, letter):
        matches = re.finditer(letter, word)
        result = [match.start() for match in matches]
        return result

    def drawAllForWord(self, qp, count, word):
        allRect = list()
        qp.setPen(QColor(192, 50, 153))
        qp.drawLine(10, 200, 470, 200)
        qp.drawLine(10, 230, 470, 230)
        x, y = (self.width() // 2 - (23 * len(word)) // 2), 205
        for i in range(len(word)):
            rect = QRect(QPoint(x + (i * 23), y), QSize(20, 20))
            qp.drawRect(x + (i * 23), y, 20, 20)
            allRect.append(rect)
        for i in self.guessedLetters:
            pos_let = self.checkLetters(self.new_word, i)
            for j in pos_let:
                qp.drawText(allRect[j], Qt.AlignCenter, i)

    def drawMan(self, qp, count):
        qp.setPen(QColor(1, 1, 1))
        flag = False
        if count >= 4:
            flag = True
        for i in range(count):
            if flag and i + 1 == count:
                qp.drawEllipse(213, 85, 15, 15)
                i -= 1
                flag = False
                if i + 2 == count:
                    break
            else:
                qp.drawLine(self.allFiguresForGame[i][0], self.allFiguresForGame[i][1])

        # self.isGame = False
        # print('you lose')


    def drawText(self, event, qp, text):
        qp.setPen(QColor(1, 1, 1))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignTop, text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())