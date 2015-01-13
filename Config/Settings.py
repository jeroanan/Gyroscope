def should_get_assets(site_config, app_config):
        return site_config.get("get_assets", app_config.get("get_assets", False))


def should_get_pages(site_config, app_config):
    return site_config.get("get_pages", app_config.get("get_pages", True))