from modules.logger.logger import Logger
from modules.settings.settings import Settings

def start_app(parameters : dict) -> None:
    """
        Cette fonction initialise le logger et charge le fichier de conf

        A noter cette fonction n'est pas teste car toutes les fonctions utilises au sein de cette fonction viennent de sous-module et sont sensé etre teste dans leur propre module

        :param parameters: Un dictionnaire des parametres necessaire pour initialiser les informations
        :type parameters: dict
    """
    # Logger loading
    Logger.get_instance().load_logger(info_file=parameters["log_info"], critical_file=parameters["log_critical"], level=parameters["log_level"])
    
    # Printing options for debug purposes in the logger (i.e in files and console if wanted)
    Logger.get_instance().info("Given options : ")
    Logger.get_instance().info("--settings={}".format(parameters["conf_file_name"]))
    Logger.get_instance().info("--log_level={}".format(parameters["log_level"]))
    Logger.get_instance().info("--log_info_file={}".format(parameters["log_info"]))
    Logger.get_instance().info("--log_crit_file={}".format(parameters["log_critical"]))

    # Load settings
    Settings.get_instance().load_settings(parameters["conf_file_name"])

def clean_up():
    pass