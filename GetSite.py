def get_site(site, config):

    import Request
    import GetAssets
    import GetPage
    from Config import Settings
    from Uri import UriBuilder

    def get_page(page):
        GetPage.request_page(page, site, config)

    http_request = Request.request(site["uri"], "index")

    if Settings.should_get_assets(site, config):
        GetAssets.get_assets(http_request.data, site, UriBuilder.join_uri(site["uri"], ""), config)
    if Settings.should_get_pages(site, config):
        list(map(get_page, site.get("pages", [])))
