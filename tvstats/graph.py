"""Helper functions for easy graph making"""

import matplotlib.pyplot as plt
import jsonhelper as jh


def graphdata(data):
    """returns ratings and episode number
    to be used for making graphs"""
    data = jh.get_ratings(data)
    num = 1
    rating_final = []
    episode_final = []
    for k,v in data.iteritems():
        rating=[]
        epinum=[]
        for r in v:
            if r != None:
                rating.append(float(r))
                epinum.append(num)
                num+=1
        rating_final.append(rating)
        episode_final.append(epinum)
    return rating_final,episode_final


def graph(data):
    """Draws graph of rating vs episode number"""
    title = data['name'] + ' (' + data['rating'] + ') '
    plt.title(title)
    plt.xlabel('Episode Number')
    plt.ylabel('Ratings')
    rf,ef=graphdata(data)
    col=['red', 'green' , 'orange']
    for i in range(len(rf)):
        x,y=ef[i],rf[i]
        k = i + 1
        plt.plot(x, y,color=col[i%3])
    x1, x2, y1, y2 = plt.axis()
    y2 = 10
    if y1 > 7:
        y1 = 7
    plt.axis([x1, x2, y1, y2])
    plt.show()
