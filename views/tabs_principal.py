from PyQt6.QtWidgets import QWidget, QTabWidget, QLabel

import i18n

class Tabs(QTabWidget):
    """
        Cette classe permet de definir un element a onglet

        :author: Panda <panda@delmasweb.net>
        :date: 24 Fevrier 2022
        :version: 1.0
    """

    def __init__(self, parent : QWidget = None, x : int = 50, y : int = 50, width: int = 1000, height: int = 1000):
        """
            Constructor
            :param parent: Optional; Default : None; Le parent de cette fenetre
            :type parent: QWidget
            :param x: Optional; Default : 50; Position en X du coin en haut a gauche de la fenetre sur l'ecran (en px)
            :type x: int
            :param y: Optional; Default : 50; Position en Y du coin en haut a gauche de la fenetre sur l'ecran (en px)
            :type y: int
            :param width: Optional; Default : 1000; Largeur de la fenetre (en px)
            :type width: int 
            :param height: Optional; Default : 1000; Hauteur de la fenetre (en px)
            :type height: int
        """
        super().__init__(parent)
        self.setGeometry(x, y, width, height)

        self.comptes = QLabel(i18n.t("translate.init"))
        self.addTab(self.comptes, i18n.t("translate.accounts"))

        self.budgets = QLabel(i18n.t("translate.init"))
        self.addTab(self.budgets, i18n.t("translate.budgets"))