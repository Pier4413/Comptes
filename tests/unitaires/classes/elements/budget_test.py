import unittest
from classes.elements.budget import Budget

class BudgetTest(unittest.TestCase):
    """
        Cette classe est un test unitaire pour la classe Budget modele

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def setUp(self) -> None:
        super().setUp()
        self.budget = Budget(
                libelle="Mon beau libelle",
                id=1,
                init=15,
                courant=20,
                depense=3
            )

    def test_libelle(self):
        self.assertEqual(self.budget.libelle, "Mon beau libelle", "Attendu : Mon beau libelle")

    def test_id(self):
        self.assertEqual(self.budget.id, 1, "Attendu : 1")

    def test_init(self):
        self.assertEqual(self.budget.init, 15, "Attendu : 15")
        
    def test_courant(self):
        self.assertEqual(self.budget.courant, 20, "Attendu : 20")

    def test_depense(self):
        self.assertEqual(self.budget.depense, 3, "Attendu : 3")