from sphinx_ifelse.utils import tags2dict

# -- General configuration ------------------------------------------------

# General information about the project.
project = 'Test Project'

# -- General configuration
extensions = [
   'sphinx_ifelse',
]

# -- extension configuration: ifelse
ifelse_variants = {
   'l1': 3,
   'l2': 3,
   'l3': 3,
}
