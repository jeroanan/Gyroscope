from Config import LoadJson


def load_sites():
    for web_site in LoadJson.load_json("sites.json", "sites"):
        yield web_site