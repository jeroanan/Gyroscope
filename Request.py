import logging
import time

import urllib3

from HttpStatuses import Status200


def request(uri, page_description=""):

    def log_status():
        if http_request.status == 404:
            logging.error("Missing page: %s" % uri)
        elif http_request.status == 200:
            Status200.log_ok_status(uri, page_description, http_request.tell()/1024, time_elapsed,
                                    http_request.status)
        else:
            logging.warning("%s (%s): %s" % (uri, page_description, http_request.status))

    logging.info("Getting %s (%s)" % (page_description, uri))
    http = urllib3.PoolManager(retries=False)
    request_start_time = time.time()
    http_request = http.request("GET", uri)
    time_elapsed = time.time() - request_start_time
    log_status()
    return http_request
