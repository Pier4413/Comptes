from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel

from classes.elements.budget import Budget as BudgetModele

class BudgetListWidgetItem(QWidget):
    """
        Cette classe represente un item de la liste de budget

        :author: Panda <panda@delmasweb.net>
        :date: 24 Fevrier 2022
        :version: 1.0
    """
    def __init__(self, parent : QWidget = None, budget : BudgetModele = None):
        """
            Constructeur

            :param parent: Optional; Default : None; Le parent de ce widget
            :type parent: QWidget
            :param budget: Optional; Default : None; Le modele du budget
            :type budget: BudgetModele
        """
        super().__init__(parent)

        h_box = QHBoxLayout(self)
        button = QPushButton()
        label = QLabel(budget.libelle)

        h_box.addWidget(button)
        h_box.addWidget(label)
        self.setLayout(h_box)
