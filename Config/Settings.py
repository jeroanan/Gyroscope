def __get_setting(site_config, app_config, key, default_value):
    return site_config.get(key, app_config.get(key, default_value))


def get_logfile_location(app_config):
    return app_config.get("logfile_location", "")


def get_log_level(app_config):
    app_config.get("log_level", 20)


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


def should_log_too_big(site_config, app_config):
    return __get_setting(site_config, app_config, "log_too_big", True)


def should_log_too_slow(site_config, app_config):
    return __get_setting(site_config, app_config, "log_too_slow", True)