"""Helper functions for easy graph making"""

import matplotlib.pyplot as plt
import jsonhelper as jh


def graphdata(data):
    """returns ratings and episode number
    to be used for making graphs"""
    data = jh.get_ratings(data)
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
