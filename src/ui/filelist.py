from PyQt5.QtWidgets import QListWidget, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSlot
import os
from src.imageprocessing.auto_blur_image import blurit

class FileList(QWidget):
    def __init__(self, parent=None):
        super(FileList, self).__init__(parent)
        self.listWidget = QListWidget()
        self.processButton = QPushButton("process")
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(self.listWidget)
        hboxLayout.addWidget(self.processButton)
        self.setLayout(hboxLayout)
        self.processButton.clicked.connect(self.blurimage)
        self.selectedDirectory = ""


    def blurimage(self):
        if self.listWidget.currentItem():
            item = os.path.join(self.selectedDirectory, self.listWidget.currentItem().text())
            blurit(item)
            print("CURRENT ITEM ", item)

    @pyqtSlot(str)
    def get_directory(self, directory):
        self.listWidget.clear()
        for file in os.listdir(directory):
            self.selectedDirectory = directory
            if file.lower().endswith(".jpg") or file.lower().endswith(".png"):
                self.listWidget.addItem(file)
