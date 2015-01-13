import logging
import time

import urllib3

from HttpStatuses import Status200
from Checks import Checks

def __log_status(http_request, uri, page_description, time_elapsed, site, config):
        if http_request.status == 404:
            logging.error("Missing page: %s" % uri)
        elif http_request.status == 200:
            Status200.log_ok_status(uri, page_description, http_request.tell()/1024, time_elapsed,
                                    http_request.status, site, config)
        else:
            logging.warning("%s (%s): %s" % (uri, page_description, http_request.status))


def __request(uri, page_description, method, site, config, fields=None, second_chance=False):

    def too_slow():
        return not Checks.time_acceptable(time_elapsed, config.get("acceptable_time", 100))

    def should_give_second_chance():
        return too_slow() and config.get("give_second_chance", True) and (not second_chance)

    logging.info("Getting %s (%s)" % (page_description, uri))
    http = urllib3.PoolManager(retries=False)

    request_start_time = time.time()
    http_request = http.request(method, uri, fields=fields)
    time_elapsed = time.time() - request_start_time

    if should_give_second_chance():
        logging.info("Doing second chance request for %s (too slow first time at %d seconds)" % (uri, time_elapsed))
        return __request(uri, page_description, method, site, config, fields, second_chance=True)

    __log_status(http_request, uri, page_description, time_elapsed, site, config)
    return http_request


def get_request(uri, site, config, page_description=""):
    return __request(uri, page_description, "GET", site, config)


def post_request(uri, page_description, fields, site, config):
    return __request(uri, page_description, "POST", site, config, fields)