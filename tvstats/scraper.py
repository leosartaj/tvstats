from bs4 import BeautifulSoup as bs
import requests
import re
import json


ROOT = "http://imdb.com"


def dict_to_json(json_dict):
    """
    convert from a dictionary to json
    """
    return json.dumps(json_dict)


def get_html(link):
    return bs(requests.get(link).text)


def get_a(html, find=''):
    links = []
    for a in html.find_all('a'):
        if a.get('href').find(find) != -1:
            links.append(a)
    return links


def episode_list(a):
    html = get_html(ROOT + a.get('href'))
    div = html.find('div', {'class': "list detail eplist"})
    links = []
    for tag in div.find_all('a', {'itemprop': "name"}):
        links.append(tag)
    return links


def get_rating(html):
    try:
        div = html.find('div', {'class': "titlePageSprite star-box-giga-star"})
        return div.text
    except AttributeError:
        return None


def get_name_date(html):
    head = html.find('h1', {'class': "header"})
    spans = head.findChildren()
    name = spans[0].text
    date = spans[1].text[1:-1]
    return name, date


def get_season_epi_num(html):
    head = html.find('h2', {'class': "tv_header"})
    spans = head.findChildren()
    season, epi = spans[1].text.split(',')
    season = re.search('\d+', season).group()
    epi = re.search('\d+', epi).group()
    return season, epi


def parse_episode(a):
    d = {}
    html = get_html(ROOT + a.get('href'))
    d['rating'] = get_rating(html)
    d['episode-name'], d['date'] = get_name_date(html)
    d['season'], d['episode'] = get_season_epi_num(html)
    return d


def parse(link):
    html = get_html(link)

    data = {'rating': get_rating(html),
            'name': get_name_date(html)[0]}

    div = html.find(id="title-episode-widget")
    season_tags = get_a(div, find="season=")
    l = []
    for slink in season_tags:
        for e in episode_list(slink):
            l.append(parse_episode(e))
    data['episodes'] = l
    return dict_to_json(data)
