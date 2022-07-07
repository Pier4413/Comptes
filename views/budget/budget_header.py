from typing import List
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QWidget, QSizePolicy, QHBoxLayout

from views.budget import LIBELLE_EXPANSION, COURANT_EXPANSION, DEPENSE_EXPANSION, INIT_EXPANSION, SUPPR_EXPANSION, EXPANSION_POLICY, ALIGNEMENT_POLICY

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
            raise Exception("La taille de l'en-tete des budgets ne correspond pas. Attendu 5")
        
        # self.
        # On commence par le libelle
        libelle = QLabel(headers[0])
        libelle.setStyleSheet('background-color: aqua')
        libelle.setSizePolicy(EXPANSION_POLICY(), EXPANSION_POLICY())
        libelle.setAlignment(ALIGNEMENT_POLICY())
        h_box.addWidget(libelle, LIBELLE_EXPANSION())

        # Puis le init
        init = QLabel(headers[1])
        init.setStyleSheet('background-color: red')
        init.setSizePolicy(EXPANSION_POLICY(), EXPANSION_POLICY())
        init.setAlignment(ALIGNEMENT_POLICY())
        h_box.addWidget(init, INIT_EXPANSION())

        # Puis la depense
        depense = QLabel(headers[2])
        depense.setStyleSheet('background-color: yellow')
        depense.setSizePolicy(EXPANSION_POLICY(), EXPANSION_POLICY())
        depense.setAlignment(ALIGNEMENT_POLICY())
        h_box.addWidget(depense, DEPENSE_EXPANSION())

        # Puis le courant
        courant = QLabel(headers[3])
        courant.setStyleSheet('background-color: blue')
        courant.setSizePolicy(EXPANSION_POLICY(), EXPANSION_POLICY())
        courant.setAlignment(ALIGNEMENT_POLICY())
        h_box.addWidget(courant, COURANT_EXPANSION())

        # Puis la suppression
        suppr = QLabel(headers[4])
        suppr.setStyleSheet('background-color: pink')
        suppr.setSizePolicy(EXPANSION_POLICY(), EXPANSION_POLICY())
        suppr.setAlignment(ALIGNEMENT_POLICY())
        h_box.addWidget(suppr, SUPPR_EXPANSION())