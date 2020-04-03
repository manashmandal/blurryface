from PyQt5.QtWidgets import (QWidget, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QListWidget )
from src.ui.filedialog import FileDialog
from src.ui.filelist import FileList

def get_widget():
    MainWidget = QWidget()

    SourceDialog = FileDialog(title="source", button_text="Load Images From")
    DestinationDialog = FileDialog(title="destination", button_text="Write Images To")

    hboxLayout = QHBoxLayout()
    vboxLayout = QVBoxLayout()
    mainhBoxLayout = QHBoxLayout()
    buttonVBoxLayout = QVBoxLayout()

    fileList = FileList()
    SourceDialog.connect(fileList.get_directory)
    DestinationDialog.connect(fileList.setDestinationDirectory)

    hboxLayout.addWidget(fileList)
    buttonVBoxLayout.addWidget(SourceDialog)
    buttonVBoxLayout.addWidget(DestinationDialog)
    hboxLayout.addLayout(buttonVBoxLayout)

    mainhBoxLayout.addLayout(hboxLayout)

    MainWidget.setLayout(mainhBoxLayout)

    return MainWidget