from modules.logger.logger import Logger
from modules.settings.settings import Settings

from classes.elements.budget import Budget as BudgetModele
from classes.elements.buget_list import BudgetList as BudgetListModele
from classes.sql.budget import Budget as BudgetSQL


from views.fenetre_principale import FenetrePrincipale
from views.budget.list_item import BudgetListWidgetItem

class BudgetControl(object):

    def __init__(self, app : FenetrePrincipale) -> None:
        """
            Constructeur

            :param app: L'application
            :type app: FenetrePrincipale
        """
        # La liste principale qui s'affiche
        self.budgets_widget = app.tabs.budgets.budgets
        self.add_button = app.tabs.budgets.add_button

        # L'acces SQL
        self.budgetSql = BudgetSQL(Settings.get_instance().get('Database', 'filename', 'comptes.db'))

        # La liste des budgets       
        self.budgets = BudgetListModele()

        # Fonction d'initialisation des boutons et autres fonctionnalites
        self.init_controls()
        
        # Chargement de la base de donnees
        self.read_budgets()

    def init_controls(self) -> None:
        """
            Cette fonction initialise les controles
        """
        self.add_button.clicked.connect(self.add_a_budget)

    def add_a_budget(self) -> None:
        """
            Ajoute un budget
        """
        # On cree le nouveau budget
        budget = BudgetModele(libelle="Nouveau budget", init=0, courant=0, depense=0)
        
        # On le sauvegarde en base de donnees
        try:
            budget = self.budgetSql.save(budget)

            # On l'ajoute a la liste de traitement
            self.budgets.append(budget)

            # On cree un widget pour l'affichage
            budget_item = BudgetListWidgetItem(
                id=budget.id,
                libelle=budget.libelle,
                montant_init=budget.init,
                montant_courant=budget.courant,
                montant_depense=budget.depense
            )
            
            # On ajoute les fonctions sur modification du budget
            budget_item.update_libelle.connect(self.update_budget_libelle) # Modification du libelle
            budget_item.update_init.connect(self.update_budget_init) # Modification du montant initial
            budget_item.delete_budget.connect(self.delete_budget) # Suppression du budget

            # On ajoute l'item a la liste d'affichage
            self.budgets_widget.add_item(budget_item)
        except Exception as e:
            Logger.get_instance().error(f"Probleme de sauvegarde de la base de donnees {e}")

    def read_budgets(self) -> None:
        """
            Va lire les budgets dans la base de donnees
        """
        budgets = self.budgetSql.select_all()
        for b in budgets:
            # On ajoute le budget a la liste des budgets
            self.budgets.append(b)

            # On cree le widget associe
            budget_item = BudgetListWidgetItem(
                id=b.id,
                libelle=b.libelle,
                montant_init=b.init,
                montant_courant=b.courant,
                montant_depense=b.depense
            )

            # Link des fonctions de traitement
            budget_item.update_libelle.connect(self.update_budget_libelle) # Modification du libelle
            budget_item.update_init.connect(self.update_budget_init) # Modification du montant initial
            budget_item.delete_budget.connect(self.delete_budget) # Suppression du budget

            # On ajoute l'element a liste d'affichage
            self.budgets_widget.add_item(budget_item)

    def update_budget_libelle(self, new_libelle : str, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'un budget est modifie et fait une sauvegarde dans la base de donnees

            :param budget: Le nouveau budget a sauvegarde
            :type budget: BudgetModele
        """
        try:
            ret = self.budgets.find_budget_from_id(id)
            if(ret is not None):
                ret["budget"].libelle = new_libelle
                self.budgetSql.modify(ret["budget"])
            else:
                Logger.get_instance().error(f"Budget avec id : {id} non trouve dans la liste pour modification libelle")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de mettre a jour le budget avec l'id : {id}. Erreur complete : {e}")

    def update_budget_init(self, new_init : float, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'un budget est modifie et fait une sauvegarde dans la base de donnees

            :param budget: Le nouveau budget a sauvegarde
            :type budget: BudgetModele
        """
        try:
            ret = self.budgets.find_budget_from_id(id)
            if(ret is not None):
                ret["budget"].init = new_init
                ret["budget"].recalcule_depense()
                ret["budget"].recalcule_courant()
                self.budgetSql.modify(ret["budget"])
            else:
                Logger.get_instance().error(f"Budget avec id : {id} non trouve dans la liste pour modification montant init")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de mettre a jour le budget avec l'id : {id}. Erreur complete : {e}")

    def delete_budget(self, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'un budget est modifie et fait la sauvegarde en base de donnees en plus de supprimer de la liste

            :param budget: L'identifiant du budget a supprimer
            :type budget: BudgetModele
            :param row_pos: La position de la ligne a supprimer
            :type row_pos: int
        """
        try:
            ret = self.budgets.find_budget_from_id(id)
            if(ret is not None):
                self.budgetSql.delete(ret["budget"])
                self.budgets_widget.delete_item(ret["index"])
            else:
                Logger.get_instance().error(f"Budget avec id : {id} non trouve dans la liste pour suppression")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de supprimer le budget avec l'id : {id}. Erreur complete : {e}")

