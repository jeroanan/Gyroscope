import logging
import time

import urllib3

from Checks import Checks
from HttpStatuses import LogStatus


def __request(uri, page_description, method, site, config, fields=None, second_chance=False, headers=None):
    def too_slow():
        return not Checks.time_acceptable(time_elapsed, config.get("acceptable_time", 100))

    def should_give_second_chance():
        return too_slow() and config.get("give_second_chance", True) and (not second_chance)

    def get_uri():
        return uri.replace(" ", "%20")

    logging.info("Getting %s (%s)" % (page_description, get_uri()))
    http = urllib3.PoolManager(retries=False)
    headers = urllib3.make_headers(keep_alive=True, accept_encoding=True)
    request_start_time = time.time()
    get_uri()
    http_request = http.request(method, get_uri(), fields=fields, headers=headers)
    time_elapsed = time.time() - request_start_time

    if should_give_second_chance():
        logging.info("Doing second chance request for %s (too slow first time at %d seconds)" % (uri, time_elapsed))
        return __request(uri, page_description, method, site, config, fields, second_chance=True, headers=headers)

    LogStatus.log_status(http_request, uri, page_description, time_elapsed, site, config)
    return http_request


def get_request(uri, site, config, page_description=""):
    return __request(uri, page_description, "GET", site, config)


def post_request(uri, page_description, fields, site, config):
    return __request(uri, page_description, "POST", site, config, fields)