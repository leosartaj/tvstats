Tvstats
*******
Scrape data of all the episodes of a Tv Series from IMDB.

Installation
============
Run
::

    python setup.py install

Dependencies
============
tvstats is based on Python 2.7. Requires ``BeautifulSoup4`` for parsing, ``requests`` for downloading html.
``Matplotlib`` is required(optional) for using graph module.

Usage
=====
Run the simple command
::

    tvstats url

to generate json data.
URL should point to homepage of a tv series. eg. http://www.imdb.com/title/tt0108778/?ref_=fn_al_tt_1

For options and help run
::

    tvstats -h

Why?
====
Here are my reasons:

* I was bored and had time to kill.
* I love watching Tv Series. Thought it would be good to analyse some data
  before starting a new one.
* Graphs are fun.
* Lastly, I wanted to test out ``BeautifulSoup4`` :).

Examples
========
.. _here: https://github.com/leosartaj/tvstats/tree/master/data/jsonData
.. _Graphs: https://github.com/leosartaj/tvstats/tree/master/data/graphs

All the datasets can be found here_. Graphs_ were made using ``graph`` function in 'graph.py'.

Friends
-------

.. image:: https://raw.githubusercontent.com/leosartaj/tvstats/master/data/graphs/friends.png

Game Of Thrones
---------------

.. image:: https://raw.githubusercontent.com/leosartaj/tvstats/master/data/graphs/gameOfThrones.png

Breaking Bad
-------------

.. image:: https://raw.githubusercontent.com/leosartaj/tvstats/master/data/graphs/breakingBad.png

How I Met Your Mother
---------------------

.. image:: https://raw.githubusercontent.com/leosartaj/tvstats/master/data/graphs/himym.png

Prison Break
------------

.. image:: https://raw.githubusercontent.com/leosartaj/tvstats/master/data/graphs/prisonBreak.png

Hannibal
---------

.. image:: https://raw.githubusercontent.com/leosartaj/tvstats/master/data/graphs/hannibal.png

Suits
------

.. image:: https://raw.githubusercontent.com/leosartaj/tvstats/master/data/graphs/suits.png

Arrow
------

.. image:: https://raw.githubusercontent.com/leosartaj/tvstats/master/data/graphs/arrow.png

Person Of Interest
------------------

.. image:: https://raw.githubusercontent.com/leosartaj/tvstats/master/data/graphs/personOfInterest.png

Homeland
---------

.. image:: https://raw.githubusercontent.com/leosartaj/tvstats/master/data/graphs/homeland.png

Bugs
====
.. |issues| replace:: https://github.com/leosartaj/tvstats/issues

For filing bugs raise an issue at |issues|
