def log_ok_status(uri, page_description, size, time_elapsed, status):

    import logging
    from Config import LoadConfig
    from Checks import Checks

    def log_time_unacceptable():
        logging.warning("%s (%s): took too long! (took %d seconds; acceptable time: %d seconds)" %
                        (uri, page_description, time_elapsed, acceptable_time))

    def log_size_unacceptable():
        logging.warning("%s (%s) is too big! It was %d KB, acceptable size is %d KB" %
                        (uri, page_description, size, acceptable_size))

    config = LoadConfig.load_config()
    acceptable_time = config.get("acceptable_time", 3)
    acceptable_size = config.get("acceptable_size", 100)

    if not Checks.time_acceptable(time_elapsed, acceptable_time):
        log_time_unacceptable()
        if not Checks.check_size_acceptable(size, acceptable_size):
            log_size_unacceptable()
    else:
        if Checks.check_size_acceptable(size, acceptable_size):
            logging.info("%s (%s): %s OK (took %d seconds)" %
                         (uri, page_description, status, time_elapsed))
        else:
            log_size_unacceptable()