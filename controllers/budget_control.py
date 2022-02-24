from typing import List

from PyQt6.QtCore import QThread

from modules.logger.logger import Logger
from modules.settings.settings import Settings

from classes.elements.budget import Budget as BudgetModele
from classes.sql.budget import Budget as BudgetSQL

from views.fenetre_principale import FenetrePrincipale
from views.budget.list_item import BudgetListWidgetItem
from views.list_view import ListWidget

from workers.budget_worker import BudgetWorker

class BudgetControl(object):

    def __init__(self, app : FenetrePrincipale) -> None:
        """
            Constructeur

            :param app: L'application
            :type app: FenetrePrincipale
        """
        self.app = app

        self.budgetSql = BudgetSQL(Settings.get_instance().get('Database', 'filename', 'comptes.db'))
        self.worker = BudgetWorker(db_name=Settings.get_instance().get('Database', 'filename', 'comptes.db'))
        self.thread = QThread()
        self.budgets = list()

        self.init_controls()
        
        self.read_budgets()

    def init_controls(self) -> None:
        """
            Cette fonction initialise les controles
        """
        self.app.tabs.budgets.add_button.clicked.connect(self.add_a_budget)

    def add_a_budget(self) -> None:
        budget = BudgetModele(libelle="Nouveau budget", init=0, courant=0, depense=0)
        self.app.tabs.budgets.budgets.add_item(
            BudgetListWidgetItem(
                budget=budget
            )
        )
        self.budgetSql.save(budget)

    def read_budgets(self) -> None:
        """
            Va lire les budgets dans la base de donnees
        """
        self.thread.started.connect(self.worker.run) # Sur demarrage du thread on execute la fonction suivante
        self.worker.progress.connect(self.budget_worker_in_progress) # Sur reception d'un message en cours
        self.worker.finished.connect(self.thread.quit) # Sur fin de la fonction du thread on quit le thread
        self.worker.finished.connect(self.thread.deleteLater) # Ensuite on le supprime
        self.worker.finished.connect(self.worker.deleteLater) # Puis on supprime le worker ???
        self.worker.finished.connect(self.budget_worker_finished) # Puis on execute la fonction de fin

        self.thread.start()

    def budget_worker_in_progress(self, budget : BudgetModele) -> None:
        """
            Fonction de gestion pour le worker sur progression de la lecture de donnees

            :param budget: Le budget recu
            :type budget: BudgetModele
        """
        Logger.get_instance().info("Nouveau budget recu")

    def budget_worker_finished(self) -> None:
        """
            Fonction de gestion sur fin du worker de la lecture de donnees
        """
        Logger.get_instance().info("Chargement des budgets finis")

    def load_budgets_in_window(self) -> None:
        """
            Fonction qui charge une liste de budgets dans la page fenetre principale
        """
        for b in self.budgets:
            self.app.tabs.budgets.budgets.addItem(BudgetListWidgetItem(
                b
            ))

