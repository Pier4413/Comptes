import pytest
from classes.elements.operation import Operation as OperationModele
from classes.sql.operation import Operation as OperationSQL

class TestOperationSQL():
    
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
    
    

    def setup_method(self) -> None:
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
        assert ret == 0, "Attendu : 0"

    def test_insert_into_database(self):
        ret = self.opSql.save(self.opMod)
        self.identifiant = ret.id
        assert ret.id == 1, "Attendu : 1"

    def test_modify(self):
        tester = self.opMod
        tester.libelle = "TestII"
        tester.id = 1 # Normalement vu qu'on utilise qu'une seule base en memoire, on a qu'un seul element introduit par testInsertIntoDatabase
        
        ret = self.opSql.modify(tester)
        assert ret.libelle == "TestII", "Attendu : TestII"

    def test_select_all(self):
        operations = self.opSql.select_all()

        if(len(operations) == 1):
            assert operations[0].id == 1, "Attendu : 1" # On recupere le premier element de la base de donnees temporaire
        else:
            assert True == False # Le test est echoue si on a rien dans la base de donnees par definition

    def test_delete(self):
        tester = self.opMod
        tester.id = 1
        ret = self.opSql.delete(self.opMod)
        assert ret == 0, "Attendu : 0"