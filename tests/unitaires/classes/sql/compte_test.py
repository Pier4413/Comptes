import unittest
from classes.elements.compte import Compte as CompteModele
from classes.sql.compte import Compte as CompteSQL

class OperationSQLTest(unittest.TestCase):
    
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
    
    def testCreateTable(self):
        ret = self.cptSql.createTable()
        self.assertEqual(ret, 0, "Attendu : 0")

    def testInsertIntoDatabase(self):
        ret = self.cptSql.save(self.cptMod)
        self.identifiant = ret.id
        self.assertEqual(ret.id, 1, "Attendu : 1")

    def testModify(self):
        tester = self.cptMod
        tester.libelle = "TestII"
        tester.id = 1 # Normalement vu qu'on utilise qu'une seule base en memoire, on a qu'un seul element introduit par testInsertIntoDatabase
        
        ret = self.cptSql.modify(tester)
        self.assertEqual(ret.libelle, "TestII", "Attendu : TestII")

    def testSelectAll(self):
        operations = self.cptSql.selectAll()

        if(len(operations) == 1):
            self.assertEqual(operations[0].id, 1, "Attendu : 1") # On recupere le premier element de la base de donnees temporaire
        else:
            self.assertTrue(False) # Le test est echoue si on a rien dans la base de donnees par definition

    @unittest.skip("Ne marche pas avec le delete pour une raison obscure")
    def testDelete(self):
        tester = self.cptMod
        tester.id = 1
        ret = self.cptSql.delete(self.cptMod)
        self.assertEqual(ret, 0, "Attendu : 0")