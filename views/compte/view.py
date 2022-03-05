import i18n

from PyQt6.QtWidgets import QGridLayout, QWidget, QPushButton

from views.list_view import ListWidget

class CompteView(QWidget):
    """
        Cette classe est le widget affiche pour la liste view

        :author: Mathsgiver <mathsgiver@gmail.com>
        :date: 05 Mars 2022
        :version: 1.0
    """

    def __init__(self, parent: QWidget = None) -> None:
        """
            Constructeur

            :param parent: Optional; Default : None; Le parent de cette fenetre
            :type parent: QWidget
        """
        super().__init__(parent)

        self.gridLayout = QGridLayout(self)

        self.comptes = ListWidget()
        
        self.gridLayout.addWidget(self.comptes, 1, 0, 1, 10)

        self.add_button = QPushButton(i18n.t("translate.compte.add"))
        self.gridLayout.addWidget(self.add_button, 0, 9, 1, 1)    