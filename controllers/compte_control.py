from modules.logger.logger import Logger
from modules.settings.settings import Settings

from classes.elements.compte import Compte as CompteModele
from classes.elements.compte_list import CompteList as CompteListModele
from classes.sql.compte import Compte as CompteSQL


from views.fenetre_principale import FenetrePrincipale
from views.compte.list_item import CompteListWidgetItem

class CompteControl(object):

    def __init__(self, app : FenetrePrincipale) -> None:
        """
            Constructeur

            :param app: L'application
            :type app: FenetrePrincipale
        """
        # La liste principale qui s'affiche
        self.comptes_widget = app.tabs.comptes.comptes
        self.add_button = app.tabs.comptes.add_button

        # L'acces SQL
        self.compteSql = CompteSQL(Settings.get_instance().get('Database', 'filename', 'comptes.db'))

        # La liste des comptes       
        self.comptes = CompteListModele()

        # Fonction d'initialisation des boutons et autres fonctionnalites
        self.init_controls()
        
        # Chargement de la base de donnees
        self.read_comptes()

    def init_controls(self) -> None:
        """
            Cette fonction initialise les controles
        """
        self.add_button.clicked.connect(self.add_a_compte)

    def add_a_compte(self) -> None:
        """
            Ajoute un compte
        """
        # On cree le nouveau compte
        compte = CompteModele(libelle="Nouveau compte")
        
        # On le sauvegarde en base de donnees
        try:
            compte = self.compteSql.save(compte)

            # On l'ajoute a la liste de traitement
            self.comptes.append(compte)

            # On cree un widget pour l'affichage
            compte_item = CompteListWidgetItem(
                id=compte.id,
                libelle=compte.libelle,
                solde=compte.solde
            )
            
            # On ajoute les fonctions sur modification du compte
            compte_item.update_libelle.connect(self.update_compte_libelle) # Modification du libelle
            compte_item.update_init.connect(self.update_compte_init) # Modification du solde
            compte_item.delete_compte.connect(self.delete_compte) # Suppression du compte

            # On ajoute l'item a la liste d'affichage
            self.comptes_widget.add_item(compte_item)
        except Exception as e:
            Logger.get_instance().error(f"Probleme de sauvegarde de la base de donnees {e}")

    def read_comptes(self) -> None:
        """
            Va lire les comptes dans la base de donnees
        """
        comptes = self.compteSql.select_all()
        for b in comptes:
            # On ajoute le compte a la liste des comptes
            self.comptes.append(b)

            # On cree le widget associe
            compte_item = CompteListWidgetItem(
                id=b.id,
                libelle=b.libelle,
                solde=b.solde,
            )

            # Link des fonctions de traitement
            compte_item.update_libelle.connect(self.update_compte_libelle) # Modification du libelle
            compte_item.update_solde.connect(self.update_solde) # Modification du solde
            compte_item.delete_compte.connect(self.delete_compte) # Suppression du compte

            # On ajoute l'element a liste d'affichage
            self.comptes_widget.add_item(compte_item)

    def update_compte_libelle(self, new_libelle : str, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'un compte est modifie et fait une sauvegarde dans la base de donnees

            :param compte: Le nouveau compte a sauvegarde
            :type compte: CompteModele
        """
        try:
            ret = self.comptes.find_compte_from_id(id)
            if(ret is not None):
                ret["compte"].libelle = new_libelle
                self.compteSql.modify(ret["compte"])
            else:
                Logger.get_instance().error(f"Compte avec id : {id} non trouve dans la liste pour modification libelle")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de mettre a jour le compte avec l'id : {id}. Erreur complete : {e}")

    def update_solde(self, new_solde : float, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'un compte est modifie et fait une sauvegarde dans la base de donnees

            :param compte: Le nouveau compte a sauvegarde
            :type compte: CompteModele
        """
        try:
            ret = self.comptes.find_compte_from_id(id)
            if(ret is not None):
                ret["compte"].solde = new_solde
                self.compteSql.modify(ret["compte"])
            else:
                Logger.get_instance().error(f"Compte avec id : {id} non trouve dans la liste pour modification solde")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de mettre a jour le compte avec l'id : {id}. Erreur complete : {e}")

    def delete_compte(self, id : int) -> None:
        """
            Cette fonction est appelle lorsqu'un compte est modifie et fait la sauvegarde en base de donnees en plus de supprimer de la liste

            :param compte: L'identifiant du compte a supprimer
            :type compte: CompteModele
            :param row_pos: La position de la ligne a supprimer
            :type row_pos: int
        """
        try:
            ret = self.comptes.find_compte_from_id(id)
            if(ret is not None):
                self.compteSql.delete(ret["compte"])
                self.comptes_widget.delete_item(ret["index"])
            else:
                Logger.get_instance().error(f"Compte avec id : {id} non trouve dans la liste pour suppression")
        except Exception as e:
            Logger.get_instance().error(f"Impossible de supprimer le compte avec l'id : {id}. Erreur complete : {e}")

