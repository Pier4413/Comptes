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
        if(self.__conn is not None):
            self.__conn.cur.execute('''CREATE TABLE budgets
                (id INTEGER NOT NULL, 
                libelle TEXT, 
                initial REAL, 
                courant REAL, 
                depense REAL,
                mois INTEGER,
                annee INTEGER,
                CONSTRAINT pk_budget PRIMARY KEY (id));''')

            self.__conn.conn.commit()
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
        if(self.__conn is not None):
            result = self.__conn.cur.execute('''INSERT INTO budgets(
                libelle,
                initial,
                courant,
                depense) VALUES(?,0,0,0)''', budget.libelle)

            if(result.rowcount > 0):
                self.__conn.conn.commit()
                budget.id = result.lastrowid
                return budget
            else:
                raise Exception(f"Budget insertion echouee, id : {budget.id}")
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
        if(self.__conn is not None):

            if(budget.id > 0):
                result = self.__conn.cur.execute('''UPDATE budgets SET libelle=?
                , initial=?
                , courant=?
                , depense=?
                , mois=?
                , annee=?
                WHERE id=?'''
                , [budget.libelle
                , budget.init
                , budget.courant
                , budget.depense
                , budget.mois
                , budget.annee
                , budget.id])

                if(result.rowcount > 0):
                    self.__conn.conn.commit()
                    return budget
                else:
                    raise Exception(f"Budget non mis a jour, id : {budget.id}")
            else:
                raise Exception(f"Could not update a non existent data")
        else:
            return None

    def select_all(self) -> list:
        """
            Cette methode recupere la liste de tous les budgets dans la base de donnees et la renvoi sous la forme d'une liste de modeles
        
            :return: Retourne les budgets retrouves dans la base
            :rtype: list
        """
        if(self.__conn is not None):
            budgets = list()
            for row in self.__conn.cur.execute('''SELECT * FROM budgets'''):
                budgets.append(Modele(
                    id=row[0],
                    libelle=row[1],
                    init=row[2],
                    courant=row[3],
                    depense=row[4],
                    mois=row[5],
                    annee=row[6]
                ))
            return budgets
        else:
            return list()

    def select_par_mois_annee(self, mois : int, annee : int) -> list:
        """
            Cette methode recupere tous les budgets pour un mois et une annee et le renvoi sous forme de liste de modeles

            :param mois: Le mois vise
            :param annee: L'annee visee
            :return: La liste des budgets correspondants
            :rtype: list
        """
        if(self.__conn is not None):
            budgets = list()
            for row in self.__conn.cur.execute('''SELECT * from budgets WHERE mois=? AND annee=?''', mois, annee):
                budgets.append(Modele(
                    id=row[0],
                    libelle=row[1],
                    init=row[2],
                    courant=row[3],
                    depense=row[4],
                    mois=row[5],
                    annee=row[6]
                ))
            return budgets
        else:
            return list()

    def verifie_si_mois_annee_existe_ou_cree(self, mois : int, annee : int) -> None:
        """
            Cette methode recupere tous les budgets pour un mois et une annee et le renvoi sous forme de liste de modeles

            :param mois: Le mois vise
            :param annee: L'annee visee
            :return: La liste des budgets correspondants
            :rtype: list
        """
        if(len(self.select_par_mois_annee(mois, annee)) == 0):
            budgets = self.select_par_mois_annee(mois - 1, annee)
            for b in budgets:
                self.save(b)

    def delete(self, budget : Modele) -> int:
        """
            Cette fonction supprime un budget de la base de donnees. Attention la suppression est definitive

            :param budget: Le budget a supprimer
            :type budget: Modele
            :return: Un code de retour 0 : OK
            :rtype: int
            :raise: Une exception si la suppression echoue
        """
        if(self.__conn is not None):

            try:
                result = self.__conn.cur.execute('''DELETE FROM budgets WHERE id=?''', [budget.id])
                
                if(result.rowcount > 0):
                    self.__conn.conn.commit()
                    return 0
                else:
                    raise Exception(f"Budget Echec suppression, id : {budget.id}")
            except Exception as e:
                raise Exception(f"Budget can't delete budget {e}")
        else:
            return -1
