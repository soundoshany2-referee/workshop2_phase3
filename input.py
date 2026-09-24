from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QIntValidator


class Input(QWidget):

    time_entered = Signal(int, int, int)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.hour_input = QLineEdit(self)
        self.min_input = QLineEdit(self)
        self.sec_input = QLineEdit(self)

        self.hour_input.setValidator(QIntValidator(0, 11, self))
        self.min_input.setValidator(QIntValidator(0, 59, self))
        self.sec_input.setValidator(QIntValidator(0, 59, self))

        self.confirm_button = QPushButton("Confirm", self)

        layout = QVBoxLayout(self)

        inputs_layout = QHBoxLayout()
        inputs_layout.addWidget(self.hour_input)
        inputs_layout.addWidget(self.min_input)
        inputs_layout.addWidget(self.sec_input)

        layout.addLayout(inputs_layout)
        layout.addWidget(self.confirm_button)

        self.confirm_button.clicked.connect(self._confirm_input)

    def _confirm_input(self):
        hour = int(self.hour_input.text())
        minute = int(self.min_input.text())
        second = int(self.sec_input.text())

        self.time_entered.emit(hour, minute, second)
