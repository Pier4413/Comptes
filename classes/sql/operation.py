from classes.sql.base import Base
from classes.elements.operation import Operation as Modele

class Operation(object):
    """
        Cette classe represente les fonctions necessaires pour une operation SQL

        :author: Panda <panda@delmasweb.net>
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
            Cette methode cree la table des operations dans la base de donnees

            :return: Un code de retour 0 : OK
            :rtype: int
        """
        if(self.__conn is not None):
            self.__conn.cur.execute('''CREATE TABLE operations
                (id INTEGER NOT NULL, 
                libelle TEXT, 
                montant REAL, 
                budget INTEGER, 
                compte INTEGER,
                date INTEGER,
                estValide INTEGER,
                estVerrouille INTEGER,
                recursivite CHAR DEFAULT NULL,
                CONSTRAINT pk_operation PRIMARY KEY (id),
                CONSTRAINT fk_budgetOperation FOREIGN KEY (budget) REFERENCES budget(id),
                CONSTRAINT fk_compteOperation FOREIGN KEY (compte) REFERENCES compte(id));''')
            self.__conn.conn.commit()
            return 0
        else:
            return -1

    def update_table(self) -> int:
        """
            Cette methode met a jour la table dans la base de donnees

            Attention : Cette methode peut perdre des donnees
        """
        if(self.__conn is not None):
            
            operations = self.select_all()

            self.__conn.cur.execute('''
                DROP TABLE operations;
            ''')

            self.create_table()

            for o in operations:
                self.save(o)

    def save(self, operation : Modele) -> Modele:
        """
            Cette methode enregistre un nouvel element dans la base de donnees a partir d'un element fourni en parametre

            :param operation: L'operation a enregistrer dans la base de donnees
            :type operation: Modele
            :return: Le operation fourni avec l'id mis a jour
            :rtype: Modele or None
            :raise: Une exception si l'insertion ne peut pas se faire
        """
        if(self.__conn is not None):
            result = self.__conn.cur.execute('''INSERT INTO operations(
                libelle,
                montant,
                compte,
                budget,
                date,
                estValide,
                estVerrouille,
                recursivite
                ) VALUES(?, ?, ?, ?, ?, ?, ?, ?);''', [operation.libelle, operation.montant, operation.compte, operation.budget, operation.date, 1 if(operation.est_valide) else 0, 1 if(operation.est_verrouille) else 0, operation.recursivite])

            if(result.rowcount > 0):
                self.__conn.conn.commit()
                operation.id = result.lastrowid
                return operation
            else:
                raise Exception(f"Operation insertion echouee, id : {operation.id}")
        else:
            return None
    
    def modify(self, operation : Modele) -> Modele:
        """
            Cette methode modifie un element dans la base de donnees a partir d'un element fourni en parametre

            :param operation: L'operation a modifier dans la base de donnees
            :type operation: Modele
            :return: Le operation mis a jour
            :rtype: Modele or None
            :raise: Une exception si la mise a jour n'a pas pu se faire
        """
        if(self.__conn is not None):
            if(operation.id > 0):
                result = self.__conn.cur.execute('''UPDATE operations SET
                    libelle=?
                    , montant=?
                    , compte=?
                    , budget=?
                    , date=?
                    , estValide=?
                    , estVerrouille=?
                    , recursivite=?
                    WHERE id=?''', 
                    [operation.libelle, 
                    operation.montant, 
                    operation.compte, 
                    operation.budget, 
                    operation.date, 
                    1 if(operation.est_valide) else 0, 
                    1 if(operation.est_verrouille) else 0, 
                    operation.recursivite, 
                    operation.id])

                if(result.rowcount > 0):
                    self.__conn.conn.commit()
                    return operation
                else:
                    raise Exception(f"Operation non mis a jour, id : {operation.id}")
            else:
                raise Exception("Could not update a non existent data")
        else:
            return None

    def select_all(self) -> list():
        """
            Cette methode recupere la liste de tous les operations dans la base de donnees et la renvoi sous la forme d'une liste de modeles
        
            :return: Retourne les operations retrouves dans la base
            :rtype: list
        """
        if(self.__conn is not None):
            operations = list()
            for row in self.__conn.cur.execute('''SELECT * FROM operations'''):
                operations.append(Modele(
                    id=row[0],
                    libelle=row[1],
                    montant=row[2],
                    compte=row[3],
                    budget=row[4],
                    date=row[5],
                    est_valide=True if(row[6]==1) else False,
                    est_verrouille=True if(row[7]==1) else False,
                    recursivite=row[8]
                ))
            return operations
        else:
            return list()

    def delete(self, operation : Modele) -> int:
        """
            Cette fonction supprime une operation de la base de donnees. Attention la suppression est definitive

            :param operation: L'operation a supprimer
            :type operation: Modele
            :return: Un code de retour 0 : OK
            :rtype: int
            :raise: Une exception si la suppression echoue
        """
        if(self.__conn is not None):
            result = self.__conn.cur.execute('''DELETE FROM operations WHERE id=?''', [operation.id])

            if(result.rowcount > 0):
                self.__conn.conn.commit()
                return 0
            else:
                raise Exception(f"Operation Echec suppression, id : {operation.id}")
        else:
            return -1
    