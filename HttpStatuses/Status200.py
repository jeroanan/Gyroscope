def log_ok_status(uri, page_description, size, time_elapsed, site, config):

    import logging
    from Config import LoadConfig
    from Config import Settings
    from Checks import Checks

    def log_time_unacceptable():
        if not Settings.should_log_too_slow(site, config):
            return
        logging.warning("%s (%s): took too long! (took %d seconds; acceptable time: %d seconds)" %
                        (uri, page_description, time_elapsed, acceptable_time))

    def log_size_unacceptable():
        logging.warning("%s (%s) is too big! It was %d KB, acceptable size is %d KB" %
                        (uri, page_description, size, acceptable_size))

    def __need_to_log_too_big():
        return (not Checks.check_size_acceptable(size, acceptable_size)) and Settings.should_log_too_big(site, config)

    def __need_to_log_too_small():
        return not Checks.time_acceptable(time_elapsed, acceptable_time) and Settings.should_log_too_slow(site, config)

    config = LoadConfig.load_config()
    acceptable_time = config.get("acceptable_time", 3)
    acceptable_size = config.get("acceptable_size", 100)

    if __need_to_log_too_small():
        log_time_unacceptable()
        if __need_to_log_too_big():
            log_size_unacceptable()
    else:
        if __need_to_log_too_big():
            log_size_unacceptable()
        else:
            logging.info("%s (%s): 200 OK (took %d seconds)" % (uri, page_description, time_elapsed))