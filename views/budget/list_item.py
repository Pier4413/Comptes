import i18n

from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QLineEdit, QLabel, QHBoxLayout, QWidget, QPushButton, QSizePolicy

from views.clickable_label import ClickableLabel

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
        
        # Creation du libelle et dimensionnement
        self.libelle = ClickableLabel(libelle)
        self.libelle.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.libelle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.libelle.clicked.connect(self.modify_libelle)
        
        #Creation du montant initial
        self.init = ClickableLabel(str(montant_init))
        self.init.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.init.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.init.clicked.connect(self.modify_init)
        
        # Creation du label de montant depense
        self.depense = QLabel(str(montant_depense))

        # Creation du label de montant restant
        self.restant = QLabel(str(montant_courant))

        # Creation du bouton de suppression d'element
        self.delete = QPushButton(i18n.t("translate.delete"))
        self.delete.clicked.connect(self.delete_budget_f)

        # On ajoute les widgets au layout avec des stretchs pour determiner leur taille
        self.h_box.addWidget(self.libelle, 3)
        self.h_box.addWidget(self.init, 2)
        self.h_box.addWidget(self.depense,2)
        self.h_box.addWidget(self.restant,2)
        self.h_box.addWidget(self.delete,1)

        # Puis on set le layout pour cet item
        self.setLayout(self.h_box)

    def modify_libelle(self) -> None:
        """
            Cette fonction transforme le label clickable de libelle en QLineEdit pour le modifier
        """
        
        # On log l'evenement
        Logger.get_instance().debug("Label clicked")

        # On supprime le label
        self.h_box.removeWidget(self.libelle)

        # On cree le line edit
        self.libelle = QLineEdit(self.libelle.text())
        self.libelle.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.libelle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.libelle.setFocus()
        self.libelle.editingFinished.connect(self.update_budget_libelle_f)

        # On l'insere a la place du label
        self.h_box.insertWidget(0, self.libelle, 3)

    def modify_init(self) -> None:
        """
            Cette fonction transforme le label clickable de init en QLineEdit pour le modifier
        """
        
        # On log l'evenement
        Logger.get_instance().debug("Init clicked")

        # On supprime le label
        self.h_box.removeWidget(self.init)

        # On cree le line edit
        self.init = QLineEdit(self.init.text())
        self.init.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.init.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.init.setFocus()
        self.init.editingFinished.connect(self.update_init_f)

        # On l'insere a la place du label
        self.h_box.insertWidget(1, self.init, 2)

    def update_budget_libelle_f(self) -> None:
        """
            Cette fonction met a jour le budget avec un nouveau libelle
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Libelle de budget mis a jour : {self.libelle.text()}")

        # On supprime le line edit
        self.h_box.removeWidget(self.libelle)

        # On cree le label
        self.libelle = ClickableLabel(self.libelle.text())
        self.libelle.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.libelle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.libelle.clicked.connect(self.modify_libelle)

        # On l'insere a la place du line edit
        self.h_box.insertWidget(0, self.libelle, 3)
        
        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_libelle.emit(self.libelle.text(), self.id)

    def update_init_f(self) -> None:
        """
            Cette fonction met a jour le budget avec le nouveau montant initial
        """
        # On ecrit un log pour le debug
        Logger.get_instance().debug(f"Montant init de budget mis a jour : {self.init.text()}")

        # On supprime le line edit
        self.h_box.removeWidget(self.init)

        # On cree le label
        self.init = ClickableLabel(self.init.text())
        self.init.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.init.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.init.clicked.connect(self.modify_init)

        # On l'insere a la place du line edit
        self.h_box.insertWidget(1, self.init, 2)

        # On emet un evenement remonter l'information au parent s'ils le souhaitent
        self.update_init.emit(float(self.init.text()), self.id)

    def delete_budget_f(self) -> None:
        """
            Cette fonction efface un budget
        """
        # On emet l'evenement de suppression pour la base de donnees
        self.delete_budget.emit(self.id)
