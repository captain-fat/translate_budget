import requests
import json
from PyQt5.QtWidgets import QMainWindow, QApplication
from main_window import Ui_MainWindow
import sys

class my_main_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(my_main_window, self).__init__(parent)
        self.setupUi(self)
        self.btn_translate.clicked.connect(self.output_result)
        self.btn_reset.clicked.connect(self.get_input_clear)

    def get_input_words(self):
        self.input_words = self.input_box.toPlainText()

    def get_input_clear(self):
        self.input_box.clear()
        self.output_box.clear()

    def output_result(self):
        self.get_input_words()
        output_box = translate(self.input_words)
        self.output_box.setText(output_box)


def translate(keyword):
    url = 'https://fanyi.baidu.com/sug'

    data = {
        'kw' : keyword
    }

    res = requests.post(url, data = data)

    str_json = res.text

    myjson = json.loads(str_json)
    info = myjson['data'][0]['v']
    return info


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = my_main_window()
    myWin.show()
    sys.exit(app.exec())