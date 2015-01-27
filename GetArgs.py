import argparse


def get_args():
    def map_args_to_dict(a):
        def map_arg_if_not_none(mapping):
            if getattr(a, mapping[0]) is not None:
                mapped_args[mapping[1]] = getattr(a, mapping[0])

        mapped_args = {}
        mappings = [
            ("acceptablesize", "acceptable_size"),
            ("acceptabletime", "acceptable_time"),
            ("configfile", "config"),
            ("getimages", "get_images"),
            ("getpages", "get_pages"),
            ("getscripts", "get_scripts"),
            ("getstylesheets", "get_stylesheets"),
            ("logfile", "logfile_location"),
            ("loglevel", "log_level"),
            ("logtoobig", "log_too_big"),
            ("logtooslow", "log_too_slow"),
            ("sitesfile", "sites_file"),
            ("nologfile", "no_logfile"),
            ("noconfig", "no_config")
        ]

        list(map(map_arg_if_not_none, mappings))
        return mapped_args

    def parse_command_line():
        parser = argparse.ArgumentParser(formatter_class=argparse.MetavarTypeHelpFormatter)

        def add_arg(arg):
            parser.add_argument(arg[0], arg[1], help=arg[2], type=arg[3])

        known_args = [
            ("-as", "--acceptablesize", "Threshold size in kilobytes before a warning is logged stating that a page "
                                        "or asset is too big. Default 3.", int),

            ("-at", "--acceptabletime", "Threshold time in seconds before a warning is logged stating that a page "
                                        "or asset was retrieved from the web server too slowly. Default 100.", int),

            ("-c", "--configfile", "Path to configuration file. Default ./config.json.", str),

            ("-gi", "--getimages", "Whether to retrieve images. This argument is overridden by page"
                                   "config for individual sites. Default True.", bool),

            ("-gp", "--getpages", "Whether the pages configured for a site should be retrieved. This argument is "
                                  "overridden by page config for individual sites. Default True", bool),

            ("-gscripts", "--getscripts", "Whether to retrieve external scripts. This argument is overridden by page "
                                          "config for individual sites. Default True", bool),

            ("-gss", "--getstylesheets", "Whether to retrieve external stylesheets. This argument is overridden by "
                                         "page config for individual sites. Default True", bool),

            ("-gsc", "--givesecondchance", "Whether a slowly-loading page or asset should be requested a second time. "
                                           "The second response will then be measured. This argument is overridden by "
                                           "page config for individual sites. Default True", bool),

            ("-lf", "--logfile", "Path to logfile. Default. ./gyroscope.log.", str),

            ("-ll", "--loglevel", "Logging level. The logger will output messages at the same "
                                  "or higher severity than is set. 0 = No logging, 10 = Debug, "
                                  "20 = Info, 30 = Warning, 40 = Error, 50 = Critical. Default 20.", int),

            ("-ltb", "--logtoobig", "Whether log warnings should be output when a page or asset is too big according"
                                    "to acceptablesize. This argument is overridden by  page config for individual "
                                    "sites. Default True.", bool),

            ("-lts", "--logtooslow", "Whether log warnings should be output when a page or asset is too slow according"
                                     "to acceptabletime. This argument is overridden by  page config for individual "
                                     "sites. Default True.", bool),

            ("-nc", "--noconfig", "Whether to load a config file. If false then just command-line args and defaults"
                                  "will be used", bool),

            ("-nlf", "--nologfile", "Whether a log file shouldn't be used. If true then log will output to stdout.",
                bool),

            ("-sf", "--sitesfile", "The location of the sites file. Default ./sites.json.", str)
        ]

        list(map(add_arg, known_args))
        return parser.parse_args()

    return map_args_to_dict(parse_command_line())