from Config import LoadJson


def load_config():
    return LoadJson.load_json("config.json", "config")