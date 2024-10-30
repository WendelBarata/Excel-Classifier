import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit
from PySide6.QtCore import Signal, QEvent, QObject
from UI_py.ExcelClassifier import Ui_MainWindow
from excel_manipulations import split_excel_by_column, common_columns
from pathlib import Path


class ExcelClassifier(QMainWindow, Ui_MainWindow):
    statusMessage = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Set initial values
        self.leExcelInputFolder.setReadOnly(True)
        self.leExcelFolderDest.setReadOnly(True)
        self.leStatusBar.setReadOnly(True)

        # Connect the buttons
        self.btnExcelInputFolder.clicked.connect(
            lambda: self.getExcelFolder(self.leExcelInputFolder))
        self.btnExcelFolderDest.clicked.connect(
            lambda: self.getExcelFolder(self.leExcelFolderDest))
        self.btnSplitExcel.clicked.connect(self.splitExcel)

        # Change value in Line edit based on the selected item in the combobox
        self.cbColumnTitle.currentTextChanged.connect(
            self.leColumnTitle.setText)

        # Connect the status message
        self.statusMessage.connect(self.setStatusMessage)

        # Install event filters
        self.leColumnTitle.installEventFilter(self)

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

        if widget == self.leExcelInputFolder:
            # Set the columns as a values to cbColumnTitle
            columns = common_columns(Path(folder), self.statusMessage)
            self.cbColumnTitle.clear()
            self.cbColumnTitle.addItems(columns)

    def splitExcel(self):
        """
        Method for splitting the excel file by column
        """
        # Get the folder paths
        inputFolder = self.leExcelInputFolder.text()
        outputFolder = self.leExcelFolderDest.text()
        column = self.leColumnTitle.text()

        # Check if the folder paths are empty
        if inputFolder == "" or outputFolder == "" or column == "":
            self.leStatusBar.setText("Please fill in all the fields")
            return

        # Split the excel files
        success = split_excel_by_column(Path(inputFolder),
                                        Path(outputFolder), column,
                                        self.statusMessage)

        # Clear the fields
        if success:
            self.clearFields()

    def setStatusMessage(self, message: str):
        """
        Method to set the status message

        Parameters:
            message (str): The message to display
        """
        self.leStatusBar.setText(message)

    def clearFields(self):
        """
        Method to clear the fields
        """
        self.leExcelInputFolder.clear()
        self.leExcelFolderDest.clear()
        self.leColumnTitle.clear()

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        '''
        Method to filter the events. This method is used to change the
        border color of the QFrame when the QLineEdit is focused or not.

        Parameters:
            obj (QObject): The object that the event is being filtered for
            event (QEvent): The event that is being filtered

        Returns:
            bool: True if the event is filtered, False otherwise
        '''
        if obj == self.leColumnTitle:
            if event.type() == QEvent.FocusIn:
                parent = obj.parent()
                if parent:
                    parent.setStyleSheet(f"QFrame#{parent.objectName()}"
                                         "{background: transparent;"
                                         "border: 1px solid rgb(23, 83, 104);"
                                         "border-radius: 4px}")
            elif event.type() == QEvent.FocusOut:
                parent = obj.parent()
                if parent:
                    parent.setStyleSheet(f"QFrame#{parent.objectName()}"
                                         "{background: transparent;"
                                         "border: 1px solid rgba(23, 83, 104, 0.3)" # noqa
                                         ";border-radius: 4px}")

        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = ExcelClassifier()
    mainwindow.show()
    sys.exit(app.exec())
