import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'untitled.ui', self)  # Загружаем дизайн
        self.btn.clicked.connect(self.hello)
        self.run()

    def run(self):
        pass

    def hello(self):
        s = self.edit.text()
        file = None
        try:
            file = open(s, 'r', encoding='utf-8')
        except Exception:
            self.myLabel.setText(f'Файл {s} не найден')
            return
        q = file.read()
        q.replace('\t', ' ')
        q.replace('\n', ' ')
        q.replace('\r', ' ')
        q.replace('\f', ' ')
        q.replace('\v', ' ')
        try:
            n = list(map(int, q.split()))
            self.box1.setValue(max(n))
            self.box2.setValue(min(n))
            self.box3.setValue(sum(n) / n.__len__())
            w = sum(n)
            e = min(n)
            r = max(n)

        except Exception:
            self.myLabel.setText(f'В файле {s} содержатся некорректные данные')
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
