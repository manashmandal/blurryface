from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt5.QtWidgets import QHBoxLayout
import sys
from src.ui.interface import get_widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = get_widget()
    w.show()
    sys.exit(app.exec_())