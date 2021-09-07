import glob
from src.convert_heic_to_jpeg import converter
import logging
import re

logger = logging.getLogger(__name__)

all_files = glob.glob('./pictures/input/*')
HEIC_files = [ file for file in all_files if re.search('/*\.(HEIC|heic)', file)]


for i in HEIC_files:
    logger.info(i)
    print(i)
    converter(i)