import i18n

from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout

from views.menu_bar import MenuBar
from views.tabs_principal import Tabs

class FenetrePrincipale(QMainWindow):
    """
        Cette classe correspond à la fenetre principale de l'application

        :author: Panda <panda@delmasweb.net>
        :date: 22 Fevrier 2022
        :version: 1.0
    """

    """
        Hauteur minimale de notre application

        :type: int
        :meta static:
    """
    MINIMUM_HEIGHT = 800

    """
        Largeur minimale de notre application

        :type: int
        :meta static:
    """
    MINIMUM_WIDTH = 800

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

        self.setMinimumSize(FenetrePrincipale.MINIMUM_WIDTH, FenetrePrincipale.MINIMUM_HEIGHT)
        
        self.setWindowTitle(app_name)
        self.setGeometry(x, y, width, height)
        self.setMenuBar(MenuBar())
        
        self.tabs = Tabs(self, x=self.real_x-40,y=self.real_y-25,width=self.real_width*0.985, height=self.real_height*0.97)

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
        self.tabs.change_size(x=self.real_x-40,y=self.real_y-25,width=self.real_width*0.985, height=self.real_height*0.97)