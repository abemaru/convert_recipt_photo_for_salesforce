import pyheif
from PIL import Image


def converter(heif_path):
    jpg_path = heif_path.replace('input', 'output').replace('HEIC', 'jpg').replace('heic', 'jpg')

    heif_image = pyheif.read(heif_path)

    jpg_image = Image.frombytes(
        heif_image.mode, 
        heif_image.size, 
        heif_image.data,
        "raw",
        heif_image.mode,
        heif_image.stride,
    )

    jpg_image.save(jpg_path, "JPEG")