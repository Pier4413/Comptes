import datetime
from dateutil.relativedelta import relativedelta
from pytz import timezone

class Operation(object):
    """
        Cette classe permet de modeliser une operation

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def __init__(self, id : int = -1, libelle : str = "", montant : float = 0, date : int = 0, est_valide : bool = False, est_verrouille : bool = False, compte : int = -1, budget : int = -1, recursivite : str = None) -> None:
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
            :param operation: Optional; Default : -1; Identifiant de l'operation associe dans la base de donnees
            :type operation: int
            :param budget: Optional; Default : -1; Identifiant de l'operation associe dans la base de donnees
            :type budget: int
        """
        self.id = id
        self.libelle = libelle
        self.montant = montant
        self.date = date
        self.est_valide = est_valide
        self.est_verrouille = est_verrouille
        self.compte = compte
        self.budget = budget
        self.recursivite = recursivite

    def __str__(self) -> str:
        """
            Cette fonction renvoi la classe sous forme de chaine de caracteres

            :rtype: str
        """
        return "Id : ["+str(self.id)+"], Libelle : ["+str(self.libelle)+"], Montant : ["+str(self.montant)+"], Date : ["+str(self.date)+"], estValide : ["+str(self.est_valide)+"], estVerrouille : ["+str(self.est_verrouille)+"], Compte : ["+str(self.compte)+"], Budget : ["+str(self.budget)+"], Recursivite : ["+str(self.recursivite)+"]"

    def est_credit(self) -> bool:
        """
            Cette fonction renvoi si c'est un debit ou un credit en fonction du signe de l'operation
            
            :return: Un booleen disant c'est un credit (True : Credit, False : Debit)
            :rtype: bool
        """
        return self.montant >= 0

    def traite_recursivite(self):
        """
            Cette fonction permet de traiter la recursivite d'une operation. Elle cree une nouvelle operation avec la nouvelle date

            :return: La nouvelle operation
            :rtype: Operation
        """
        if(self.recursivite is not None):
            try:
                return Operation(
                    libelle=self.libelle,
                    montant=self.montant,
                    date=Operation.parse_nouvelle_date_recursivite(self.date, self.recursivite),
                    budget=self.budget,
                    compte=self.compte,
                    recursivite=self.recursivite
                )
            except Exception:
                return None
        return None

    def parse_nouvelle_date_recursivite(date : int, recursivite : str) -> int:
        """
            Cette fonction renvoi la nouvelle date en fonction du parsing de la recursivite

            :param date: La date sous forme d'un timestamp
            :type date: La date
            :param recursivite: La recursivite sous forme d'une chaine de caractere
            :type recursivite: str
            :raise: Une exception si la recursivite demande n'existe pas
        """
        date_formatted = datetime.datetime.fromtimestamp(date, tz=timezone("UTC"))

        if(recursivite == "w"):
            return int((date_formatted + relativedelta(weeks=1)).timestamp())
        elif(recursivite == "ow"):
            return int((date_formatted + relativedelta(weeks=2)).timestamp())
        elif(recursivite == "m"):
            return int((date_formatted + relativedelta(months=1)).timestamp())
        elif(recursivite == "om"):
            return int((date_formatted + relativedelta(months=2)).timestamp())
        elif(recursivite == "t"):
            return int((date_formatted + relativedelta(months=3)).timestamp())
        elif(recursivite == "s"):
            return int((date_formatted + relativedelta(months=6)).timestamp())
        elif(recursivite == "y"):
            return int((date_formatted + relativedelta(years=1)).timestamp())
        else:
            raise Exception("La recursivite demande n'existe pas")
