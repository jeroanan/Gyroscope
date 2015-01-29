def load_json(file_name, root_element):
    import json
    from jsmin import jsmin

    with open(file_name) as f:
        return json.loads(jsmin(f.read()))[root_element]