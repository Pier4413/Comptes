import sys
import getopt
from dotenv import load_dotenv

from modules.logger.logger import Logger
from modules.settings.settings import Settings

def start_app():
    conf_file_name = "./conf/settings.ini"
    env_file_name = "./conf/.env"
    log_info = "./logs/info.log"
    log_critical = "./logs/critical.log"
    log_level = 20
    
    # Process command line options
    opts, args = getopt.getopt(sys.argv[1:], "", ["settings=","env=","log_level=", "log_info_file=", "log_crit_file="])

    for opt, arg in opts:
        if opt in ["--settings"]:
            conf_file_name = arg
        elif opt in ["--env"]:
            env_file_name = arg
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
    Logger.get_instance().info("--env={}".format(env_file_name))
    Logger.get_instance().info("--log_level={}".format(log_level))
    Logger.get_instance().info("--log_info_file={}".format(log_info))
    Logger.get_instance().info("--log_crit_file={}".format(log_critical))

    # Opening informations in .env and .ini files
    load_dotenv(env_file_name)

    # Load settings
    Settings.get_instance().load_settings(conf_file_name)

# Si on est dans la boucle principale
if __name__=="__main__":
    start_app()
