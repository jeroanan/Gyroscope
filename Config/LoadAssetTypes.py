def load_asset_types():
    import logging
    from Config import LoadJson

    try:
        return LoadJson.load_json("Data/AssetTypes.json", "asset_types")
    except FileNotFoundError:
        logging.critical("Unable to find Data/AssetTypes.json")
        return {}
    except ValueError:
        logging.critical("Data/AssetTypes.json has become corrupted")
        return {}
