import sys
import i18n

from modules.logger.logger import Logger
from modules.settings.settings import Settings

from PyQt6.QtWidgets import QApplication
from utils.budget_control import BudgetControl

from views.fenetre_principale import FenetrePrincipale

from classes.sql.base import Base as BaseSQL

from utils.misc import parse_command_line
from utils.translation import i18n_loading
from utils.app import start_app, clean_up

# Si on est dans la boucle principale
if __name__=="__main__":

    # Parsing des options de la ligne de commande
    parameters = parse_command_line(sys.argv[1:])

    # Chargement des fichiers de conf et de logs
    start_app(parameters)

    # Chargement des traductions
    i18n_loading(Settings.get_instance().get('Translation', 'folder_path', "./resources/translation"), Settings.get_instance().get('Translation', 'locale', 'en'))

    # Ouverture de la base de donnees
    BaseSQL.get_instance(Settings.get_instance().get('Database', 'filename', 'comptes.db'))

    # Demarrage de l'application
    app=QApplication(sys.argv)

    # Connexion d'une fonction a la fermeture de l'application pour pouvoir decharger des choses si besoin (fermeture de la base de donnees par exemple)
    app.aboutToQuit.connect(clean_up)

    # Creation de la fenetre principale
    ex=FenetrePrincipale(app_name=i18n.t("translate.app_name"), width=Settings.get_instance().getint('Window', 'width', 1200), height=Settings.get_instance().getint('Window', 'height', 900))

    # Controleur pour les budgets
    budgetControl  = BudgetControl(ex)
    
    # Execution de l'application
    sys.exit(app.exec())