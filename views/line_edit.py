from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFocusEvent
from PyQt6.QtWidgets import QLineEdit

class LineEdit(QLineEdit):

    """
        Signal emis lorsque l'on perd le focus
    """
    focus_losed = pyqtSignal()

    def focusOutEvent(self, a0: QFocusEvent) -> None:
        """
            Reimplementation de la fonction focusOutEvent pour detecter la perte de focus
        """
        self.focus_losed.emit()
        return super().focusOutEvent(a0)