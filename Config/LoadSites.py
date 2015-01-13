import logging
import sys
from Config import LoadJson


def load_sites():
    try:
        for web_site in LoadJson.load_json("sites.json", "sites"):
            yield web_site
    except FileNotFoundError:
        logging.error("Unable to find sites.json. Terminating.")
        sys.exit(-1)