import logging
import sys
from Config import LoadJson


def load_config(config_file="config.json", no_config=False):
    try:
        if no_config:
            return {}
        if config_file is None:
            config_file = "config.json"
        return LoadJson.load_json(config_file, "config")
    except FileNotFoundError:
        logging.error("Unable to find config file %s. Terminating." % config_file)
        sys.exit(-1)
    except ValueError:
        logging.error("It seems that your config file is corrupt. Terminating.")
        sys.exit(-1)