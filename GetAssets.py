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

    def sizes_in_kilobytes():
        return math.ceil(sum(sizes)/1024)

    def average_size(number_of_items):
        return math.ceil(sizes_in_kilobytes() / max(number_of_items, 1))

    def log_size_information(number_of_items, resource_type):
        logging.info("Got all {resource_type}s for {page_uri}. Total size was {total_size}KB.".format(
                     resource_type=resource_type, page_uri=page_uri, total_size=sizes_in_kilobytes()))

        logging.info("Average {resource_type} size: {average_size}KB.".format(
            resource_type=resource_type, average_size=average_size(number_of_items)))

    def get_asset(find_function, asset_type, uri_attrib):
        sizes.clear()
        found_assets = find_function()
        request_all(found_assets, uri_attrib)
        log_size_information(len(found_assets), asset_type)

    def get_scripts():
        def find():
            scripts = soup.findAll("script", src=re.compile(".*"))
            logging.info("Found {num_scripts} external scripts".format(num_scripts=len(scripts)))
            return scripts
        get_asset(find, "script", "src")

    def get_images():
        def find():
            images = soup.findAll("img", src=re.compile(".*"))
            logging.info("Found {num_images} images".format(num_images=len(images)))
            return images
        get_asset(find, "image", "src")

    def get_stylesheets():
        def find():
            stylesheets = soup.findAll("link", rel="stylesheet")
            logging.info("Found {num_stylesheets} external stylesheets".format(num_stylesheets=len(stylesheets)))
            return stylesheets
        get_asset(find, "stylesheet", "href")

    def get_all_assets():
        if Settings.should_get_scripts(site, config):
            get_scripts()
        if Settings.should_get_images(site, config):
            get_images()
        if Settings.should_get_stylesheets(site, config):
            get_stylesheets()

    sizes = []
    logging.info("Getting assets for {page_uri}".format(page_uri=page_uri))
    soup = BeautifulSoup(html_str)
    start_time = time.time()
    get_all_assets()
    time_elapsed = time.time() - start_time
    logging.info("Finished getting assets for {page_uri}. Took {time_elapsed} seconds.".format(
        page_uri=page_uri, time_elapsed=time_elapsed))