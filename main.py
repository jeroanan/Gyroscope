from collections import ChainMap
import logging
import time
import sys
import GetArgs

import GetSite
from Config import Defaults
from Config import LoadSites
from Config import LoadConfig
from Config import Settings


def work():

    def init_config():
        args = GetArgs.get_args()
        return ChainMap(args, LoadConfig.load_config(args.get("config")), Defaults.get_defaults())

    def init_logging():
        logfile_location = Settings.get_logfile_location(config)
        if logfile_location == "":
            logging.basicConfig(level=config["log_level"], format="%(asctime)s %(message)s")
        else:
            logging.basicConfig(filename=logfile_location, level=config["log_level"],
                                filemode=config["logfile_mode"], format="%(asctime)s %(message)s")

    def get_site(site):
        def site_disabled():
            return site.get("disabled", False)

        if not site_disabled():
            GetSite.get_site(site, config)

    config = init_config()
    init_logging()
    logging.info("Start")
    start_time = time.time()
    list(map(get_site, LoadSites.load_sites(config["sites_file"])))
    logging.info("End (total time: %d seconds)" % (time.time() - start_time))

try:
    work()
except KeyboardInterrupt:
    logging.shutdown()
    sys.exit(0)

