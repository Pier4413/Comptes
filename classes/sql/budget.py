from classes.sql.base import Base
from classes.elements.budget import Budget as Modele

class Budget(object):
    """
        Cette classe gere un budget au sein de SQL

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def __init__(self, database_name : str = None) -> None:
        """
            Constructeur

            :param database_name: Le nom de la base de donnees
            :type database_name: str
        """
        self.__conn = Base.get_instance(database_name)

    def create_table(self) -> int:
        """
            Cette methode cree la table des budgets dans la base de donnees

            :return: Un code de retour 0 : OK
            :rtype: int
        """
        if(self.__conn != None):
            self.__conn.execute('''CREATE TABLE budgets
                (id INTEGER NOT NULL, 
                libelle TEXT, 
                initial REAL, 
                courant REAL, 
                depense REAL,
                CONSTRAINT pk_budget PRIMARY KEY (id));''')

            self.__conn.commit()
            return 0
        else:
            return -1

    def save(self, budget : Modele) -> Modele:
        """
            Cette methode enregistre un nouvel element dans la base de donnees a partir d'un element fourni en parametre

            :param budget: Le budget a enregistrer dans la base de donnees
            :type budget: Modele
            :return: Le budget fourni avec l'id mis a jour
            :rtype: Modele or None
            :raise: Une exception si l'insertion ne peut pas se faire
        """
        if(self.__conn != None):
            result = self.__conn.execute('''INSERT INTO budgets(
                libelle,
                initial,
                courant,
                depense) VALUES(\"'''+str(budget.libelle)+'''\",0,0,0)''')

            if(result.rowcount > 0):
                self.__conn.commit()
                budget.id = result.lastrowid
                return budget
            else:
                raise Exception("Budget insertion echouee, id : "+budget.id)
        else:
            return None
    
    def modify(self, budget : Modele) -> Modele:
        """
            Cette methode modifie un element dans la base de donnees a partir d'un element fourni en parametre

            :param budget: Le budget a modifier dans la base de donnees
            :type budget: Modele
            :return: Le budget mis a jour
            :rtype: Modele or None
            :raise: Une exception si la mise a jour n'a pas pu se faire
        """
        if(self.__conn != None):

            if(budget.id > 0):
                result = self.__conn.execute('''UPDATE budgets SET libelle='''+str(budget.libelle)+''',initial='''+str(budget.init)+''',courant='''+str(budget.courant)+''',depense='''+str(budget.depense)+''' WHERE id='''+str(budget.id))

                if(result.rowcount > 0):
                    self.__conn.commit()
                    return budget
                else:
                    raise Exception("Budget non mis a jour, id : "+budget.id)
            else:
                raise Exception("Could not update a non existent data")
        else:
            return None

    def select_all(self) -> list:
        """
            Cette methode recupere la liste de tous les budgets dans la base de donnees et la renvoi sous la forme d'une liste de modeles
        
            :return: Retourne les budgets retrouves dans la base
            :rtype: list
        """
        if(self.__conn != None):
            budgets = list()
            for row in self.__conn.execute('''SELECT * FROM budgets'''):
                budgets.append(Modele(
                    id=row[0],
                    libelle=row[1],
                    init=row[2],
                    courant=row[3],
                    depense=row[4]
                ))
            return budgets
        else:
            return list()

    def delete(self, budget : Modele) -> int:
        """
            Cette fonction supprime un budget de la base de donnees. Attention la suppression est definitive

            :param budget: Le budget a supprimer
            :type budget: Modele
            :return: Un code de retour 0 : OK
            :rtype: int
            :raise: Une exception si la suppression echoue
        """
        if(self.__conn != None):
            result = self.__conn.execute('''DELETE FROM budgets WHERE id='''+str(budget.id))

            if(result.rowcount > 0):
                self.__conn.commit()
                return 0
            else:
                raise Exception("Budget Echec suppression, id : "+budget.id)
        else:
            return -1
