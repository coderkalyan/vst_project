import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.main_window import MainUI


def main():
    app = QApplication(sys.argv)

    main_window = QMainWindow(parent=None, flags=Qt.Window)
    main_window_ui = MainUI(window=main_window)
    main_window.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
