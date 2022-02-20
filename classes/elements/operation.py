class Operation(object):
    """
        Cette classe permet de modeliser une operation

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def __init__(self, id : int = -1, libelle : str = "", montant : float = 0, date : int = 0, estValide : bool = False, estVerrouille : bool = False) -> None:
        """
            Constructeur

            :param id: Optional; Default : -1; L'identifiant dans la base de donnees
            :type id: int
            :param libelle: Optional; Default : ""; Le libelle de l'operation
            :type libelle: str
            :param montant: Optional; Default : 0; Le montant de l'operation
            :type montant: float
            :param date: Optional; Default : 0; La date sous forme de timestamp UNIX
            :type date: int
            :param estValide: Optional; Default : False; Si l'operation a ete validee par l'utilisateur (i.e apparait sur le compte bancaire)
            :type estValide: bool
            :param estVerrouille: Optional; Default : False; Si l'operation a ete verrouille par l'utilisateur (i.e ne peut plus etre modifiee)
            :type estVerrouille:
        """
        self.id = id
        self.libelle = libelle
        self.montant = montant
        self.date = date
        self.estValide = estValide
        self.estVerrouille = estVerrouille

    def __str__(self) -> str:
        """
            Cette fonction renvoi la classe sous forme de chaine de caracteres

            :rtype: str
        """
        return "Id : ["+str(self.id)+"], Libelle : ["+str(self.libelle)+"], Montant : ["+str(self.montant)+"], Date : ["+str(self.date)+"], estValide : ["+str(self.estValide)+"], estVerrouille : ["+str(self.estVerrouille)+"]"

    def estCredit(self) -> bool:
        """
            Cette fonction renvoi si c'est un debit ou un credit en fonction du signe de l'operation
            
            :return: Un booleen disant c'est un credit (True : Credit, False : Debit)
            :rtype: bool
        """
        return self.montant >= 0
