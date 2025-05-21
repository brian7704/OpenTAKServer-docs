# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenTAKServer'
copyright = '2025, Brian Wallen'
author = 'Brian Wallen'
release = '1.4.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_copybutton']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

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