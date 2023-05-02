AUTHOR = 'admin'
SITENAME = 'AdminLTE pelican'
SITEURL = ''
EMAIL = 'email@example.com'
PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

SLUGIFY_SOURCE = 'title'

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_URL = 'tags.html'

DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'

# Generate archive
ARCHIVES_SAVE_AS = 'archives/index.html'
ARCHIVES_URL = 'archives/'

# Theme settings
THEME = 'adminlte'
PYGMENTS_STYLE = 'nord'

STATIC_DIR = 'theme'

RECENT_POST_COUNT = 2

# Plugins
PLUGINS = []

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github source', 'https://github.com/AdminLTE-pelican/adminlte-pelican.github.io'),
         ('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
