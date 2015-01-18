def request_page(page_to_request, site, config):

    import GetAssets
    import Request
    from Uri import UriBuilder

    def get_page_description():
        return page_to_request.get("description", "")

    full_uri = UriBuilder.join_uri(site["uri"], page_to_request["path"])
    req = Request.get_request(full_uri, site, config, get_page_description())
    GetAssets.get_assets(req.data, site, full_uri, config)
