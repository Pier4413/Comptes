import sys

from modules.logger.logger import Logger

from utils import start_app

# Si on est dans la boucle principale
if __name__=="__main__":
    start_app(sys.argv[1:])
    Logger.get_instance().info("TEST CA MARCHE")
