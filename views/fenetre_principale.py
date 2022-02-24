from PyQt6.QtCore import QSize
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import QMainWindow, QWidget

from views.menu_bar import MenuBar
from views.tabs_principal import Tabs

from modules.logger.logger import Logger

class FenetrePrincipale(QMainWindow):
    """
        Cette classe correspond à la fenetre principale de l'application

        :author: Panda <panda@delmasweb.net>
        :date: 22 Fevrier 2022
        :version: 1.0
    """

    def MINIMUM_SIZE() -> QSize:
        """
            Fonction permettant de simuler une variable statique pour la taille minimale

            :return: La valeur statique
            :rtype: int
        """
        return QSize(800, 800)

    def __init__(self, parent : QWidget = None, app_name : str = "Comptes", 
        x : int = 50, y : int = 50, width: int = 1000, height: int = 1000) -> None:
        """
            Constructor

            :param parent: Optional; Default : None; Le parent de cette fenetre
            :type parent: QWidget
            :param app_name: Optional; Default : "Comptes"; Le nom de l'application
            :type app_name: str
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

        self.real_x = x
        self.real_y = y
        self.real_width = width
        self.real_height = height

        self.setMinimumSize(FenetrePrincipale.MINIMUM_SIZE())
        
        self.setWindowTitle(app_name)
        self.setGeometry(x, y, width, height)
        self.setMenuBar(MenuBar())
        
        self.tabs = Tabs(parent=self)

        self.show()

    def resizeEvent(self, a0: QResizeEvent) -> None:
        """
            Surcharge de la fonction resizeEvent du parent pour pouvoir redimensionner nos elements et ajouter des controles sur la taille min et max

            :param a0: L'evenement de redimensionnement
            :type a0: QResizeEvent
            :override:
        """
        super().resizeEvent(a0)
        self.real_width = a0.size().width()
        self.real_height = a0.size().height()
        Logger.get_instance().debug(f"Taille de la fenetre : {self.real_width}, {self.real_height}")
        self.tabs.change_size(x=5,y=25,width=self.real_width-5, height=self.real_height-27)