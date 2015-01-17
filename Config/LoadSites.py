import logging
import sys
from Config import LoadJson


def load_sites(sites_file):
    try:
        for web_site in LoadJson.load_json(sites_file, "sites"):
            yield web_site
    except FileNotFoundError:
        logging.error("Unable to find %s. Terminating." % sites_file)
        sys.exit(-1)
    except ValueError:
        logging.error("It seems that your sites.json is corrupt. Terminating.")
        sys.exit(-1)