from typing import List
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
        """
            Cette fonction ajoute un item a la liste

            :param item: L'item a ajouter (doit etre un QWidget ou en herite)
            :type item: QWidget
        """
        temp = QListWidgetItem(self)
        self.addItem(temp)
        temp.setSizeHint(item.minimumSizeHint())
        self.setItemWidget(temp, item)

    def add_items(self, items : List[QWidget]) -> None:
        """
            Ajoute beaucoup d'items a la liste

            :param items: La liste des items a ajouter
            :type items: List[QWidget]
        """
        for item in items:
            self.add_item(item)

    def delete_item(self, row : int) -> None:
        """
            Supprime un item de la liste

            :param row: Le numero de l'item
            :type row: int
        """
        self.takeItem(row)

    def clear_list(self) -> None:
        """
            Nettoie integralement la liste en la vidant
        """
        for i in range(self.count() - 1, -1, -1):
            self.takeItem(i)

    def update_items(self, new_items : List[QWidget]) -> None:
        """
            Remplace la liste courante par la nouvelle liste fournie en parametre

            :param new_items: La nouvelle liste d'items
            :type new_items: List[QWidget]
        """
        return # On evite cette fonction car elle ne marche comme je le voudrais
        # BUG : Cette fonction ne marche pas mais fait s'arreter l'application
        self.clear_list()
        self.add_items(new_items)
