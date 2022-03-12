from typing import List
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QWidget, QSizePolicy, QHBoxLayout

class BudgetHeaderItem(QWidget):
    """
        Cette classe est l'en-tete du tableau

        :author: Panda <panda@delmasweb.net>
        :date: 12 Mars 2022
        :version: 1.0
    """

    def __init__(self, parent: QWidget = None, headers : List[str] = list()) -> None:
        """
            Constructeur
        """
        super().__init__(parent)

        # On cree le layout necessaire
        h_box = QHBoxLayout(self)

        if(len(headers) != 5):
            raise Exception("La taille de l'en-tete des budgets ne correspond pas")
        
        # On commence par le libelle
        libelle = QLabel(headers[0])
        libelle.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        libelle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_box.addWidget(libelle, 3)

        # Puis le init
        init = QLabel(headers[1])
        init.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        init.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_box.addWidget(init, 2)

        # Puis la depense
        depense = QLabel(headers[2])
        depense.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        depense.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_box.addWidget(depense, 2)

        # Puis le courant
        courant = QLabel(headers[3])
        courant.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        courant.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_box.addWidget(courant, 2)

        # Puis la suppression
        suppr = QLabel(headers[4])
        suppr.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        suppr.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_box.addWidget(suppr, 2)