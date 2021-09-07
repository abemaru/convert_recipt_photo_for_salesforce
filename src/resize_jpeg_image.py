from PIL import Image
from pyheif.reader import HeifFile

def image_resizer(jpeg_path, ratio=2):
    img = Image.open(jpeg_path)
    
    width = img.width
    height = img.height

    resized_img = img.resize((width // ratio, height // 2), resample=Image.LANCZOS)
    resized_img.save(jpeg_path)