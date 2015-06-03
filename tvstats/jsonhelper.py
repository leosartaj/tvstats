import json


def dict_to_json(json_dict):
    """
    convert from a dictionary to json
    """
    return json.dumps(json_dict)


def json_to_dict(json_str):
    """
    convert from json to dictionary
    """
    return json.loads(json_str)
