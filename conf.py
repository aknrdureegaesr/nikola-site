#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################
# Configuration, please edit
########################################

# post_pages contains (wildcard, destination, template, use_in_feed) tuples.
#
# The wildcard is used to generate a list of reSt source files (whatever/thing.txt)
# That fragment must have an associated metadata file (whatever/thing.meta),
# and opcionally translated files (example for spanish, with code "es"):
#     whatever/thing.txt.es and whatever/thing.meta.es
#
# From those files, a set of HTML fragment files will be generated:
# whatever/thing.html (and maybe whatever/thing.html.es)
#
# These files are combinated with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is specified in the metadata file.
#
# if use_in_feed is True, then those posts will be added to the site's
# rss feeds.
#

post_pages = (
    ("posts/*.txt", "blog", "post.tmpl", True),
    ("stories/*.txt", "", "story.tmpl", False),
)

# What is the default language?

DEFAULT_LANG = "en"

# What languages do you have?
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location

TRANSLATIONS = {
    "en": "",
    }

# Paths for different autogenerated bits. These are combined with the translation
# paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
TAG_PATH = "categories"
# Final location is output / TRANSLATION[lang] / INDEX_PATH / index-*.html
INDEX_PATH = "blog"
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / archive.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
ARCHIVE_PATH = "archive"
# Final locations are:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
RSS_PATH = ""
TEMPLATE_ENGINE = "mako"
INPUT_FORMAT = "rest"
# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []

REDIRECTIONS = [] 

# Commands to execute to deploy. Can be anything, for example,
# you may use rsync:
# "rsync -rav output/* joe@my.site:/srv/www/site"
# And then do a backup, or ping pingomatic.
# To do manual deployment, set it to []
DEPLOY_COMMANDS = [
    r'rsync -rav --delete output/* ralsina@direct.ralsina.com.ar:/srv/www/nikola',
]

##############################################################################
# Image Gallery Options
##############################################################################

# Galleries are folders in galleries/
# Final location of galleries will be output / GALLERY_PATH / gallery_name
GALLERY_PATH = "galleries"
THUMBNAIL_SIZE = 180

##############################################################################
# HTML fragments and diverse things that are used by the templates
##############################################################################

# Data about this site
BLOG_TITLE = "Nikola"
BLOG_URL = "http://nikola.ralsina.com.ar"
BLOG_EMAIL = "ralsina@netmanagers.com.ar"
BLOG_DESCRIPTION = "A blog about Nikola, the static website generator."
BLOG_AUTHOR = "Roberto Alsina"

THEME = 'site'

# A HTML fragment describing the license, for the sidebar.
# I recomment using Creative Commons' wizard: http://creativecommons.org/choose/
LICENSE = """
    <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/2.5/ar/">
    <img alt="Creative Commons License" style="border-width:0; margin-bottom:12px;"
    src="http://i.creativecommons.org/l/by-nc-sa/2.5/ar/88x31.png"></a>"""

# A small copyright notice for the page footer
CONTENT_FOOTER = u'''Contents © 2012 Roberto Alsina <ralsina@kde.org>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="http://nikola.ralsina.com.ar">Powered by Nikola</a>&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="https://twitter.com/intent/follow?original_referer=http%3A%2F%2Fplatform.twitter.com%2Fwidgets%2Ffollow_button.1333526973.html&region=follow_link&screen_name=nikolagenerator&source=followbutton&variant=2.0">Follow Nikola on twitter</a>
'''

# To enable comments via Disqus, you need to create a forum at http://disqus.com,
# and set DISQUS_FORUM to the short name you selected.
# If you want to disable comments, set it to False.
DISQUS_FORUM = "nikolaweb"

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a feedburner feed or something else.

#RSS_LINK = """
    #<link rel="alternate" type="application/rss+xml" title="RSS" href="http://feeds.feedburner.com/LateralOpinion">
    #<link rel="alternate" type="application/rss+xml" title="RSS en Espanol" href="http://feeds.feedburner.com/LateralOpinionEsp">
#"""
RSS_LINK = None

# A search form to search this site, for the sidebar. You can use a google
# custom search (http://www.google.com/cse/)
# Or a duckduckgo search: https://duckduckgo.com/search_box.html
# This example should work for pretty much any site we generate.
SEARCH_FORM = """ """

# Google analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
ANALYTICS = """
<!-- Start of StatCounter Code for Default Guide -->
<script type="text/javascript">
var sc_project=7842875; 
var sc_invisible=1; 
var sc_security="3421486a"; 
</script>
<script type="text/javascript"
src="http://www.statcounter.com/counter/counter.js"></script>
<noscript><div class="statcounter"><a title="tumblr
statistics" href="http://statcounter.com/tumblr/"
target="_blank"><img class="statcounter"
src="http://c.statcounter.com/7842875/0/3421486a/1/"
alt="tumblr statistics"></a></div></noscript>
<!-- End of StatCounter Code for Default Guide -->
    """

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {
    'analytics': ANALYTICS,
    'blog_title': BLOG_TITLE,
    'blog_url': BLOG_URL,
    'blog_author': BLOG_AUTHOR,
    'translations': TRANSLATIONS,
    'license': LICENSE,
    'search_form': SEARCH_FORM,
    'disqus_forum': DISQUS_FORUM,
    'content_footer': CONTENT_FOOTER,
    'rss_path': RSS_PATH,
    'rss_link': RSS_LINK,
    # Locale-dependent links for the sidebar
    'sidebar_links': {
        'en': (
            ('/documentation.html', 'Documentation'),
            ('/blog/index.html', 'Blog'),
            ('http://groups.google.com/group/nikola-discuss', 'Forum'),
            ('https://github.com/ralsina/nikola', 'Source Code'),
            ('/changes.html', 'Changelog'),
            ('https://github.com/ralsina/nikola/issues', 'Report a Bug'),
            )
        }
    }


GZIP_FILES = True
