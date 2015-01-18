def request_page(page_to_request, site, config):
    import GetAssets
    import Request

    from collections import ChainMap

    from Config import PageDefaults
    from Uri import UriBuilder

    def do_request():
        if page_config["method"] == "GET":
            return Request.get_request(full_uri, site, config, page_config["description"])
        else:
            response = Request.post_request(full_uri, site, config, page_config["postdata"], page_config["description"])
            return response

    page_config = ChainMap(page_to_request, PageDefaults.get_default())
    full_uri = UriBuilder.join_uri(site["uri"], page_config["path"])
    req = do_request()
    GetAssets.get_assets(req.data, site, full_uri, config)
