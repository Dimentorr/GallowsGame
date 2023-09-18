import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QLine, QRect
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.words = ['ромашка', 'солнце', 'собака']
        self.hints = ['На любовь гадают обычно именно так',
                      'В начале оно вращалось вокруг, а потом оказалось, что всё иначе', 'Друг человека']
        self.new_word = random.choice(self.words)
        self.dict_words = dict()
        for i in range(len(self.words)):
            self.dict_words[self.words[i]] = self.hints[i]

        self.initUI(self.dict_words[self.new_word])

    def draw_first_line(self, qp):
        qp.drawLine(290, 40, 290, 150)

    def draw_second_line(self, qp):
        qp.drawLine(310, 60, 220, 60)

    def draw_third_line(self, qp):
        qp.drawLine(220, 60, 220, 85)

    def draw_head(self, qp):
        qp.drawEllipse(213, 85, 15, 15)

    def draw_body(self, qp):
        qp.drawLine(220, 100, 220, 130)

    def draw_first_hand(self, qp):
        qp.drawLine(220, 105, 230, 115)

    def draw_second_hand(self, qp):
        qp.drawLine(220, 105, 210, 115)

    def draw_first_leg(self, qp):
        qp.drawLine(220, 130, 210, 140)

    def draw_second_leg(self, qp):
        qp.drawLine(220, 130, 230, 140)

    def initUI(self, text):
        self.text = text
        self.setGeometry(500, 300, 480, 370)
        self.setWindowTitle('Виселица')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        self.drawMan(qp)
        qp.end()

    def drawMan(self, qp):
        qp.setPen(QColor(1, 1, 1))
        self.draw_first_line(qp)
        self.draw_second_line(qp)
        self.draw_third_line(qp)
        self.draw_head(qp)
        self.draw_body(qp)
        self.draw_first_hand(qp)
        self.draw_second_hand(qp)
        self.draw_first_leg(qp)
        self.draw_second_leg(qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(1, 1, 1))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignTop, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
