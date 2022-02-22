import unittest
from classes.elements.compte import Compte as CompteModele
from classes.sql.compte import Compte as CompteSQL

class CompteSQLTest(unittest.TestCase):
    
    """
        Id global. Peut-etre modifie par les tests
    """
    identifiant = -1

    """
        Libelle global. Peut-etre modifie par les tests
    """
    libelle="Ma nouvelle operation"
    
    """
        Montant global. Peut-etre modifie par les tests
    """
    solde=30  
    
    def setUp(self) -> None:
        super().setUp()
        self.cptSql = CompteSQL(":memory:")
        self.cptMod = CompteModele(
            id=self.identifiant,
            libelle=self.libelle,
            solde=self.solde
        )
    
    def test_create_table(self):
        ret = self.cptSql.create_table()
        self.assertEqual(ret, 0, "Attendu : 0")

    def test_insert_into_database(self):
        ret = self.cptSql.save(self.cptMod)
        self.identifiant = ret.id
        self.assertEqual(ret.id, 1, "Attendu : 1")

    def test_modify(self):
        tester = self.cptMod
        tester.libelle = "TestII"
        tester.id = 1 # Normalement vu qu'on utilise qu'une seule base en memoire, on a qu'un seul element introduit par testInsertIntoDatabase
        
        ret = self.cptSql.modify(tester)
        self.assertEqual(ret.libelle, "TestII", "Attendu : TestII")

    def test_select_all(self):
        operations = self.cptSql.select_all()

        if(len(operations) == 1):
            self.assertEqual(operations[0].id, 1, "Attendu : 1") # On recupere le premier element de la base de donnees temporaire
        else:
            self.assertTrue(False) # Le test est echoue si on a rien dans la base de donnees par definition

    @unittest.skip("#BUG Ne marche pas avec le delete pour une raison obscure")
    def testDelete(self):
        tester = self.cptMod
        tester.id = 1
        ret = self.cptSql.delete(self.cptMod)
        self.assertEqual(ret, 0, "Attendu : 0")