from PyQt6.QtWidgets import QMainWindow, QWidget

class FenetrePrincipale(QMainWindow):
    """
        Cette classe correspond à la fenetre principale de l'application

        :author: Panda <panda@delmasweb.net>
        :date: 22 Fevrier 2022
        :version: 1.0
    """

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
        self.setWindowTitle(app_name)
        self.setGeometry(x, y, width, height)
        self.show()