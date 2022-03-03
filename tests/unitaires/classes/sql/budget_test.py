import pytest
from classes.elements.budget import Budget as BudgetModele
from classes.sql.budget import Budget as BudgetSQL

class TestBudgetSQL():

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
    
    def setup_method(self) -> None:
        self.bgSql = BudgetSQL(":memory:")
        self.bgMod = BudgetModele(
            id=self.identifiant,
            libelle=self.libelle,
            courant=self.courant,
            depense=self.depense,
            mois=1,
            annee=0,
            init=self.init
        )
    
    def test_create_table(self):
        ret = self.bgSql.create_table()
        assert ret == 0, "Attendu : 0"

    def test_insert_into_database(self):
        ret = self.bgSql.save(self.bgMod)
        self.identifiant = ret.id
        assert ret.id == 1, "Attendu : 1"

    def test_modify(self):
        tester = self.bgMod
        tester.libelle = "TestII"
        tester.id = 1 # Normalement vu qu'on utilise qu'une seule base en memoire, on a qu'un seul element introduit par testInsertIntoDatabase
        
        ret = self.bgSql.modify(tester)
        assert ret.libelle == "TestII", "Attendu : TestII"

    def test_select_all(self):
        budgets = self.bgSql.select_all()

        if(len(budgets) == 1):
            assert budgets[0].id == 1, "Attendu : 1" # On recupere le premier element de la base de donnees temporaire
        else:
            assert True == False # Le test est echoue si on a rien dans la base de donnees par definition

    def test_select_par_mois_et_annee(self):
        budgets = self.bgSql.select_par_mois_annee(1,0)

        if(len(budgets) == 1):
            assert budgets[0].id == 1, "Attendu : 1"
        else:
            assert True == False

    def test_verifie_si_mois_annee_existe_ou_cree(self):
        self.bgSql.verifie_si_mois_annee_existe_ou_cree(12,1)

        budgets = self.bgSql.select_all()

        if(len(budgets) == 2):
            assert True == True, "Attendu : 2 budgets, soit 2 mois"
        else:
            assert True == False

    def test_delete(self):
        tester = self.bgMod
        tester.id = 1
        ret = self.bgSql.delete(self.bgMod)
        assert ret == 0, "Attendu : 0"