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

    def test_id(self) -> None:
        self.assertEqual(self.operation.id, 1, "Attendu : 1")
    
    def test_libelle(self) -> None:
        self.assertEqual(self.operation.libelle, "Ma nouvelle operation", "Attendu : Ma nouvelle operation")

    def test_montant(self) -> None:
        self.assertEqual(self.operation.montant, 10, "Attendu : 10")

    def test_date(self) -> None:
        self.assertEqual(self.operation.date, 50, "Attendu : 50")

    def test_est_valide(self) -> None:
        self.assertEqual(self.operation.est_valide, True, "Attendu : True")

    def test_est_verrouille(self) -> None:
        self.assertEqual(self.operation.est_verrouille, True, "Attendu : True")
    
    def test_est_credit(self) -> None:
        self.assertEqual(self.operation.est_credit(), True, "Attendu : True")

    def test_est_debit(self) -> None:
        self.operation.montant = -5
        self.assertEqual(self.operation.est_credit(), False, "Attendu : False")

    def test_est_credit_0(self) -> None:
        self.operation.montant = 0
        self.assertEqual(self.operation.est_credit(), True, "Attendu : True")