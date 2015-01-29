def get_assets(html_str, site, page_uri, config):
    import logging
    import re
    import time

    from bs4 import BeautifulSoup
    import math

    import Request
    from Config import Defaults
    from Config import LoadAssetTypes
    from Uri import UriBuilder

    def request_all(assets, uri_attrib):

        def get_uri(asset):
            return UriBuilder.build_uri(asset, site["uri"])

        def do_request(uri):
            sizes.append(Request.get_request(uri, site, config).tell())

        uris = map(get_uri, map(lambda a: a[uri_attrib], assets))
        list(map(do_request, uris))

    def sizes_in_kilobytes():
        return math.ceil(sum(sizes) / 1024)

    def average_size(number_of_items):
        return math.ceil(sizes_in_kilobytes() / max(number_of_items, 1))

    def log_size_information(number_of_items, resource_type):
        logging.info("Got all {resource_type}s for {page_uri}. Total size was {total_size}KB.".format(
                     resource_type=resource_type, page_uri=page_uri, total_size=sizes_in_kilobytes()))

        logging.info("Average {resource_type} size: {average_size}KB.".format(
            resource_type=resource_type, average_size=average_size(number_of_items)))

    def get_asset(asset_type):
        sizes.clear()
        found_assets = soup.findAll(asset_type["tag_name"],
                                    attrs={asset_type["match_attrib"]: re.compile(asset_type["match_value"])})
        logging.info("Found {num_assets} {asset_name}s".format(num_assets=len(found_assets),
                                                               asset_name=asset_type["name"]))
        request_all(found_assets, asset_type["uri_attrib"])
        log_size_information(len(found_assets), asset_type["name"])

    def get_all_assets():
        def get_site_assets():
            if "asset_types" in site:
                return site["asset_types"]
            if "asset_types" in config:
                return config["asset_types"]
            return Defaults.get_defaults()["asset_types"]

        site_assets = get_site_assets()
        for asset_type in asset_types:
            if asset_type["name"] in site_assets:
                get_asset(asset_type)

    sizes = []
    logging.info("Getting assets for {page_uri}".format(page_uri=page_uri))
    soup = BeautifulSoup(html_str)
    asset_types = LoadAssetTypes.load_asset_types()
    start_time = time.time()
    get_all_assets()
    time_elapsed = time.time() - start_time
    logging.info("Finished getting assets for {page_uri}. Took {time_elapsed} seconds.".format(
        page_uri=page_uri, time_elapsed=time_elapsed))