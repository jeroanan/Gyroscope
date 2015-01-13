def request_page(page_to_request, site, config):

    import GetAssets
    import Request
    from Config import Settings
    from Uri import UriBuilder

    def get_page_description():
        return page_to_request.get("description", "")

    full_uri = UriBuilder.join_uri(site["uri"], page_to_request["path"])
    req = Request.request(full_uri, get_page_description())
    if Settings.should_get_assets(site, config):
        GetAssets.get_assets(req.data, site, full_uri)
