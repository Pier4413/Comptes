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

    def testLibelle(self):
        self.assertEquals(self.budget.libelle, "Mon beau libelle", "Attendu : Mon beau libelle")

    def testId(self):
        self.assertEquals(self.budget.id, 1, "Attendu : 1")

    def testInit(self):
        self.assertEquals(self.budget.init, 15, "Attendu : 15")
        
    def testCourant(self):
        self.assertEquals(self.budget.courant, 20, "Attendu : 20")

    def testDepense(self):
        self.assertEquals(self.budget.depense, 3, "Attendu : 3")