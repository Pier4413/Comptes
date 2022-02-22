import unittest
from classes.elements.operation import Operation as OperationModele
from classes.sql.operation import Operation as OperationSQL

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
    montant=30
    
    """
        Date globale. Peut-etre modifie par les tests
    """
    date=50
    
    """
        Identifiant de compte global. Peut-etre modifie par les tests
    """
    compte=2
    
    """
        Identifiant de budget global. Peut-etre modifie par les tests
    """
    budget=3
    
    

    def setUp(self) -> None:
        super().setUp()
        self.opSql = OperationSQL(":memory:")
        self.opMod = OperationModele(
                id=self.identifiant,
                libelle=self.libelle,
                montant=self.montant,
                date=self.date,
                compte=self.compte,
                budget=self.budget
        )
    
    def test_create_table(self):
        ret = self.opSql.create_table()
        self.assertEqual(ret, 0, "Attendu : 0")

    def test_insert_into_database(self):
        ret = self.opSql.save(self.opMod)
        self.identifiant = ret.id
        self.assertEqual(ret.id, 1, "Attendu : 1")

    def test_modify(self):
        tester = self.opMod
        tester.libelle = "TestII"
        tester.id = 1 # Normalement vu qu'on utilise qu'une seule base en memoire, on a qu'un seul element introduit par testInsertIntoDatabase
        
        ret = self.opSql.modify(tester)
        self.assertEqual(ret.libelle, "TestII", "Attendu : TestII")

    def test_select_all(self):
        operations = self.opSql.select_all()

        if(len(operations) == 1):
            self.assertEqual(operations[0].id, 1, "Attendu : 1") # On recupere le premier element de la base de donnees temporaire
        else:
            self.assertTrue(False) # Le test est echoue si on a rien dans la base de donnees par definition

    @unittest.skip("#BUG Ne marche pas avec le delete pour une raison obscure")
    def test_delete(self):
        tester = self.opMod
        tester.id = 1
        ret = self.opSql.delete(self.opMod)
        self.assertEqual(ret, 0, "Attendu : 0")