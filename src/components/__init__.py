# Defining the imports in this file makes the import syntax cleaner
# Without this, the app.py file would have to import each component
# via from `components.small import title, etc`,
# but now we can use from `components import title, etc`.
# In other words, everything that's imported here
# is available in the components namespace/module.
from .general import title, sidebar, histogram, density  # noqa: F401
from .table import table  # noqa: F401
