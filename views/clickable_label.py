from PyQt6.QtGui import QMouseEvent
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QLabel

class ClickableLabel(QLabel):

    """
        Signal de clic sur le label
    """
    clicked = pyqtSignal()

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        """
            Quand on a clic souris cette evenement sera appele donc on emet l'evenement de clic
        """
        if(ev.button() == Qt.MouseButton.LeftButton):
            self.clicked.emit()