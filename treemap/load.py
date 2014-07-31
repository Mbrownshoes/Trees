import os 
from django.contrib.gis.utils import LayerMapping
from .models import Trees

trees_mapping = {
    'address_po' : 'ADDRESS_PO',
    'address_fu' : 'ADDRESS_FU',
    'objectid' : 'OBJECTID',
    'struct_id' : 'STRUCT_ID',
    'common_nam' : 'COMMON_NAM',
    'botanical_field' : 'BOTANICAL_',
    'diameter_b' : 'DIAMETER_B',
    'tree_posit' : 'TREE_POSIT',
    'geom' : 'MULTIPOINT',
}

tree_shp = os.path.abspath('../street_tree_data_wgs84/street_tree_general_data_wgs84.shp')

def run(verbose=True):
    lm = LayerMapping(Trees, tree_shp, trees_mapping, transform=False)

    lm.save(strict=True, verbose=verbose)