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

    def getInstance(databaseName = None):
        """ 
            Static access method

            :param databaseName: Optional; Default : None; Le nom de la base de donnees, a noter qu'il n'est utile de le passer que la premiere fois que l'on instancie le singleton
            :type databaseName: str
            :meta static:
        """
        if Base.__instance == None:
            Base(databaseName)
        return Base.__instance
   
    def __init__(self, databaseName : str):
        """
            Constructeur prive

            :param databaseName: Le nom de la base de donnees
            :type databaseName: str
        """
        if Base.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            try:
                if(databaseName != None):
                    self.conn = sqlite3.connect(databaseName)
                    self.cur = self.conn.cursor()
                    Base.__instance = self
                else:
                    raise Exception("You should provide a database name for the first instancation of the class")
            except:
                Base.__instance = None

    def __del__(self) -> None:
        self.conn.close()

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