def get_site(site, config):

    import Request
    import GetAssets
    import GetPage
    from Config import Settings
    from Uri import UriBuilder
    from functools import partial

    http_request = Request.get_request(site["uri"], site, config, "index")

    if Settings.should_get_assets(site, config):
        GetAssets.get_assets(http_request.data, site, UriBuilder.join_uri(site["uri"], ""), config)
    if Settings.should_get_pages(site, config):
        list(map(partial(GetPage.request_page, site=site, config=config), site.get("pages", [])))
