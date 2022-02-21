import unittest
from xml.dom.minidom import Element
from classes.elements.compte import Compte

class Compte_test(unittest.TestCase):
    """
        Cette classe est un test unitaire pour la classe Compte modele

        :author: Mathsgiver <mathsgiver@gmail.com>
        :date: 21 Fevrier 2022
        :version: 1.0
    """

    def setUp(self) -> None:
        super().setUp()
        self.compte = Compte(
                libelle="Mon miserable compte",
                id=1,
                solde=-6.66
            )

    def testLibelle(self):
        self.assertEqual(self.compte.libelle, "Mon miserable compte", "Attendu : Mon miserable compte")

    def testId(self):
        self.assertEqual(self.compte.id, 1, "Attendu : 1")

    def testSolde(self):
        self.assertEqual(self.compte.solde, -6.66, "Attendu : -6.66")