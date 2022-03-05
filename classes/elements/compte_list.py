from typing import List
from classes.elements.compte import Compte

class CompteList(list):
    """
        Cette classe permet d'implementer une liste de compte

        :author: Mathsgiver <mathsgiver@gmail.com>
        :date: 03 Mars 2022
        :version: 1.0
    """
    
    def find_compte_from_id(self, id : int) -> dict:
        """
            Retourne un dictionnaire contenant le compte trouve et son index dans la liste
            
            :param id: L'identifiant du compte que l'on cherche
            :type id: int
        """
        index = 0
        for b in self:
            if(b.id == id):
                return {"compte": b, "index": index}
            index = index + 1