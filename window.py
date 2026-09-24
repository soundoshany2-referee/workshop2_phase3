from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from workshop.data import MyData
from workshop.status import StatusWidget
from workshop.input import Input


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.data = MyData()

        self.status_widget = StatusWidget(
            "clock.qml",
            self.data
        )

        self.input = Input()

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        layout.addWidget(self.status_widget)
        layout.addWidget(self.input)

        self.setCentralWidget(central_widget)

        self.input.time_entered.connect(self._set_time)

        self.show()

    def _set_time(self, hour: int, minute: int, second: int):
        self.data.hours = hour
        self.data.mins = minute
        self.data.secs = second
