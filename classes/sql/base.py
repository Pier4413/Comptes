import sqlite3

class Base(object):
    """
        Cette classe a pour but de faire les operations de base SQL

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """
    
    """
        Static instance for Singleton
        :meta static:
        :type __instance: Logger
    """
    __instance = None

    def getInstance():
        """ 
            Static access method
            :meta static:
        """
        if Base.__instance == None:
            Base()
        return Base.__instance
   
    def __init__(self):
        """
            Virtually private constructor
        """
        if Base.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            try:
                self.conn = sqlite3.connect("comptes.db")
                self.cur = self.conn.cursor()
                Base.__instance = self
            except:
                Base.__instance = None

    #def __del__(self) -> None:
    #    self.conn.close()

    def execute(self, query : str) -> sqlite3.Cursor:
        """
            Cette methode cree les tables

            :param query: La requete a executee
            :type query: str
            :return: Le resultat de la requete
            :rtype: sqlite3.Cursor
        """
        return self.cur.execute(query)

    def commit(self) -> None:
        self.conn.commit()