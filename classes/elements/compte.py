from typing import List

from classes.elements.operation import Operation


class Compte(object):
    """
    Cette classe represente un compte au sein de l'application (Modele)

    :author: Mathsgiver <mathsgiver@gmail.com>
    :date: 20 Fevrier 2022
    :version: 1.0 
    """

    def __init__(self, id : int = -1, libelle : str = "", solde : float = 0,operations : List[Operation] = list()) -> None:
        """
        Construction

        :param id: Optional ; Default : -1; L'identifiant en base de donnees. -1 signifie aucune entree en base de donnees connue
        :type id: int
        :param libelle: Optional ; Default : ""; Le libelle du compte 
        :type libelle: str 
        :param solde: Optional ; Default : ""; Le solde du compte
        :type solde: float
        :param operations: Optional ; Default : list(); La liste des operations du compte
        :type operations: list
        """
        self.id = id
        self.libelle = libelle
        self.solde = solde
        self.operations = operations
    
    def __str__(self) -> str:
        """
        Conversion en texte

        :return: Retourne le contenu des attributs sous format texte
        :rtype: str
        """
        return f"Id : [{self.id}], Libelle : [{self.libelle}], Solde : [{self.solde}], Operations : [{self.operations}]"

    def recalcule_solde(self) -> str:
        """
            Cette fonction recalcule le solde disponible
        """
        for o in self.operations:
            self.solde = self.solde + o.montant
        self.solde = round(self.solde, 2)