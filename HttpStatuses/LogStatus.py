import logging
from HttpStatuses import Status200


def log_status(http_request, uri, page_description, time_elapsed, site, config):
    def log_400():
        logging.error("Bad request: %s" % uri)

    def log_403():
        logging.error("Access denied: %s" % uri)

    def log_404():
        logging.error("Missing page: %s" % uri)

    def log_200():
        Status200.log_ok_status(uri, page_description, http_request.tell() / 1024, time_elapsed, site, config)

    def log_500():
        logging.critical("Error: %s" % uri)

    def log_default():
        logging.warning("%s (%s): %s" % (uri, page_description, http_request.status))

    status_methods = {
        400: log_400,
        403: log_403,
        404: log_404,
        200: log_200,
        500: log_500
    }
    status_methods.get(http_request.status, log_default)()
