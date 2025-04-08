# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import date

project = 'B6x Docs'
copyright = "2003-%d, XIAOMAN" % date.today().year
author = 'XIAOMAN-AI'
release = ''

# -- General configuration ---------------------------------------------------
# The master toctree document.
master_doc = 'index'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst']

extensions = [
    'sphinx.ext.autosectionlabel',
]

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_favicon = "./_images/xm_favicon.ico"
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_images']
html_show_sphinx = False
html_title = ''
# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%Y-%m-%d"
