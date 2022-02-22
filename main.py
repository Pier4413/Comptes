import sys

from modules.logger.logger import Logger
from modules.settings.settings import Settings

from PyQt6.QtWidgets import QApplication

from views.fenetre_principale import FenetrePrincipale

from utils.misc import parse_command_line
from utils.i18n import i18n_loading
from utils.app import start_app, clean_up

# Si on est dans la boucle principale
if __name__=="__main__":

    # Parsing des options de la ligne de commande
    parameters = parse_command_line(sys.argv[1:])

    # Chargement des fichiers de conf et de logs
    start_app(parameters)

    # Chargement des traductions
    i18n_loading(Settings.get_instance().get('translation', 'folder_path', "./resources/translation"), Settings.get_instance().get('translation', 'locale', 'en'))

    # Demarrage de l'application
    app=QApplication(sys.argv)

    # Connexion d'une fonction a la fermeture de l'application pour pouvoir decharger des choses si besoin (fermeture de la base de donnees par exemple)
    app.aboutToQuit.connect(clean_up)

    # Creation de la fenetre principale
    ex=FenetrePrincipale()

    # Execution de l'application
    sys.exit(app.exec())