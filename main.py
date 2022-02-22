import sys

from modules.logger.logger import Logger

from utils import start_app, parse_command_line

# Si on est dans la boucle principale
if __name__=="__main__":
    parameters = parse_command_line(sys.argv[1:])
    start_app(parameters)
    Logger.get_instance().info("TEST CA MARCHE")
