import unittest
from classes.elements.budget import Budget as BudgetModele
from classes.sql.budget import Budget as BudgetSQL

class BudgetSQLTest(unittest.TestCase):

    """
        Id global. Peut-etre modifie par les tests
    """
    identifiant = -1

    """
        Libelle global. Peut-etre modifie par les tests
    """
    libelle="Ma nouvelle operation"
    
    """
        Courant global. Peut-etre modifie par les tests
    """
    courant=30
    
    """
        Depense globale. Peut-etre modifie par les tests
    """
    depense=50
    
    """
        Montant init global. Peut-etre modifie par les tests
    """
    init=2
    
    def setUp(self) -> None:
        super().setUp()
        self.bgSql = BudgetSQL(":memory:")
        self.bgMod = BudgetModele(
            id=self.identifiant,
            libelle=self.libelle,
            courant=self.courant,
            depense=self.depense,
            init=self.init
        )
    
    def testCreateTable(self):
        ret = self.bgSql.createTable()
        self.assertEqual(ret, 0, "Attendu : 0")

    def testInsertIntoDatabase(self):
        ret = self.bgSql.save(self.bgMod)
        self.identifiant = ret.id
        self.assertEqual(ret.id, 1, "Attendu : 1")

    @unittest.skip("#BUG Ne marche pas à corriger")
    def testModify(self):
        tester = self.bgMod
        tester.libelle = "TestII"
        tester.id = 1 # Normalement vu qu'on utilise qu'une seule base en memoire, on a qu'un seul element introduit par testInsertIntoDatabase
        
        ret = self.bgSql.modify(tester)
        self.assertEqual(ret.libelle, "TestII", "Attendu : TestII")

    def testSelectAll(self):
        operations = self.bgSql.selectAll()

        if(len(operations) == 1):
            self.assertEqual(operations[0].id, 1, "Attendu : 1") # On recupere le premier element de la base de donnees temporaire
        else:
            self.assertTrue(False) # Le test est echoue si on a rien dans la base de donnees par definition

    @unittest.skip("#BUG Ne marche pas avec le delete pour une raison obscure")
    def testDelete(self):
        tester = self.bgMod
        tester.id = 1
        ret = self.bgSql.delete(self.bgMod)
        self.assertEqual(ret, 0, "Attendu : 0")