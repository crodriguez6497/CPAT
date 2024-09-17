import sphinx_rtd_theme

project = 'C-PAT'
copyright = '2024 U.S. Federal Government (in countries where recognized)'
author = 'Christian Rodriguez'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.todo',
    'myst_parser',    
    'sphinx_tabs.tabs'
]

images_config = {
    'override_image_directive': True,
    'default_image_width': '50%',
    'default_group': 'default'
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'prev_next_buttons_location': 'both',
    'sticky_navigation': True
}
html_static_path = ['_static']


# -- Options for EPUB output
epub_show_urls = 'footnote'
