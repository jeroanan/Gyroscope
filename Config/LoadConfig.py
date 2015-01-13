import logging
import sys
from Config import LoadJson


def load_config():
    try:
        return LoadJson.load_json("config.json", "config")
    except FileNotFoundError:
        logging.error("Unable to find config file. Terminating.")
        sys.exit(-1)
    except ValueError:
        logging.error("It seems that your config.json is corrupt. Terminating.")
        sys.exit(-1)