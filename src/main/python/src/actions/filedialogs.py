from PyQt5.QtCore import pyqtSlot

@pyqtSlot(str)
def get_source_destination(directory):
    print("The direcotory is ", directory)
    print(directory)