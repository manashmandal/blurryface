from PyQt5.QtWidgets import QListWidget, QWidget, QHBoxLayout, QPushButton, QProgressBar, QCheckBox, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import pyqtSlot, Qt
import os
from src.imageprocessing.auto_blur_image import blurit

class FileList(QWidget):
    def __init__(self, parent=None):
        super(FileList, self).__init__(parent)
        self.listWidget = QListWidget()
        self.processButton = QPushButton("process")
        self.progress = QProgressBar()
        self.showImage = QCheckBox(text="Show Processed Image")
        self.textProgress = QLabel("Idle")
        self.thresholdSlider = QSlider(Qt.Horizontal)
        self.thresholdText = "Threshold : {threshold}"
        self.thresholdLabel = QLabel(self.thresholdText.format(threshold=30))

        self.thresholdSlider.setTickPosition(QSlider.TicksBelow)
        self.thresholdSlider.setRange(0, 100)
        self.thresholdSlider.setTickInterval(10)
        self.thresholdSlider.setValue(30)
        self.thresholdSlider.sliderMoved.connect(lambda position: self.thresholdLabel.setText(self.thresholdText.format(threshold=position)))
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.listWidget)
        vboxLayout.addWidget(self.processButton)
        vboxLayout.addWidget(self.progress)
        vboxLayout.addWidget(self.textProgress)
        vboxLayout.addWidget(self.thresholdLabel)
        vboxLayout.addWidget(self.thresholdSlider)
        self.setLayout(vboxLayout)
        self.processButton.clicked.connect(self.blurimage)
        self.selectedDirectory = ""
        self.destinationDirectory = ""


    def blurimage(self):
        self.progress.setValue(0)
        self.textProgress.setText("Idle...")
        threshold = float(self.thresholdSlider.value()) / 100.0

        items = [
            os.path.join(self.selectedDirectory, self.listWidget.item(index).text()) for index in range(self.listWidget.count())
        ]

        self.progress.setRange(0, len(items))
        #
        for idx, item in enumerate(items):
            self.textProgress.setText(f"Processing {item}")
            blurit(item, writepath=self.destinationDirectory, threshold=threshold, showimage=self.showImage.isChecked())
            self.progress.setValue(idx+1)

        self.textProgress.setText("Done!")


    @pyqtSlot(str)
    def get_directory(self, directory):
        self.listWidget.clear()
        for file in os.listdir(directory):
            self.selectedDirectory = directory
            if file.lower().endswith(".jpg") or file.lower().endswith(".png"):
                self.listWidget.addItem(file)


    @pyqtSlot(str)
    def setDestinationDirectory(self, directory):
        self.destinationDirectory = directory