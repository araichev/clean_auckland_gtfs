import os
import sys
from pathlib import Path 

sys.path.insert(0, os.path.abspath('..'))

import clean_auckland_gtfs


DATA_DIR = Path('tests/data')