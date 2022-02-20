from classes.sql.base import Base
from classes.elements.budget import Budget as Modele

class Budget(object):
    """
        Cette classe gere un budget au sein de SQL

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def __init__(self) -> None:
        self.conn = Base.getInstance()

    def createTable(self) -> int:
        """
            Cette methode cree la table des budgets dans la base de donnees
        """
        return self.conn.execute('''CREATE TABLE budgets
            (id INTEGER NOT NULL, 
            libelle TEXT, 
            initial REAL, 
            courant REAL, 
            depense REAL,
            CONSTRAINT pk_budget PRIMARY KEY (id));''')

    def save(self, budget : Modele):
        """
            Cette methode enregistre un nouvel element dans la base de donnees a partir d'un element fourni en parametre

            :param budget: Le budget a enregistrer dans la base de donnees
            :type budget: Modele
        """
        return self.conn.execute('''INSERT INTO budgets(
            libelle,
            initial,
            courant,
            depense) VALUES(?,0,0,0)''', (budget.libelle))
    
    def modify(self, budget : Modele):
        """
            Cette methode modifie un element dans la base de donnees a partir d'un element fourni en parametre

            :param budget: Le budget a modifier dans la base de donnees
            :type budget: Modele
        """
        return self.conn.execute('''UPDATE budgets
            SET libelle=?,init=?,courant=?,depense=? WHERE id=?
        ''', (budget.libelle, budget.init, budget.courant, budget.depense, budget.id))

    def selectAll(self) -> list:
        """
            Cette methode recupere la liste de tous les budgets dans la base de donnees et la renvoi sous la forme d'une liste de modeles
        """
        budgets = list()
        for row in self.conn.execute('''SELECT * FROM budgets'''):
            budgets.append(Modele(
                id=row[0],
                libelle=row[1],
                init=row[2],
                courant=row[3],
                depense=row[4]
            ))
        return budgets
