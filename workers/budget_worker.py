from typing import List

from PyQt6.QtCore import QObject, pyqtSignal

from classes.elements.budget import Budget as BudgetModele
from classes.sql.budget import Budget as BudgetSQL

class BudgetWorker(QObject):
    """
        Worker du budget

        :author: Panda <panda@delmasweb.net>
        :date: January 15, 2022
        :version: 1.0
    """

    """
        pyqtSignal a envoye quand le worker a fini sa tache
    """
    finished = pyqtSignal()
    
    """
        pyqtSignal a envoye quand le worker est en cours d'execution
    """
    progress = pyqtSignal(BudgetModele)

    def __init__(self, parent : QObject = None, db_name : str = None) -> None:
        """
            Constructeur du worker

            :param parent: Optional; Default : None; Le parent du worker
            :type parent: QObject
            :param db_name: Optional; Default : None; Le nom de la base de donnees
            :type db_name: str 
        """
        super().__init__(parent)
        self.db_name = db_name

    def run(self):
        """
            Boucle principale du worker
        """
        budgetSQL = BudgetSQL(self.db_name)
        budgets = budgetSQL.select_all()

        for b in budgets:
            self.progress.emit(b)
        self.finished.emit()
