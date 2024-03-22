from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from MainWindow import Ui_MainWindow # Импорт сгенерированого файла
import sys

class MWindow(QtWidgets.QMainWindow):
    def __init__(self):
        #Работа в MainWindow
        super(MWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def application():
    app = QtWidgets.QApplication(sys.argv)
    window = MWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    application()