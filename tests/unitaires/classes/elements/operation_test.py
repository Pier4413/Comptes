import unittest
from classes.elements.operation import Operation

class BudgetTest(unittest.TestCase):
    """
        Cette classe est un test unitaire pour la classe Operation modele

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def setUp(self) -> None:
        super().setUp()
        self.operation = Operation(
            id=1,
            libelle="Ma nouvelle operation",
            montant=10,
            date=50,
            estValide=True,
            estVerrouille=True
        )

    def testId(self) -> None:
        self.assertEqual(self.operation.id, 1, "Attendu : 1")
    
    def testLibelle(self) -> None:
        self.assertEqual(self.operation.libelle, "Ma nouvelle operation", "Attendu : Ma nouvelle operation")

    def testMontant(self) -> None:
        self.assertEqual(self.operation.montant, 10, "Attendu : 10")

    def testDate(self) -> None:
        self.assertEqual(self.operation.date, 50, "Attendu : 50")

    def testEstValide(self) -> None:
        self.assertEqual(self.operation.estValide, True, "Attendu : True")

    def testEstVerrouille(self) -> None:
        self.assertEqual(self.operation.estVerrouille, True, "Attendu : True")
    
    def testEstCredit(self) -> None:
        self.assertEqual(self.operation.estCredit(), True, "Attendu : True")

    def testEstDebit(self) -> None:
        self.operation.montant = -5
        self.assertEqual(self.operation.estCredit(), False, "Attendu : False")

    def testEstCredit0(self) -> None:
        self.operation.montant = 0
        self.assertEqual(self.operation.estCredit(), True, "Attendu : True")