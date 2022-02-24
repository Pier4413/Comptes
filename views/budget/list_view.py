from typing import List
from PyQt6.QtWidgets import QListWidget, QWidget

from classes.elements.budget import Budget as BudgetModele
from views.budget.list_item import BudgetListWidgetItem

class BudgetListWidget(QListWidget):
    """
        Cette classe correspond a la liste des budgets disponibles

        :author: Panda <panda@delmasweb.net>
        :date: 24 Fevrier 2022
        :version: 1.0 
    """

    def __init__(self, parent: QWidget = None, budgets : List[BudgetModele] = list()) -> None:
        """
            Constructeur

            :param parent: Optional; Default : None; Le parent de ce widget
            :type parent: QWidget
            :param budgets: Optional; Default : list(); La liste des budgets que l'on souhaite afficher
            :type budgets: List[BudgetModele]
        """
        super().__init__(parent)

        self.budgets = budgets

        for b in self.budgets:
            BudgetListWidgetItem(self, b)
