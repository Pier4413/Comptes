from PyQt6.QtWidgets import QComboBox, QWidget, QHBoxLayout
from classes.sql.compte import Compte as CompteSQL
from classes.elements.compte import Compte as CompteModele
import i18n

from modules.settings.settings import Settings

class FenetreComptes(QComboBox):

    def __init__(self,  parent : QWidget = None):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.comptesSQL = CompteSQL(Settings.get_instance().get('Database', 'filename', 'comptes.db'))
        listecompte=self.comptesSQL.select_all()

        for row in listecompte:
            self.cb.addItem(row.libelle)

        layout.addWidget(self.cb)
        self.setLayout(layout)
