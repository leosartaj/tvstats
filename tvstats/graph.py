"""Helper functions for easy graph making"""

import matplotlib.pyplot as plt
import collections as co
import jsonhelper as jh


def get_data(fname):
    """returns dictionary"""
    with open(fname) as f:
        return jh.json_to_dict(f.read())


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


def graphdata(data):
    """returns ratings and episode number
    to be used for making graphs"""
    data = get_ratings(data)
    num = 1
    rating, epinum = [], []
    for k, v in data.iteritems():
        for r in v:
            if r != None:
                rating.append(float(r))
                epinum.append(num)
                num += 1
    return epinum, rating


def graph(data):
    """Draws graph of rating vs episode number"""
    title = data['name'] + ' (' + data['rating'] + ') '
    plt.title(title)
    plt.xlabel('Episode Number')
    plt.ylabel('Ratings')
    x, y = graphdata(data)
    plt.plot(x, y, 'r')
    plt.show()
