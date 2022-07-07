import this
from classes.elements import operation
from modules.logger.logger import Logger
from modules.settings.settings import Settings

from classes.elements.operation import Operation as OperationModele
from classes.elements.operation_list import OperationList as OperationListModele
from classes.sql.operation import Operation as OperationSQL
from classes.elements.compte import Compte as CompteModele
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

        # La liste des operation       
        self.operations = OperationListModele()

        # Fonction d'initialisation des boutons et autres fonctionnalites
        self.init_controls()
        
        # Chargement de la base de donnees
        self.read_operation()

        self.operations_list = list()

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
        operation = OperationModele(libelle="Nouvelle operation",montant=0)
        
        # On le sauvegarde en base de donnees
        try:
            operation = self.operationSql.save(operation)

            # On l'ajoute a la liste de traitement
            self.operations.append(operation)

            # On cree un widget pour l'affichage
            operation_item = OperationListWidgetItem(
                id=operation.id,
                libelle=operation.libelle,
                montant=operation.montant,
                compte=operation.compte,
                budget=operation.budget
            )
            
            # On ajoute les fonctions sur modification de l'operation
            operation_item.update_libelle.connect(self.update_operation_libelle) # Modification du libelle
            operation_item.update_montant.connect(self.update_operation_montant) # Modification du solde
            operation_item.update_compte.connect(self.update_operation_compte) # Modification du compte
            operation_item.update_budget.connect(self.update_operation_budget) # Modification du budget
            #operation_item.valide_operation.connect(self.delete_operation) # Validation de l'operation
            #operation_item.verrouille_operation.connect(self.delete_operation) # Verrouillage de l'operation           
            operation_item.delete_operation.connect(self.delete_operation) # Suppression de l'operation
            operation_item.read_all_compte.connect(self.read_all_compte)

            self.operations_list.append(operation_item)

            operation_item.compte.addItem("Test")

            # On ajoute l'item a la liste d'affichage
            self.operations_widget.add_item(operation_item)
        except Exception as e:
            Logger.get_instance().error(f"Probleme de sauvegarde de la base de donnees {e}")

    def read_all_compte(self) -> None:
        compte = self.operations_list[0].compte.addItem("test")

    def read_operation(self) -> None:
        """
            Va lire les operation dans la base de donnees
        """
        operations = self.operationSql.select_all()
        for b in operations:
            # On ajoute le compte a la liste des comptes
            self.operations.append(b)

            # On cree le widget associe
            operation_item = OperationListWidgetItem(
                id=b.id,
                libelle=b.libelle,
                montant=b.montant,
                compte=b.montant,
                budget=b.budget
            )

            # Link des fonctions de traitement
            operation_item.update_libelle.connect(self.update_operation_libelle) # Modification du libelle
            operation_item.update_montant.connect(self.update_operation_montant) # Modification du solde
            operation_item.update_compte.connect(self.update_operation_compte) # Modification du compte
            operation_item.update_budget.connect(self.update_operation_budget) # Modification du solde
            #operation_item.valide_operation.connect(self.valide_operation) # Validation d'operation
            #operation_item.verrouille_operation.connect(self.verrouille_operation) # Verrouillage d'operation
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

    def update_operation_compte(self, new_compte : str, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'une operation est modifiee et fait une sauvegarde dans la base de donnees

            :param operation: Le nouveau operation a sauvegarde
            :type operation: OperationModele
        """
        try:
            ret = self.operations.find_operation_from_id(id)
            if(ret is not None):
                ret["operation"].compte = new_compte
                self.operationSql.modify(ret["operation"])
            else:
                Logger.get_instance().error(f"Operation avec id : {id} non trouve dans la liste pour modification compte")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de mettre a jour l'operation avec l'id : {id}. Erreur complete : {e}")

    def update_operation_budget(self, new_budget : str, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'une operation est modifiee et fait une sauvegarde dans la base de donnees

            :param operation: Le nouveau operation a sauvegarde
            :type operation: OperationModele
        """
        try:
            ret = self.operations.find_operation_from_id(id)
            if(ret is not None):
                ret["operation"].budget = new_budget
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
                self.operations.remove(ret["operation"])
                self.operationSql.delete(ret["operation"])
                self.operations_widget.delete_item(ret["index"])
            else:
                Logger.get_instance().error(f"Operation avec id : {id} non trouve dans la liste pour suppression")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de supprimer l'operation avec l'id : {id}. Erreur complete : {e}")
