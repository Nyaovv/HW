import sys
from urllib.request import urlopen

from lxml import etree
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton,
    QVBoxLayout
)
from PyQt5.Qt import Qt


class Course(QObject):
    CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

    def get(self):
        with urlopen(self.CBR_URL) as r:
            tree = etree.parse(r)
            value = tree.xpath('*[@ID="R01235"]/Value')[0].text
            return float(value.replace(',', '.'))


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initSignals()
        self._initLayouts()




    def _initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmountEdit = QDoubleSpinBox(self)
        self.srcAmountEdit.setMaximum(999999999)
        self.resultAmountEdit = QDoubleSpinBox(self)
        self.resultAmountEdit.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)
        self.clearBtn = QPushButton('Очистить', self)




    def _initSignals(self):
        self.convertBtn.clicked.connect(self.onClickConvertBtn)
        self.clearBtn.clicked.connect(self.onClickClearBtn)

    def _initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)

        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmountEdit)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmountEdit)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.clearBtn)

        self.setCentralWidget(w)

    def onClickConvertBtn(self):
        value_r = self.srcAmountEdit.value()
        value_d = self.resultAmountEdit.value()

        if (value_r and value_d) or not (value_r and value_d):
            self.convertBtn.setEnabled(False)
            self.convertBtn.setEnabled(True)

        if value_r and not value_d:
            self.resultAmountEdit.setValue(value_r / Course().get())

        if value_d and not value_r:
            self.srcAmountEdit.setValue(value_d * Course().get())

    def onClickClearBtn(self):
        value_r = self.srcAmountEdit.value()
        value_d = self.resultAmountEdit.value()

        self.resultAmountEdit.setValue(0)
        self.srcAmountEdit.setValue(0)

    def keyPressEvent(self, k):
        if k.key() == Qt.Key_Return: # конвертировать - Enter
            self.onClickConvertBtn()
        if k.key() == Qt.Key_Escape: # очистить - Escape
            self.onClickClearBtn()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    converter = MainWindow()
    converter.show()

    sys.exit(app.exec_())
