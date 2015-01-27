import logging
import sys
from Config import LoadJson


def load_sites(sites_file):
    try:
        if sites_file is None:
            sites_file = "sites.json"
        for web_site in LoadJson.load_json(sites_file, "sites"):
            yield web_site
    except FileNotFoundError:
        logging.error("Unable to find {file_name}. Terminating.".format(file_name=sites_file))
        sys.exit(-1)
    except ValueError:
        logging.error("It seems that {file_name} is corrupt. Terminating.".format(file_name=sites_file))
        sys.exit(-1)