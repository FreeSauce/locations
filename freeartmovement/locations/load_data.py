import os
from django.contrib.gis.utils import LayerMapping

from .models import State


state_mapping = {
    'statefp' : 'STATEFP',
    'statens' : 'STATENS',
    'affgeoid' : 'AFFGEOID',
    'geoid' : 'GEOID',
    'stusps' : 'STUSPS',
    'name' : 'NAME',
    'lsad' : 'LSAD',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'geom' : 'MULTIPOLYGON',
}

state_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/states.shp'))

def run(verbose=True):
	ours = LayerMapping(State, state_shp, state_mapping, transform=True)
	ours.save(strict=True, verbose=verbose)