def get_defaults():
    return {
        "acceptable_size": 100,
        "acceptable_time": 3,
        "get_pages": False,
        "get_assets": False,
        "get_images": True,
        "get_scripts": True,
        "get_stylesheets": True,
        "give_second_chance": True,
        "logfile_location": "gyroscope.log",
        "logfile_mode": "w",
        "log_level": 30,
        "log_too_big": True,
        "log_too_slow": True,
        "sites_file": "sites.json"
    }