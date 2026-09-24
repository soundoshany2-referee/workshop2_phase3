from PySide6.QtWidgets import QWidget
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtCore import QUrl, QObject

from pathlib import Path


def get_asset(file_name: str) -> str:
    """Returns the absolute path to a resource file."""

    assets_folder = Path(__file__).parent.resolve()

    return str(assets_folder / file_name)


class StatusWidget(QQuickWidget):

    def __init__(
        self,
        widget_filepath: str,
        data_bridge: QObject | None = None,
        parent: QWidget | None = None
    ):
        super().__init__(parent)

        if data_bridge is not None:
            self.setInitialProperties({"clockData": data_bridge})

            self.setSource(
                QUrl.fromLocalFile(get_asset(widget_filepath))
            )

            self.setResizeMode(
                QQuickWidget.ResizeMode.SizeRootObjectToView
            )
