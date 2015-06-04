"""Functions for scraping IMDB"""

from bs4 import BeautifulSoup as bs
import requests
import re


ROOT = "http://imdb.com"


def get_html(link):
    return bs(requests.get(link).text)


def get_a(html, find=''):
    """Finds all the 'a' tags with find in their href"""
    links = []
    for a in html.find_all('a'):
        if a.get('href').find(find) != -1:
            links.append(a)
    return links


def episode_list(a):
    """List of all episodes of a season"""
    html = get_html(ROOT + a.get('href'))
    div = html.find('div', {'class': "list detail eplist"})
    links = []
    for tag in div.find_all('a', {'itemprop': "name"}):
        links.append(tag)
    return links


def get_rating(html):
    """Rating of an episode
    Works for any page with a rating
    Incase no rating found, returns None
    """
    try:
        div = html.find('div', {'class': "titlePageSprite star-box-giga-star"})
        return div.text.strip(' ')
    except AttributeError:
        return None


def get_name_date(html):
    head = html.find('h1', {'class': "header"})
    spans = head.findChildren()
    name = spans[0].text
    if len(spans) == 2:
        date = spans[1].text[1:-1]
    else:
        date = None
    return name, date


def get_season_epi_num(html):
    head = html.find('h2', {'class': "tv_header"})
    spans = head.findChildren()
    if len(spans) == 2:
        season, epi = spans[1].text.split(',')
        season = re.search('\d+', season).group()
        epi = re.search('\d+', epi).group()
        return season, epi
    else:
        return None, None


def parse_episode(a):
    """Collects data related to an episode"""
    d = {}
    html = get_html(ROOT + a.get('href'))
    d['rating'] = get_rating(html)
    d['episode-name'], d['date'] = get_name_date(html)
    season, d['episode-num'] = get_season_epi_num(html)
    return season, d


def parse(link):
    """Parses a Tv Series
    returns the dataset as a dictionary
    """
    html = get_html(link)

    data = {'rating': get_rating(html),
            'name': get_name_date(html)[0]}

    div = html.find(id="title-episode-widget")
    season_tags = get_a(div, find="season=")
    episodes = {}
    for slink in season_tags:
        for e in episode_list(slink):
            season, d = parse_episode(e)
            if season in episodes:
                episodes[season].append(d)
            else:
                episodes[season] = [d]
    data['episodes'] = episodes
    return data
