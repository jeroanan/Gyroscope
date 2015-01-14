import logging
import re
import time

from bs4 import BeautifulSoup
import math

import Request
from Config import Settings
from Uri import UriBuilder


def get_assets(html_str, site, page_uri, config):

    def request_all(assets, uri_attrib):

        def get_uri(asset):
            return UriBuilder.build_uri(asset, site["uri"])

        def do_request(uri):
            sizes.append(Request.get_request(uri, site, config).tell())

        uris = map(get_uri, map(lambda a: a[uri_attrib], assets))
        list(map(do_request, uris))

    def get_scripts():
        scripts = soup.findAll("script", src=re.compile(".*"))
        logging.info("Found %d external scripts" % len(scripts))
        request_all(scripts, "src")

    def get_images():

        def sizes_in_kilobytes():
            return math.ceil(sum(sizes)/1024)

        def average_size(number_of_items):
            return math.ceil(sizes_in_kilobytes() / number_of_items)

        sizes.clear()
        images = soup.findAll("img", src=re.compile(".*"))
        logging.info("Found %d images" % len(images))
        request_all(images, "src")
        logging.info("Got all images. Total size was %d KB" % sizes_in_kilobytes())
        logging.info("Average image size: %dKB" % average_size(len(images)))

    def get_stylesheets():
        stylesheets = soup.findAll("link", rel="stylesheet")
        logging.info("Found %d external stylesheets" % len(stylesheets))
        request_all(stylesheets, "href")

    def get_all_assets():
        if Settings.should_get_scripts(site, config):
            get_scripts()
        if Settings.should_get_images(site, config):
            get_images()
        if Settings.should_get_stylesheets(site, config):
            get_stylesheets()

    sizes = []
    logging.info("Getting assets for %s", page_uri)
    soup = BeautifulSoup(html_str)
    start_time = time.time()
    get_all_assets()
    time_elapsed = time.time() - start_time
    logging.info("Finished getting assets for %s. Took %d seconds." % (page_uri, time_elapsed))