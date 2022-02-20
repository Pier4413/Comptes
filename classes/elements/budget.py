class Budget(object):
    """
        Cette classe represente un budget au sein de l'application (Modele)

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def __init__(self, id : int = -1, libelle : str = "", init : float = 0, courant : float = 0, depense : float = 0) -> None:
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
        """
        self.id = id
        self.libelle = libelle
        self.init = init
        self.courant = courant
        self.depense = depense

    def __str__(self) -> str:
        return "Id : ["+str(self.id)+"], Libelle : ["+str(self.libelle)+"], Init : ["+str(self.init)+"], Courant : ["+str(self.courant)+"], Depense : ["+str(self.depense)+"]"