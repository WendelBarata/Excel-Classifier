import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from UI_py.ExcelClassifier import Ui_MainWindow


class ExcelClassifier(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = ExcelClassifier()
    mainwindow.show()
    sys.exit(app.exec())
