from PyQt5.QtWidgets import QFileDialog, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot

class FileDialog(QWidget):
    def __init__(self, title, button_text, parent=None):
        super(FileDialog, self).__init__(parent)
        self.title = title
        self.button_text = button_text
        self.hboxLayout = QHBoxLayout()
        self.button = QPushButton(self.button_text)
        self.fileDialog = QFileDialog()
        self.fileDialog.hide()
        self.fileDialog.setOption(QFileDialog.ShowDirsOnly)
        self.fileDialog.setFileMode(QFileDialog.DirectoryOnly)
        self.hboxLayout.addWidget(self.fileDialog)
        self.hboxLayout.addWidget(self.button)
        self.button.clicked.connect(lambda : self.fileDialog.show())
        self.fileDialog.directoryEntered.connect(self.get_directory)
        self.setLayout(self.hboxLayout)

    @pyqtSlot(str)
    def get_directory(self, entered_directory):
        print("Entered directory ", entered_directory)


    def connect(self, function):
        self.fileDialog.directoryEntered.connect(function)
