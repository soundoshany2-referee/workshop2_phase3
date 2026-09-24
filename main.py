from PySide6.QtWidgets import QApplication
from workshop.window import Window
import sys


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
