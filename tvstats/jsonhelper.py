import json
import collections as co


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


def get_data(fname):
    """returns dictionary"""
    with open(fname) as f:
        return json_to_dict(f.read())


def collapse(season):
    """Collects all the ratings of episodes from a season"""
    l = []
    for epi in season:
        l.append(epi['rating'])
    return l


def get_ratings(data):
    """Ratings of all the episodes of all the seasons"""
    episodes = data['episodes']
    ratings = {}
    for season in episodes:
        ratings[season] = collapse(episodes[season])
    return co.OrderedDict(sorted(ratings.items()))
