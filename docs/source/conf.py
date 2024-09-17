import sphinx_rtd_theme
import codecs
import sys
import os

source_encoding = 'utf-8-sig'

def decode_file(file_path):
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'ascii']
    for enc in encodings:
        try:
            with codecs.open(file_path, 'r', encoding=enc) as f:
                content = f.read()
            return content
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Unable to decode {file_path} with any of the attempted encodings")

def source_read_handler(app, docname, source):
    file_path = app.env.doc2path(docname)
    source[0] = decode_file(file_path)

def setup(app):
    app.connect('source-read', source_read_handler)

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
    'sphinx_tabs.tabs',
    'sphinxcontrib.images'
]

images_config = {
    'override_image_directive': True,
    'default_image_width': '50%',
    'default_group': 'default'
}

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'prev_next_buttons_location': 'both',
    'sticky_navigation': True
}
html_static_path = ['_static']
html_output_dir = '_build/html'

# -- Options for EPUB output
epub_show_urls = 'footnote'
