def build_uri(asset_uri, site_uri):
    asset_uri = asset_uri.strip("..")
    if asset_uri.startswith("http"):
        return asset_uri
    separator = ""
    if not asset_uri.startswith("/"):
        separator = "/"
    return "%s%s%s" % (site_uri, separator, asset_uri)


def join_uri(site_uri, file_path):
    return "%s%s" % (site_uri, file_path)