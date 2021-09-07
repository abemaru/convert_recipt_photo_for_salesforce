import glob
from src.convert_heic_to_jpeg import converter

HEIC_files = glob.glob('./pictures/input/*.HEIC')

converter()