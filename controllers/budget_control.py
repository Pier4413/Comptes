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
        budget = self.budgetSql.save(budget)

        budget_item = BudgetListWidgetItem(budget=budget)
        budget_item.update_budget.connect(self.update_budget)
        budget_item.delete_budget.connect(self.delete_budget)
        self.app.tabs.budgets.budgets.add_item(budget_item)

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
        Logger.get_instance().debug("Nouveau budget recu")
        budget_item = BudgetListWidgetItem(budget=budget)
        budget_item.update_budget.connect(self.update_budget)
        budget_item.delete_budget.connect(self.delete_budget)
        self.app.tabs.budgets.budgets.add_item(budget_item)

    def budget_worker_finished(self) -> None:
        """
            Fonction de gestion sur fin du worker de la lecture de donnees
        """
        Logger.get_instance().info(f"Chargement des budgets finis")

    def update_budget(self, budget : BudgetModele) -> None:
        """
            Cette fonction est appelle lorsqu'un budget est modifie et fait une sauvegarde dans la base de donnees

            :param budget: Le nouveau budget a sauvegarde
            :type budget: BudgetModele
        """
        try:
            self.budgetSql.modify(budget)
        except Exception as e:
            Logger.get_instance().error(f"Impossible de mettre a jour le budget avec l'id : {budget.id}. Erreur complete : {e}")

    def delete_budget(self, budget : BudgetModele) -> None:
        """
            Cette fonction est appelle lorsqu'un budget est modifie et fait la sauvegarde en base de donnees en plus de supprimer de la liste

            :param budget: Le budget a supprimer
            :type budget: BudgetModele
        """
        try:
            self.budgetSql.delete(budget)
        except Exception as e:
            Logger.get_instance().error(f"Impossible de supprimer le budget avec l'id : {budget.id}. Erreur complete : {e}")

