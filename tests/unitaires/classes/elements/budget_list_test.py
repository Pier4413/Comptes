from classes.elements.budget import Budget
from classes.elements.buget_list import BudgetList

class TestBudgetList():

    def setup_method(self):
        self.budgets = BudgetList()
        self.budgets.append(Budget(
            id=50,
            libelle="Mon libelle de test",
            init=10,
            courant=11,
            depense=5
        ))

    def test_find_an_element_from_id(self):
        ret = self.budgets.find_budget_from_id(50)
        assert ret["budget"].id == 50 and ret["index"] == 0
