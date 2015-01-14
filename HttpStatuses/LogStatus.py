import logging
from HttpStatuses import Status200


def log_status(http_request, uri, page_description, time_elapsed, site, config):
    def log_404():
        logging.error("Missing page: %s" % uri)

    def log_200():
        Status200.log_ok_status(uri, page_description, http_request.tell() / 1024, time_elapsed, site, config)

    def log_default():
        logging.warning("%s (%s): %s" % (uri, page_description, http_request.status))

    status_methods = {404: log_404, 200: log_200}
    status_methods.get(http_request.status, log_default)()
