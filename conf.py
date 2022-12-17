from ablog.conf import *

org = 'photon-platform'
org_name = 'PHOTON platform'

repo = ''
repo_name = ''

blog_title = f'{org_name}'
project = f'{org_name}'
version = ""  # The short X.Y version.
release = ""  # The full version, including alpha/beta/rc tags.

copyright = f'{year}, {org_name}'
author = "phi ARCHITECT"

# Base URL for the website, required for generating feeds.
# e.g. blog_baseurl = "http://example.com/"
blog_baseurl = f'https://{org}.github.io'
html_base_url = blog_baseurl
html_baseurl = blog_baseurl

blog_authors = {
    "phi": ("phi ARCHITECT", None),
}

html_theme_options = {
    'logo': 'logo.png',
    'logo_name': True,
    'github_user': org,
    'github_button': True,
}

