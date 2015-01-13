import logging
import time

import urllib3

from HttpStatuses import Status200


def __log_status(http_request, uri, page_description, time_elapsed):
        if http_request.status == 404:
            logging.error("Missing page: %s" % uri)
        elif http_request.status == 200:
            Status200.log_ok_status(uri, page_description, http_request.tell()/1024, time_elapsed,
                                    http_request.status)
        else:
            logging.warning("%s (%s): %s" % (uri, page_description, http_request.status))


def __request(uri, page_description, method, fields=None):
    logging.info("Getting %s (%s)" % (page_description, uri))
    http = urllib3.PoolManager(retries=False)
    request_start_time = time.time()
    http_request = http.request(method, uri, fields=fields)
    time_elapsed = time.time() - request_start_time
    __log_status(http_request, uri, page_description, time_elapsed)
    return http_request


def get_request(uri, page_description=""):
    return __request(uri, page_description, "GET")


def post_request(uri, page_description, fields):
    return __request(uri, page_description, "POST", fields)