import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class ExcelClassifier(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = ExcelClassifier()
    mainwindow.show()
    sys.exit(app.exec())
