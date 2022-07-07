import pytest
from classes.elements.compte import Compte
from classes.elements.operation import Operation

class TestCompte():
    """
        Cette classe est un test unitaire pour la classe Compte modele

        :author: Mathsgiver <mathsgiver@gmail.com>
        :date: 21 Fevrier 2022
        :version: 1.0
    """

    def setup_method(self) -> None:
        self.compte = Compte(
                libelle="Mon miserable compte",
                id=1,
                solde=-6.66
            )

    def test_libelle(self):
        assert self.compte.libelle == "Mon miserable compte", "Attendu : Mon miserable compte"

    def test_id(self):
        assert self.compte.id == 1, "Attendu : 1"

    def test_solde(self):
        assert self.compte.solde == -6.66, "Attendu : -6.66"

    def test_recalcule_solde(self):
        self.compte.operation = [
            Operation(montant=-2),
            Operation(montant=-8.3),
            Operation(montant=10)
        ]
        self.compte.recalcule_solde()
        assert self.compte.solde == -6.96, "Attendu : -6.96"