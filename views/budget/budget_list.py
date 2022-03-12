from views.budget.list_item import BudgetListWidgetItem

class BudgetListWidget(list):
    """
        Cette classe permet de stocker et recuperer des BudgetListWidgetItem

        :author: Panda <panda@delmasweb.net>
        :date: 12 Mars 2022
        :version: 1.0
    """

    def find_by_id(self, id : int) -> BudgetListWidgetItem:
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