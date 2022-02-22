def start_app(args):
    """
        Cette fonction charge les d'options et initialise les loggers a partir des options fournis en commande

        Par exemple si on fournit le tableau suivant :
        ["--settings=./conf/settings.ini", "--log_info_file=./logs/info.log"]

        Alors on chargera le fichier ./conf/settings.ini pour le fichier de settings  et on enregistrera les logs de nvieau info max dans le fichier ./logs/info

        :param args: Le tableau des options que l'on fournit en parametre
        :type args: []
    """
    import getopt
    from modules.logger.logger import Logger
    from modules.settings.settings import Settings

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

    # Logger loading
    Logger.get_instance().load_logger(info_file=log_info, critical_file=log_critical, level=log_level)
    
    # Printing options for debug purposes in the logger (i.e in files and console if wanted)
    Logger.get_instance().info("Given options : ")
    Logger.get_instance().info("--settings={}".format(conf_file_name))
    Logger.get_instance().info("--log_level={}".format(log_level))
    Logger.get_instance().info("--log_info_file={}".format(log_info))
    Logger.get_instance().info("--log_crit_file={}".format(log_critical))

    # Load settings
    Settings.get_instance().load_settings(conf_file_name)