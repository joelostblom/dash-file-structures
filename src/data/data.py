# Instead of reading in the data separately in components.py and callbacks.py
# we can read it in once in data.py and import it into the other files.
# Python modules are only loaded once, so the data will only be read in once.
from vega_datasets import data


cars = data.cars()
