def __get_setting(site_config, app_config, key, default_value):
    return site_config.get(key, app_config.get(key, default_value))


def should_get_assets(site_config, app_config):
    return __get_setting(site_config, app_config, "get_assets", False)


def should_get_images(site_config, app_config):
    return __get_setting(site_config, app_config, "get_images", True)


def should_get_scripts(site_config, app_config):
    return __get_setting(site_config, app_config, "get_scripts", True)


def should_get_stylesheets(site_config, app_config):
    return __get_setting(site_config, app_config, "get_stylesheets", True)


def should_get_pages(site_config, app_config):
    return __get_setting(site_config, app_config, "get_pages", True)