from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt5.QtWidgets import QHBoxLayout
import sys
from src.ui.interface import get_widget

if __name__ == "__main__":
    appctxt = ApplicationContext()
    app = QApplication(sys.argv)
    w = get_widget()
    w.show()
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)