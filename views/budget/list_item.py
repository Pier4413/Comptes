from PyQt6.QtWidgets import QListWidgetItem, QWidget

from classes.elements.budget import Budget as BudgetModele

class BudgetListWidgetItem(QListWidgetItem):
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
        self.setText(budget)