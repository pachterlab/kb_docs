# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'kallisto | bustools'
copyright = '2024, Pachter Lab'
author = 'Delaney K. Sullivan, Laura Luebbert'

release = '0.28.2'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
    'nbsphinx',
]

nbsphinx_execute = 'never' # Set to 'auto' if you want to execute notebooks

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
smartquotes = False
smartquotes_action = 'qe'
html_theme_options = {
    'navigation_depth': 3
}

# Add "View on Github" link
html_context = {
    "display_github": True,
    "github_user": "pachterlab",
    "github_repo": "kb_docs",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
