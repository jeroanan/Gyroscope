import logging
import time
import sys

import GetSite
from Config import LoadSites
from Config import LoadConfig


def work():

    def init_logging():
        logfile_location = config.get("logfile_location", "")
        if logfile_location == "":
            logging.basicConfig(level=config.get("log_level", 20), format="%(asctime)s %(message)s")
        else:
            logging.basicConfig(filename=logfile_location, level=config.get("log_level", 20),
                                filemode=config.get("logfile_mode", "a"), format="%(asctime)s %(message)s")

    def get_site(site):
        GetSite.get_site(site, config)

    config = LoadConfig.load_config()
    init_logging()
    logging.info("Start")
    start_time = time.time()
    list(map(get_site, LoadSites.load_sites()))
    logging.info("End (total time: %d seconds)" % (time.time() - start_time))

try:
    work()
except KeyboardInterrupt:
    logging.shutdown()
    sys.exit(0)

