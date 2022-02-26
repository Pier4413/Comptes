from classes.sql.base import Base
from classes.elements.compte import Compte as Modele

class Compte(object):
    """
        Cette classe gere un compte au sein de SQL

        :author: Mathsgiver <mathsgiver@gmail.com>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def __init__(self, database_name : str) -> None:
        """
            Constructeur

            :param database_name: Le nom de la base de donnees
            :type database_name: str
        """
        self.__conn = Base.get_instance(database_name)

    def create_table(self) -> int:
        """
            Cette methode cree la table des comptes dans la base de donnees

            :return: Un code de retour 0 : OK
            :rtype: int
            :raise: Une exception si la table ne peut etre creee
        """
        if(self.__conn is not None):
            self.__conn.cur.execute('''CREATE TABLE comptes
                (id INTEGER NOT NULL, 
                libelle TEXT, 
                solde REAL,
                CONSTRAINT pk_comptes PRIMARY KEY (id));''')

            self.__conn.conn.commit()
            return 0
        else:
            return -1
    
    def save(self, compte : Modele) -> Modele:
        """
            Cette methode enregistre un nouvel element dans la base de donnees a partir d'un element fourni en parametre

            :param compte: Le compte a enregistrer dans la base de donnees
            :type compte: Modele
            :return: Le compte fourni avec l'id mis a jour
            :rtype: Modele or None
            :raise: Une exception si l'insertion ne peut pas se faire
        """
        if(self.__conn is not None):
            result = self.__conn.cur.execute('''INSERT INTO comptes(
                libelle,
                solde) VALUES(?, ?)''', [compte.libelle, compte.solde])

            if(result.rowcount > 0):
                self.__conn.conn.commit()
                compte.id = result.lastrowid
                return compte
            else:
                raise Exception(f"Compte insertion echouee, id : {compte.id}")
        else:
            return None
    
    def modify(self, compte : Modele) -> Modele:
        """
            Cette methode modifie un element dans la base de donnees a partir d'un element fourni en parametre

            :param budget: Le compte a modifier dans la base de donnees
            :type budget: Modele
            :return: Le compte mis a jour
            :rtype: Modele or None
            :raise: Une exception si la mise a jour n'a pas pu se faire
        """
        if(self.__conn is not None):

            if(compte.id > 0):
                result = self.__conn.cur.execute('''UPDATE comptes SET libelle=?,solde=?''', [compte.libelle, compte.solde])

                if(result.rowcount > 0):
                    self.__conn.conn.commit()
                    return compte
                else:
                    raise Exception(f"Compte non mis a jour, id : {compte.id}")
            else:
                raise Exception(f"Could not update a non existent data")
        else:
            return None

    def select_all(self) -> list:
        """
            Cette methode recupere la liste de tous les comptes dans la base de donnees et la renvoi sous la forme d'une liste de modeles
        
            :return: Retourne les comptes retrouves dans la base
            :rtype: list
        """
        if(self.__conn is not None):
            comptes = list()
            for row in self.__conn.cur.execute('''SELECT * FROM comptes'''):
                comptes.append(Modele(
                    id=row[0],
                    libelle=row[1],
                    solde=row[2]
                ))
            return comptes
        else:
            return list()

    def delete(self, compte : Modele) -> int:
        """
            Cette fonction supprime un compte de la base de donnees. Attention la suppression est definitive

            :param budget: Le compte a supprimer
            :type budget: Modele
            :return: Un code de retour 0 : OK
            :rtype: int
            :raise: Une exception si la suppression echoue
        """
        if(self.__conn is not None):
            result = self.__conn.cur.execute('''DELETE FROM comptes WHERE id=?''', [compte.id])

            if(result.rowcount > 0):
                self.__conn.conn.commit()
                return 0
            else:
                raise Exception(f"Budget Echec suppression, id : {compte.id}")
        else:
            return -1

