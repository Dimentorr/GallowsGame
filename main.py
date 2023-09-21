import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap, QPen
from PyQt5.QtCore import Qt, QLine, QRect, QPoint, QSize
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.isGame = True
        self.guessedRight = 0
        self.notGuessed = 0
        self.rects_for_letters = list()
        self.words = ['ромашка', 'солнце', 'собака']
        self.hints = ['На любовь гадают обычно именно так',
                      'В начале оно вращалось вокруг, а потом оказалось, что всё иначе', 'Друг человека']
        self.new_word = random.choice(self.words)
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

    def paintEvent(self, event):
        QWidget.paintEvent(self, event)
        qp = QPainter()
        qp.begin(self)
        match self.start:
            case 1:
                self.start += 1
                self.drawText(event, qp, self.text)
                self.drawAllForWord(qp)
            case _:
                self.drawMan(qp, self.notGuessed)
        qp.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.text() in self.new_word and self.isGame:
            self.guessedRight += 1
            pass
        elif event.text() not in self.new_word and self.isGame:
            self.notGuessed += 1
            self.update()

    def drawAllForWord(self, qp):
        qp.setPen(QColor(192, 50, 153))
        qp.drawLine(10, 200, 470, 200)
        qp.drawLine(10, 230, 470, 230)
        x, y = (self.width() // 2 - (23 * len(self.new_word)) // 2), 205
        for i in range(len(self.new_word)):
            rect = QRect(QPoint(x + (i * 23), y), QSize(20, 20))
            qp.drawRect(x + (i * 23), y, 20, 20)
            self.rects_for_letters.append(rect)
            qp.drawText(self.rects_for_letters[i], Qt.AlignCenter, self.new_word[i])

    def drawMan(self, qp, count):
        qp.setPen(QColor(1, 1, 1))
        match count:
            case 1:
                # first_line
                qp.drawLine(290, 40, 290, 150)
            case 2:
                # second_line
                qp.drawLine(QPoint(310, 60), QPoint(220, 60))
            case 3:
                # third_line
                qp.drawLine(QPoint(220, 60), QPoint(220, 85))
            case 4:
                # head
                qp.drawEllipse(213, 85, 15, 15)
            case 5:
                # body
                qp.drawLine(QPoint(220, 100), QPoint(220, 130))
            case 6:
                # first_hand
                qp.drawLine(QPoint(220, 105), QPoint(230, 115))
            case 7:
                # second_hand
                qp.drawLine(QPoint(220, 105), QPoint(210, 115))
            case 8:
                # first_leg
                qp.drawLine(QPoint(220, 130), QPoint(210, 140))
            case 9:
                # second_leg
                qp.drawLine(QPoint(220, 130), QPoint(230, 140))
                self.isGame = False
                print('you lose')
            case _:
                print('you lose')

    def drawText(self, event, qp, text):
        qp.setPen(QColor(1, 1, 1))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignTop, text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    # ex = MainWindow()
    sys.exit(app.exec_())
