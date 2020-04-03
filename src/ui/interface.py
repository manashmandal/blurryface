from PyQt5.QtWidgets import (QWidget, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QListWidget )
from src.ui.filedialog import FileDialog
from src.ui.filelist import FileList

def get_widget():
    MainWidget = QWidget()
    # SourceDirDialog = QFileDialog()

    SourceDialog = FileDialog(title="source", button_text="Open Source Directory")
    # DestinationDialog = FileDialog(title="destination", button_text="Open Destination Directory")

    # SourceDirDialog.setOption(QFileDialog.ShowDirsOnly)
    # SourceDirDialog.setFileMode(QFileDialog.DirectoryOnly)
    # SourceDirDialog.hide()
    # SourceDirDialog.directoryEntered.connect(get_source_destination)
    # ShowSourceDialogButton = QPushButton("Load Images From Folder")
    # ShowSourceDialogButton.clicked.connect(lambda : SourceDirDialog.show())
    hboxLayout = QHBoxLayout()
    vboxLayout = QVBoxLayout()

    fileList = FileList()
    SourceDialog.connect(fileList.get_directory)

    hboxLayout.addWidget(fileList)
    hboxLayout.addWidget(SourceDialog)


    # hboxLayout.addWidget(fileList)
    #
    # hboxLayout.addLayout(SourceDialog.hboxLayout)
    # hboxLayout.addLayout(DestinationDialog.hboxLayout)
    # hboxLayout.addWidget(ShowSourceDialogButton)
    # hboxLayout.addWidget(DestinationDirDialog)

    vboxLayout.addLayout(hboxLayout)

    MainWidget.setLayout(vboxLayout)

    return MainWidget