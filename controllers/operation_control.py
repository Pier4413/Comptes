from modules.logger.logger import Logger
from modules.settings.settings import Settings

from classes.elements.operation import Operation as OperationModele
from classes.elements.operation_list import OperationList as OperationListModele
from classes.sql.operation import Operation as OperationSQL
from classes.sql.budget import Budget as BudgetSQL 
from classes.sql.compte import Compte as CompteSQL


from views.fenetre_principale import FenetrePrincipale
from views.operation.list_item import OperationListWidgetItem

class OperationControl(object):

    def __init__(self, app : FenetrePrincipale) -> None:
        """
            Constructeur

            :param app: L'application
            :type app: FenetrePrincipale
        """
        # La liste principale qui s'affiche
        self.operations_widget = app.tabs.operation.operation
        self.add_button = app.tabs.operation.add_button

        # L'acces SQL
        self.operationSql = OperationSQL(Settings.get_instance().get('Database', 'filename', 'comptes.db'))
        self.budgetSql = BudgetSQL(Settings.get_instance().get('Database','filename','comptes.db'))
        self.compteSql = CompteSQL(Settings.get_instance().get('Database', 'filename', 'comptes.db'))

        # La liste des operations       
        self.operations = OperationListModele()
        # La liste des comptes
        self.comptes = list()
        # La liste des operations
        self.budgets = list()

        # Fonction d'initialisation des boutons et autres fonctionnalites
        self.init_controls()
        
        # Chargement de la base de donnees
        self.read_operation()

    def init_controls(self) -> None:
        """
            Cette fonction initialise les controles
        """
        self.add_button.clicked.connect(self.add_a_operation)

    def add_a_operation(self) -> None:
        """
            Ajoute une operation
        """
        # On cree la nouvelle operation
        operation = OperationModele(libelle="Nouvelle operation",montant=0,est_valide=False,est_verrouille=False)
        self.read_all_budget()
        self.read_all_compte()
        # On le sauvegarde en base de donnees
        try:
            operation = self.operationSql.save(operation)

            # On l'ajoute a la liste de traitement
            self.operations.append(operation)

            # On cree un widget pour l'affichage
            operation_item = OperationListWidgetItem(
                id=operation.id,
                libelle=operation.libelle,
                montant=operation.montant
            )
            
            # On ajoute les fonctions sur modification de l'operation
            operation_item.update_libelle.connect(self.update_operation_libelle) # Modification du libelle
            operation_item.update_montant.connect(self.update_operation_montant) # Modification du solde
            operation_item.update_compte.connect(self.update_operation_compte) # Modification du compte
            operation_item.update_budget.connect(self.update_operation_budget) # Modification du budget
            operation_item.valide_operation.connect(self.valide_operation) # Validation de l'operation
            operation_item.verouille_operation.connect(self.verouille_operation) # Verrouillage de l'operation           
            operation_item.delete_operation.connect(self.delete_operation) # Suppression de l'operation

            for c in self.comptes: 
                if not(c.est_archive):
                    operation_item.compte.addItem(c.libelle,c)

            for d in self.budgets:
                operation_item.budget.addItem(d.libelle,d)
            
            # On ajoute l'item a la liste d'affichage
            self.operations_widget.add_item(operation_item)
        except Exception as e:
            Logger.get_instance().error(f"Probleme de sauvegarde de la base de donnees {e}")

    def read_operation(self) -> None:
        """
            Va lire les operation dans la base de donnees
        """
        operations = self.operationSql.select_all()
        self.read_all_compte()
        self.read_all_budget()

        for b in operations:
            # On ajoute le compte a la liste des comptes
            self.operations.append(b)

            # On cree le widget associe
            operation_item = OperationListWidgetItem(
                id=b.id,
                libelle=b.libelle,
                montant=b.montant,
                est_valide=b.est_valide,
                est_verouille=b.est_verrouille
            )

            # Link des fonctions de traitement
            for c in self.comptes: 
                if not(c.est_archive):
                    operation_item.compte.addItem(c.libelle,c)
                    if c.id == b.compte:
                        operation_item.compte.setCurrentIndex(operation_item.compte.count()-1)

            operation_item.update_compte.connect(self.update_operation_compte) # Modification du compte

            for d in self.budgets:
                operation_item.budget.addItem(d.libelle,d)
                if d.id == b.budget:
                    operation_item.budget.setCurrentIndex(operation_item.budget.count()-1)
                            
            operation_item.update_budget.connect(self.update_operation_budget) # Modification du budget
            operation_item.update_libelle.connect(self.update_operation_libelle) # Modification du libelle
            operation_item.update_montant.connect(self.update_operation_montant) # Modification du solde
            operation_item.valide_operation.connect(self.valide_operation) # Validation d'operation
            operation_item.verouille_operation.connect(self.verouille_operation) # Verrouillage d'operation
            operation_item.delete_operation.connect(self.delete_operation) # Suppression d'operation

            # On ajoute l'element a liste d'affichage
            self.operations_widget.add_item(operation_item)

    def update_operation_libelle(self, new_libelle : str, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'une operation est modifiee et fait une sauvegarde dans la base de donnees

            :param operation: La nouvelle operation a sauvegarde
            :type operation: OperationModele
        """
        try:
            ret = self.operations.find_operation_from_id(id)
            if(ret is not None):
                ret["operation"].libelle = new_libelle
                self.operationSql.modify(ret["operation"])
            else:
                Logger.get_instance().error(f"Operation avec id : {id} non trouve dans la liste pour modification libelle")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de mettre a jour l'operation avec l'id : {id}. Erreur complete : {e}")

    def update_operation_montant(self, new_solde : float, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'une operation est modifiee et fait une sauvegarde dans la base de donnees

            :param operation: Le nouveau operation a sauvegarde
            :type operation: OperationModele
        """
        try:
            ret = self.operations.find_operation_from_id(id)
            if(ret is not None):
                ret["operation"].solde = new_solde
                self.operationSql.modify(ret["operation"])
                
            else:
                Logger.get_instance().error(f"Operation avec id : {id} non trouve dans la liste pour modification montant")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de mettre a jour l'operation avec l'id : {id}. Erreur complete : {e}")

    def update_operation_compte(self, id_compte : int, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'une operation est modifiee et fait une sauvegarde dans la base de donnees

            :param operation: Le nouveau operation a sauvegarde
            :type operation: OperationModele
        """
        try:
            ret = self.operations.find_operation_from_id(id)
            if(ret is not None):
                cp = self.comptes[id_compte]
                ret["operation"].compte = cp.id
                self.operationSql.modify(ret["operation"])
            else:
                Logger.get_instance().error(f"Operation avec id : {id} non trouve dans la liste pour modification compte")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de mettre a jour l'operation avec l'id : {id}. Erreur complete : {e}")

    def update_operation_budget(self, id_budget : int, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'une operation est modifiee et fait une sauvegarde dans la base de donnees

            :param operation: Le nouveau operation a sauvegarde
            :type operation: OperationModele
        """
        try:
            ret = self.operations.find_operation_from_id(id)
            if(ret is not None):
                bd = self.budgets[id_budget]
                ret["operation"].budget = bd.id
                self.operationSql.modify(ret["operation"])
            else:
                Logger.get_instance().error(f"Operation avec id : {id} non trouve dans la liste pour modification budget")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de mettre a jour l'operation avec l'id : {id}. Erreur complete : {e}")

    def delete_operation(self, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'une operation est modifie et fait la sauvegarde en base de donnees en plus de supprimer de la liste

            :param operation: L'identifiant du operation a supprimer
            :type operation: OperationModele
            :param row_pos: La position de la ligne a supprimer
            :type row_pos: int
        """
        try:
            ret = self.operations.find_operation_from_id(id)
            if(ret is not None):
                self.operations.remove(ret["operation"])
                self.operationSql.delete(ret["operation"])
                self.operations_widget.delete_item(ret["index"])
            else:
                Logger.get_instance().error(f"Operation avec id : {id} non trouve dans la liste pour suppression")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de supprimer l'operation avec l'id : {id}. Erreur complete : {e}")

    def valide_operation(self, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'un operation est modifie et fait la sauvegarde en base de donnees en plus de supprimer de la liste

            :param compte: L'identifiant du compte a supprimer
            :type compte: OperationModele
            :param row_pos: La position de la ligne a supprimer
            :type row_pos: int
        """
        try:
            ret = self.operations.find_operation_from_id(id)
            if(ret is not None):
                ret["operation"].est_valide = True
                self.operationSql.modify(ret["operation"])
            else:
                Logger.get_instance().error(f"Operation avec id : {id} non trouve dans la liste pour suppression")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de supprimer l'operation avec l'id : {id}. Erreur complete : {e}")

    def verouille_operation(self, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'un operation est modifie et fait la sauvegarde en base de donnees en plus de supprimer de la liste

            :param compte: L'identifiant du compte a supprimer
            :type compte: OperationModele
            :param row_pos: La position de la ligne a supprimer
            :type row_pos: int
        """
        try:
            ret = self.operations.find_operation_from_id(id)
            if(ret is not None):
                ret["operation"].est_verrouille = True
                self.operationSql.modify(ret["operation"])
            else:
                Logger.get_instance().error(f"Operation avec id : {id} non trouve dans la liste pour suppression")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de supprimer l'operation avec l'id : {id}. Erreur complete : {e}")

    def read_all_compte(self) -> None:
        self.comptes.clear()
        comptes = self.compteSql.select_all()
        for c in comptes:
            self.comptes.append(c)

    def read_all_budget(self) -> None:
        self.budgets.clear()
        budgets = self.budgetSql.select_all()
        for c in budgets:
            self.budgets.append(c)
