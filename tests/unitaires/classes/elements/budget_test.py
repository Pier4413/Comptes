import pytest
from classes.elements.budget import Budget
from classes.elements.operation import Operation

class TestBudget():
    """
        Cette classe est un test unitaire pour la classe Budget modele

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def setup_method(self) -> None:
        self.budget = Budget(
                libelle="Mon beau libelle",
                id=1,
                init=15,
                courant=20,
                depense=3
            )

    def test_libelle(self):
        assert self.budget.libelle == "Mon beau libelle", "Attendu : Mon beau libelle"

    def test_id(self):
        assert self.budget.id == 1, "Attendu : 1"

    def test_init(self):
        assert self.budget.init == 15, "Attendu : 15"
        
    def test_courant(self):
        assert self.budget.courant == 20, "Attendu : 20"

    def test_depense(self):
        assert self.budget.depense == 3, "Attendu : 3"

    def test_recalcule_depense(self):
        self.budget.operations = [
            Operation(montant=-10),
            Operation(montant=-20)
        ]
        self.budget.recalcule_depense()
        assert self.budget.depense == 33, "Attendu : 33"

    def test_recalcule_courant(self):
        self.budget.recalcule_courant()
        assert self.budget.courant == 12