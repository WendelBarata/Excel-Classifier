import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit
from UI_py.ExcelClassifier import Ui_MainWindow


class ExcelClassifier(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Set initial values
        self.leExcelInputFolder.setReadOnly(True)
        self.leExcelFolderDest.setReadOnly(True)

        # Connect the buttons
        self.btnExcelInputFolder.clicked.connect(
            lambda: self.getExcelFolder(self.leExcelInputFolder))
        self.btnExcelFolderDest.clicked.connect(
            lambda: self.getExcelFolder(self.leExcelFolderDest))

    def getExcelFolder(self, widget: QLineEdit):
        """
        Method for selecting the folder containing the excel files

        Parameters:
        widget (QLineEdit): The QLineEdit widget to display the folder path
        """
        # Select a folder containing the excel files
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")

        if folder == "":
            return

        widget.setText(folder)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = ExcelClassifier()
    mainwindow.show()
    sys.exit(app.exec())
