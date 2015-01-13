import logging
import re
import time

from bs4 import BeautifulSoup

import Request
from Uri import UriBuilder


def get_assets(html_str, site_uri, page_uri):

    def request_all(assets, uri_attrib):

        def get_uri(asset):
            return UriBuilder.build_uri(asset, site_uri)

        uris = map(get_uri, map(lambda a: a[uri_attrib], assets))
        list(map(Request.request, uris))

    def get_scripts():
        scripts = soup.findAll("script", src=re.compile(".*"))
        logging.info("Found %d external scripts" % len(scripts))
        request_all(scripts, "src")

    def get_images():
        images = soup.findAll("img", src=re.compile(".*"))
        logging.info("Found %d images" % len(images))
        request_all(images, "src")

    def get_stylesheets():
        stylesheets = soup.findAll("link", rel="stylesheet")
        logging.info("Found %d external stylesheets" % len(stylesheets))
        request_all(stylesheets, "href")

    def get_all_assets():
        get_scripts()
        get_images()
        get_stylesheets()

    logging.info("Getting assets for %s", site_uri)
    soup = BeautifulSoup(html_str)
    start_time = time.time()
    get_all_assets()
    time_elapsed = time.time() - start_time
    logging.info("Finished getting assets for %s. Took %d seconds." % (page_uri, time_elapsed))