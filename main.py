import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QLine, QRect, QPoint, QSize
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.rects_for_letters = list()
        self.words = ['ромашка', 'солнце', 'собака']
        self.hints = ['На любовь гадают обычно именно так',
                      'В начале оно вращалось вокруг, а потом оказалось, что всё иначе', 'Друг человека']
        self.new_word = random.choice(self.words)
        self.dict_words = dict()
        for i in range(len(self.words)):
            self.dict_words[self.words[i]] = self.hints[i]

        self.initUI(self.dict_words[self.new_word])

    def initUI(self, text):
        self.text = text
        self.setGeometry(500, 300, 480, 370)
        self.setWindowTitle('Виселица')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp, self.text)
        self.drawMan(qp)
        qp.end()

    def drawMan(self, qp):
        # убрать все фекции, на отрисовку сделал хуйню...
        qp.setPen(QColor(192, 50, 153))
        qp.drawLine(10, 200, 470, 200)
        qp.drawLine(10, 230, 470, 230)
        x, y = (self.width() // 2 - (23 * len(self.new_word)) // 2), 205
        for i in range(len(self.new_word)):
            rect = QRect(QPoint(x + (i * 23), y), QSize(20, 20))
            qp.drawRect(x + (i * 23), y, 20, 20)
            self.rects_for_letters.append(rect)
            print(1)
            print(type(self.rects_for_letters[i]))
            print(1)
            qp.drawText(self.rects_for_letters[i], Qt.AlignCenter, self.new_word[i])
            print(1)

        qp.setPen(QColor(1, 1, 1))
        self.first_line = qp.drawLine(290, 40, 290, 150)
        self.second_line = qp.drawLine(310, 60, 220, 60)
        self.third_line = qp.drawLine(220, 60, 220, 85)
        self.head = qp.drawEllipse(213, 85, 15, 15)
        self.body = qp.drawLine(220, 100, 220, 130)
        self.first_hand = qp.drawLine(220, 105, 230, 115)
        self.second_hand = qp.drawLine(220, 105, 210, 115)
        self.first_leg = qp.drawLine(220, 130, 210, 140)
        self.second_leg = qp.drawLine(220, 130, 230, 140)

    def drawText(self, event, qp, text):
        qp.setPen(QColor(1, 1, 1))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignTop, text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
