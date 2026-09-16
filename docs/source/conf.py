# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'StrokeSeg2'
copyright = '2026, Empenn Research Team'
author = 'Empenn Research Team'

release = '2.0'
version = '2.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinxcontrib.bibtex",
    'myst_parser',   # 👈 enables Markdown support
]

# Allow both .rst and .md as source files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

# 👈 THIS IS THE NEW LINE FOR DOXYGEN
html_extra_path = ['doxygen_out'] 

# -- Options for EPUB output -------------------------------------------------

epub_show_urls = 'footnote'

# -- Options for LOGO -------------------------------------------------
# Add path to custom static files
html_static_path = ['_static']

# Set the logo (path is relative to _static/)
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"

bibtex_bibfiles = ["references.bib"]
bibtex_default_style = "plain"