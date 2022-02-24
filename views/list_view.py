from PyQt6.QtWidgets import QWidget, QListWidget, QListWidgetItem

class ListWidget(QListWidget):
    """
        Cette classe correspond a la liste des budgets disponibles

        :author: Panda <panda@delmasweb.net>
        :date: 24 Fevrier 2022
        :version: 1.0 
    """

    def __init__(self, parent: QWidget = None) -> None:
        """
            Constructeur

            :param parent: Optional; Default : None; Le parent de ce widget
            :type parent: QWidget
            :param budgets: Optional; Default : list(); La liste des budgets que l'on souhaite afficher
            :type budgets: List[BudgetModele]
        """
        super().__init__(parent)

    def add_item(self, item : QWidget) -> None:
        temp = QListWidgetItem(self)
        self.addItem(temp)
        temp.setSizeHint(item.minimumSizeHint())
        self.setItemWidget(temp, item)