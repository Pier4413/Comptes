from modules.logger.logger import Logger
from modules.settings.settings import Settings
from classes.sql.compte import Compte as CompteSQL
from classes.sql.budget import Budget as BudgetSQL
from classes.sql.operation import Operation as OperationSQL

def start_app(parameters : dict) -> None:
    """
        Cette fonction initialise le logger et charge le fichier de conf

        A noter cette fonction n'est pas teste car toutes les fonctions utilises au sein de cette fonction viennent de sous-module et sont sensé etre teste dans leur propre module

        :param parameters: Un dictionnaire des parametres necessaire pour initialiser les informations
        :type parameters: dict
    """
    # Logger loading
    Logger.get_instance().load_logger(info_file=parameters["log_info"], critical_file=parameters["log_critical"], console = True, level=parameters["log_level"], app_name="Accounts")
    
    # Printing options for debug purposes in the logger (i.e in files and console if wanted)
    Logger.get_instance().info("Given options : ")
    Logger.get_instance().info("--settings={}".format(parameters["conf_file_name"]))
    Logger.get_instance().info("--log_level={}".format(parameters["log_level"]))
    Logger.get_instance().info("--log_info_file={}".format(parameters["log_info"]))
    Logger.get_instance().info("--log_crit_file={}".format(parameters["log_critical"]))

    # Load settings
    Settings.get_instance().load_settings(parameters["conf_file_name"])

    compte_sql = CompteSQL(Settings.get_instance().get('Database', 'filename', 'comptes.db'))
    budget_sql = BudgetSQL(Settings.get_instance().get('Database', 'filename', 'comptes.db'))
    operation_sql = OperationSQL(Settings.get_instance().get('Database', 'filename', 'comptes.db'))

    # Test de creation de la table
    try:
        compte_sql.create_table()
        budget_sql.create_table()
        operation_sql.create_table()
    except Exception as e:
        Logger.get_instance().error("Could not create the table. Maybe it already exists"+str(e))
    else:
        Logger.get_instance().debug("Table created if not exists")

def clean_up():
    pass