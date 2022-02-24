from PyQt6.QtWidgets import QMenuBar, QWidget, QMenu

from modules.logger.logger import Logger

class MenuBar(QMenuBar):
    """
        Cette classe represente la barre de menus de notre application

        :author: Panda <panda@delmasweb.net>
        :date: 24 Fevrier 2022
        :version: 1.0
    """

    def __init__(self, parent: QWidget = None) -> None:
        """
            Constructeur

            :param parent: Optional; Default : None; Le parent de cette fenetre
            :type parent: QWidget
        """
        super().__init__(parent)

        # Ajout un menu dans la menu bar
        self.firstMenu = QMenu("Fichier", self)

        # Ajoute une action et un trigger sur cette action dans le menu precedemment cree
        self.firstAction = self.firstMenu.addAction("&Open File")
        self.firstAction.triggered.connect(self.openFile)

        # Ajout le menu a la menu bar
        self.addMenu(self.firstMenu)

    def openFile(self) -> None:
        """
            Cette fonction ouvre une base de données
        """
        Logger.get_instance().info("TEST TRIGGERED")
        