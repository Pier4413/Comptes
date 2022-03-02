from typing import List
from classes.elements.budget import Budget

class BudgetList(list):
    """
        Cette classe permet d'implementer une liste de budget

        :author: Panda <panda@delmasweb.net>
        :date: 26 Fevrier 2022
        :version: 1.0
    """
    
    def find_budget_from_id(self, id : int) -> dict:
        """
            Retourne un dictionnaire contenant le budget trouve et son index dans la liste
            
            :param id: L'identifiant du budget que l'on cherche
            :type id: int
        """
        index = 0
        for b in self:
            if(b.id == id):
                return {"budget": b, "index": index}
            index = index + 1