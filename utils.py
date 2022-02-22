import getopt
import i18n
from typing import Any

def parse_command_line(args : Any) -> dict:
    """
        Cette fonction parse la ligne de commande des options fournis et le renvoi sous forme de dictionnaire d'options

        Par exemple si on fournit le tableau suivant :
        ["--settings=./conf/settings.ini", "--log_info_file=./logs/info.log"]

        A noter qu'il existe des valeurs par defaut pour toutes les options propose afin que si l'information n'est pas passe une valeur par defaut puisse
        etre utilise

        :param args: Le tableau des options que l'on fournit en parametre
        :type args: []
        :return: Un dictionnaire avec les informations de la ligne de commande
        :rtype: dict
    """
    conf_file_name = "./conf/settings.ini"
    log_info = "./logs/info.log"
    log_critical = "./logs/critical.log"
    log_level = 20
    
    # Process command line options
    opts, args = getopt.getopt(args, "", ["settings=","log_level=", "log_info_file=", "log_crit_file="])

    for opt, arg in opts:
        if opt in ["--settings"]:
            conf_file_name = arg
        elif opt in ["--log_level"]:
            log_level = int(arg)
        elif opt in ["--log_info_file"]:
            log_info = arg
        elif opt in ["--log_crit_file"]:
            log_critical = arg
        else:
            print("Option not handled")

    return {
        "conf_file_name": conf_file_name,
        "log_level": log_level,
        "log_info": log_info,
        "log_critical": log_critical
    }

def i18n_loading(translationPath : str, locale : str) -> None:
    """
        Cette fonction charge les fichiers de traduction

        :param translationPath: Le dossier des fichiers de traduction
        :type translationPath: str
        :param locale: La locale a utiliser
        :type locale: str
    """    
    i18n.load_path.append(translationPath)
    i18n.set('locale', locale)
    i18n.set('fallback', 'en')
