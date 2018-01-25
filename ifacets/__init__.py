import os
import sys

root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(root, 'vendor/facets/facets_overview/python'))

from ifacets import IFacets
