# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../../OpenTAKServer'))

project = 'OpenTAKServer'
copyright = '2025, Brian Wallen'
author = 'Brian Wallen'
release = '1.6.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_copybutton', 'sphinxcontrib.lightbox2', 'sphinxext.opengraph', 'sphinx.ext.autosectionlabel',
              'sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.coverage', 'sphinx.ext.autosummary', 'sphinxcontrib.autohttp.flask',
              'sphinx_sqlalchemy',]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

ogp_site_url = "https://docs.opentakserver.io"
ogp_site_name = "OpenTAKServer Docs"
ogp_image = "https://docs.opentakserver.io/_static/ots_logo.png"
ogp_custom_meta_tags = ["<meta property=\"og:logo\" content=\"https://docs.opentakserver.io/_static/ots_logo.png\" />"]

numpydoc_show_class_members = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = '_static/ots_logo.png'
html_favicon = '_static/favicon.png'
html_theme_options = {
    'analytics_id': 'G-22JB0TDCSP',
    'canonical_url': 'docs.opentakserver.io',
    'logo_only': True,
    'style_external_links': True,
    'github_url': 'https://github.com/brian7704/OpenTAKServer-docs',
}
