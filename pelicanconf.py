#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cameron Malloy'
SITENAME = 'Cameron Malloy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Tijuana'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%d %b %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL_LINKS = {'Github': 'https://www.github.com/cameronmalloy',
                'Twitter': 'https://www.twitter.com/spectraldecomp',
                'LinkedIn': 'https://www.linkedin.com/in/cameron-malloy'}

STATIC_PATHS = ['assets']

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS = 'UA-168820719-1'

THEME = 'pelican-themes/attila'
