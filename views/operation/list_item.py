from msilib.schema import ComboBox
import i18n

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLineEdit, QLabel, QHBoxLayout, QWidget, QPushButton, QComboBox

from classes.elements.operation import Operation as OperationModele

from modules.logger.logger import Logger
class OperationListWidgetItem(QWidget):
    """
        Cette classe represente un item de la liste d'operation

        :author: Mathsgiver <mathsgiver@gmail.com>
        :date: 16 Mars 2022
        :version: 1.0
    """

    """
        pyqtSignal a envoye quand on met a jour le solde
    """
    update_montant = pyqtSignal(float, int)

    """
        pyqtSignal a envoye quand on met a jour le libelle
    """
    update_libelle = pyqtSignal(str, int)

    """
        pyqtSignal a envoye quand on met a jour le compte associe
    """
    update_compte = pyqtSignal(int,int)

    """
        pyqtSignal a envoye quand on met a jour le budget associe
    """
    update_budget = pyqtSignal(int,int)

    """
        pyqtSignal a envoye quand on supprime une operation
    """
    delete_operation = pyqtSignal(int)

    """
        pyqtSignal a envoye quand on verouille une operation
    """
    verouille_operation = pyqtSignal(int)

    """
        pyqtSignal a envoye quand on valide une opération
    """
    valide_operation = pyqtSignal(int)

    """
        pyqtSignal a envoye quand on deroule les comptes disponibles
    """
    read_all_compte = pyqtSignal()

    def __init__(self, parent : QWidget = None, id : int = 0, libelle : str = None, montant : float = 0, compte : int = 0, budget : int = 0):
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
        self.compte = QComboBox(None)
        self.compte.addItem("translate.choose")
        self.budget = QComboBox(None)
        self.montant = QLineEdit(str(montant))
        self.valide = QPushButton(i18n.t("translate.valide"))
        self.verrouille = QPushButton(i18n.t("translate.verrouille"))
        self.delete = QPushButton(i18n.t("translate.delete"))

        # On ajoute les evenements necessaire
        self.libelle.editingFinished.connect(self.update_operation_libelle_f)
        self.montant.editingFinished.connect(self.update_montant_f)
        self.compte.currentIndexChanged.connect(self.update_compte_f)
        self.compte.activated.connect(self.read_all_compte_f)
        self.budget.currentIndexChanged.connect(self.update_budget_f)
        self.valide.clicked.connect(self.valide_operation_f)
        self.verrouille.clicked.connect(self.verrouille_operation_f)
        self.delete.clicked.connect(self.delete_operation_f)

        # On ajoute les widgets au layout
        self.h_box.addWidget(self.compte)
        self.h_box.addWidget(self.budget)
        self.h_box.addWidget(self.libelle)
        self.h_box.addWidget(self.montant)
        self.h_box.addWidget(self.valide)
        self.h_box.addWidget(self.verrouille)
        self.h_box.addWidget(self.delete)

        # Puis on set le layout pour cet item
        self.setLayout(self.h_box)

    def update_operation_libelle_f(self) -> None:
        """
            Cette fonction met a jour l'operation avec un nouveau libelle
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Libelle d'operation mis a jour : {self.libelle.text()}")
        
        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_libelle.emit(self.libelle.text(), self.id)

    def update_montant_f(self) -> None:
        """
            Cette fonction met a jour l'operation avec le nouveau montant
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Montant d'operation mis a jour : {self.montant.text()}")

        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_init.emit(float(self.montant.text()), self.id)

    def update_compte_f(self) -> None:
        """
            Cette fonction met a jour l'operation avec le nouveau compte
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Compte d'operation mis a jour : {self.compte.text()}")

        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_init.emit(float(self.compte.text()), self.id)

    def update_budget_f(self) -> None:
        """
            Cette fonction met a jour l'operation avec le nouveau budget
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Budget d'operation mis a jour : {self.compte.text()}")

        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_init.emit(float(self.budget.text()), self.id)

    def valide_operation_f(self) -> None:
        """
            Cette fonction efface une operation
        """
        # On emet l'evenement de suppression pour la base de donnees
        self.valide_operation.emit(self.id)

    def verrouille_operation_f(self) -> None:
        """
            Cette fonction efface une operation
        """
        # On emet l'evenement de suppression pour la base de donnees
        self.verouille_operation.emit(self.id)

    def delete_operation_f(self) -> None:
        """
            Cette fonction efface une operation
        """
        # On emet l'evenement de suppression pour la base de donnees
        self.delete_operation.emit(self.id)

    def read_all_compte_f(self) -> None:
        """
           Cette fonction recupere la liste des comptes
        """

        self.read_all_compte.emit()
