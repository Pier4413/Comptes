from typing import List
from xmlrpc.client import boolean

from classes.elements.operation import Operation


class Compte(object):
    """
    Cette classe represente un compte au sein de l'application (Modele)

    :author: Mathsgiver <mathsgiver@gmail.com>
    :date: 20 Fevrier 2022
    :version: 1.0 
    """

    def __init__(self, id : int = -1, libelle : str = "", solde : float = 0, est_archive : boolean = False) -> None:
        """
        Construction

        :param id: Optional ; Default : -1; L'identifiant en base de donnees. -1 signifie aucune entree en base de donnees connue
        :type id: int
        :param libelle: Optional ; Default : ""; Le libelle du compte 
        :type libelle: str 
        :param solde: Optional ; Default : ""; Le solde du compte
        :type solde: float
        :param est_archive: Optional ; Default : False; Si l'operation a ete archive ou non
        :type est_archive: boolean
        """
        self.id = id
        self.libelle = libelle
        self.solde = solde
        self.est_archive = est_archive
    
    def __str__(self) -> str:
        """
        Conversion en texte

        :return: Retourne le contenu des attributs sous format texte
        :rtype: str
        """
        return f"Id : [{self.id}], Libelle : [{self.libelle}], Solde : [{self.solde}], Archive : [{self.est_archive}]"