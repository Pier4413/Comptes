import i18n

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLineEdit, QLabel, QHBoxLayout, QWidget, QPushButton

from classes.elements.compte import Compte as CompteModele

from modules.logger.logger import Logger
class CompteListWidgetItem(QWidget):
    """
        Cette classe represente un item de la liste de compte

        :author: Mathsgiver <mathsgiver@gmail.com>
        :date: 05 Mars 2022
        :version: 1.0
    """

    """
        pyqtSignal a envoye quand on met a jour le solde
    """
    update_solde = pyqtSignal(float, int)

    """
        pyqtSignal a envoye quand on met a jour le libelle
    """
    update_libelle = pyqtSignal(str, int)

    """
        pyqtSignal a envoye quand on supprime un compte
    """
    delete_compte = pyqtSignal(int)

    def __init__(self, parent : QWidget = None, id : int = 0, libelle : str = None, solde : float = 0):
        """
            Constructeur

            :param parent: Optional; Default : None; Le parent de ce widget
            :type parent: QWidget
            :param compte: Optional; Default : None; Le modele du compte
            :type compte: CompteModele
            :param row_pos: Optional; Default : 0; Le numero de la ligne
            :type row_pos: int
        """
        super().__init__(parent)

        # On cree le layout necessaire
        self.h_box = QHBoxLayout(self)

        # On cree les widgets
        self.id = id
        self.libelle = QLineEdit(libelle)
        self.solde = QLineEdit(str(solde))
        self.delete = QPushButton(i18n.t("translate.delete"))

        # On ajoute les evenements necessaire
        self.libelle.editingFinished.connect(self.update_compte_libelle_f)
        self.solde.editingFinished.connect(self.update_solde_f)
        self.delete.clicked.connect(self.delete_compte_f)

        # On ajoute les widgets au layout
        self.h_box.addWidget(self.libelle)
        self.h_box.addWidget(self.solde)
        self.h_box.addWidget(self.delete)

        # Puis on set le layout pour cet item
        self.setLayout(self.h_box)

    def update_compte_libelle_f(self) -> None:
        """
            Cette fonction met a jour le compte avec un nouveau libelle
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Libelle de compte mis a jour : {self.libelle.text()}")
        
        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_libelle.emit(self.libelle.text(), self.id)

    def update_solde_f(self) -> None:
        """
            Cette fonction met a jour le compte avec le nouveau montant initial
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Solde du compte mis a jour : {self.solde.text()}")

        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_init.emit(float(self.solde.text()), self.id)

    def delete_compte_f(self) -> None:
        """
            Cette fonction efface un compte
        """
        # On emet l'evenement de suppression pour la base de donnees
        self.delete_compte.emit(self.id)
