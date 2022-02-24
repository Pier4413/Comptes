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
        pyqtSignal a envoye quand on met a jour le budget
    """
    update_budget = pyqtSignal(BudgetModele)

    """
        pyqtSignal a envoye quand on supprime un budget
    """
    delete_budget = pyqtSignal(BudgetModele)

    def __init__(self, parent : QWidget = None, budget : BudgetModele = None):
        """
            Constructeur

            :param parent: Optional; Default : None; Le parent de ce widget
            :type parent: QWidget
            :param budget: Optional; Default : None; Le modele du budget
            :type budget: BudgetModele
        """
        super().__init__(parent)

        # On cree le layout necessaire
        self.h_box = QHBoxLayout(self)

        # On cree les widgets
        self.budget = budget
        self.libelle = QLineEdit(self.budget.libelle)
        self.init = QLineEdit(str(self.budget.init))
        self.depense = QLabel(str(self.budget.depense))
        self.restant = QLabel(str(self.budget.courant))
        self.delete = QPushButton(i18n.t("translate.delete"))

        # On ajoute les evenements necessaire
        self.libelle.editingFinished.connect(self.update_budget_libelle)
        self.init.editingFinished.connect(self.update_init)
        self.delete.clicked.connect(self.delete_budget_f)

        # On ajoute les widgets au layout
        self.h_box.addWidget(self.libelle)
        self.h_box.addWidget(self.init)
        self.h_box.addWidget(self.depense)
        self.h_box.addWidget(self.restant)
        self.h_box.addWidget(self.delete)

        # Puis on set le layout pour cet item
        self.setLayout(self.h_box)

    def update_budget_libelle(self) -> None:
        """
            Cette fonction met a jour le budget avec un nouveau libelle
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Libelle de budget mis a jour : {self.libelle.text()}")
        
        # On change le texte dans le budget courant
        self.budget.libelle = self.libelle.text()

        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_budget.emit(self.budget)

    def update_init(self) -> None:
        """
            Cette fonction met a jour le budget avec le nouveau montant initial
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Montant init de budget mis a jour : {self.libelle.text()}")

        # On met a jour les montants dans le budget courant et l'interface
        self.budget.init = float(self.init.text())
        self.budget.recalcule_depense()
        self.budget.recalcule_courant()
        self.depense.setText(str(self.budget.depense))
        self.restant.setText(str(self.budget.courant))

        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_budget.emit(self.budget)

    def delete_budget_f(self) -> None:
        """
            Cette fonction efface un budget
        """
        self.libelle.deleteLater()
        self.init.deleteLater()
        self.depense.deleteLater()
        self.restant.deleteLater()
        self.delete.deleteLater()
        self.delete_budget.emit(self.budget)
