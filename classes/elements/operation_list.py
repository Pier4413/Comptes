from typing import List
from classes.elements.operation import Operation

class OperationList(list):
    """
        Cette classe permet d'implementer une liste d'operation

        :author: Mathsgiver <mathsgiver@gmail.com>
        :date: 16 Mars 2022
        :version: 1.0
    """
    
    def find_operation_from_id(self, id : int) -> dict:
        """
            Retourne un dictionnaire contenant l'operation trouve et son index dans la liste
            
            :param id: L'identifiant du compte que l'on cherche
            :type id: int
        """
        index = 0
        for b in self:
            if(b.id == id):
                return {"operation": b, "index": index}
            index = index + 1