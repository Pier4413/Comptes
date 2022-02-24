from typing import List
from classes.elements.operation import Operation

class Budget(object):
    """
        Cette classe represente un budget au sein de l'application (Modele)

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def __init__(self, id : int = -1, libelle : str = "", init : float = 0, courant : float = 0, depense : float = 0, operations : List[Operation] = list()) -> None:
        """
            Constructeur

            :param id: Optional; Default : -1; L'identifiant en base de donnees. -1 signifie aucune entree en base de donnees connue
            :type id: int
            :param libelle: Optional; Default : ""; Le libelle du budget
            :type libelle: str
            :param init: Optional; Default : 0; Le montant initial du budget
            :type init: float
            :param courant: Optional; Default : 0; Le montant qu'il reste sur le budget
            :type courant: float
            :param depense: Optional; Default : 0; Le montant qui a ete depense
            :type depense: float
            :param operations: Optional; Default : list(); La liste des operations associes a ce budget
            :type operations: list
        """
        self.id = id
        self.libelle = libelle
        self.init = init
        self.courant = courant
        self.depense = depense
        self.operations = operations

    def __str__(self) -> str:
        return "Id : ["+str(self.id)+"], Libelle : ["+str(self.libelle)+"], Init : ["+str(self.init)+"], Courant : ["+str(self.courant)+"], Depense : ["+str(self.depense)+"], Operations : ["+str(self.operations)+"]"

    def recalcule_depense(self) -> None:
        """
            Cette fonction recalcule le montant depense sur un budget
        """
        for o in self.operations:
            self.depense = self.depense - o.montant

    def recalcule_courant(self) -> None:
        """
            Cette fonction recalcule le montant courant disponible
        """
        self.courant = self.init - self.depense
