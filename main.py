import re
import glob
from src.convert_heic_to_jpeg import converter
from src.resize_jpeg_image import image_resizer

all_files = glob.glob('./pictures/input/*')
HEIC_files = [ file for file in all_files if re.search('/*\.(HEIC|heic)', file)]

jpeg_files = []

for file in HEIC_files:
    jpeg_files.append(converter(file))

for file in jpeg_files:
    image_resizer(file)
