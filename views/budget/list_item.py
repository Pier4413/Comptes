import i18n

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLineEdit, QLabel, QHBoxLayout, QWidget, QPushButton

from classes.elements.budget import Budget as BudgetModele

from modules.logger.logger import Logger
class BudgetListWidgetItem(QWidget):
    """
        Cette classe represente un item de la liste de budget

        :author: Panda <panda@delmasweb.net>
        :date: 24 Fevrier 2022
        :version: 1.0
    """

    """
        pyqtSignal a envoye quand on met a jour le montant initial
    """
    update_init = pyqtSignal(float, int)

    """
        pyqtSignal a envoye quand on met a jour le libelle
    """
    update_libelle = pyqtSignal(str, int)

    """
        pyqtSignal a envoye quand on supprime un budget
    """
    delete_budget = pyqtSignal(int)

    def __init__(self, parent : QWidget = None, id : int = 0, libelle : str = None, montant_init : float = 0, montant_depense : float = 0, montant_courant : float = 0):
        """
            Constructeur

            :param parent: Optional; Default : None; Le parent de ce widget
            :type parent: QWidget
            :param budget: Optional; Default : None; Le modele du budget
            :type budget: BudgetModele
            :param row_pos: Optional; Default : 0; Le numero de la ligne
            :type row_pos: int
        """
        super().__init__(parent)

        # On cree le layout necessaire
        self.h_box = QHBoxLayout(self)

        # On cree les widgets
        self.id = id
        self.libelle = QLineEdit(libelle)
        self.init = QLineEdit(str(montant_init))
        self.depense = QLabel(str(montant_depense))
        self.restant = QLabel(str(montant_courant))
        self.delete = QPushButton(i18n.t("translate.delete"))

        # On ajoute les evenements necessaire
        self.libelle.editingFinished.connect(self.update_budget_libelle_f)
        self.init.editingFinished.connect(self.update_init_f)
        self.delete.clicked.connect(self.delete_budget_f)

        # On ajoute les widgets au layout
        self.h_box.addWidget(self.libelle)
        self.h_box.addWidget(self.init)
        self.h_box.addWidget(self.depense)
        self.h_box.addWidget(self.restant)
        self.h_box.addWidget(self.delete)

        # Puis on set le layout pour cet item
        self.setLayout(self.h_box)

    def update_budget_libelle_f(self) -> None:
        """
            Cette fonction met a jour le budget avec un nouveau libelle
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Libelle de budget mis a jour : {self.libelle.text()}")
        
        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_libelle.emit(self.libelle.text(), self.id)

    def update_init_f(self) -> None:
        """
            Cette fonction met a jour le budget avec le nouveau montant initial
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Montant init de budget mis a jour : {self.libelle.text()}")

        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_init.emit(float(self.init.text()), self.id)

    def delete_budget_f(self) -> None:
        """
            Cette fonction efface un budget
        """
        # On emet l'evenement de suppression pour la base de donnees
        self.delete_budget.emit(self.id)
