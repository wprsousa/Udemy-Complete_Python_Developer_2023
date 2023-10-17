import sys
from pathlib import Path
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# check if new/ exists, if not create
new_directory = Path(str(output_folder))
if not new_directory.exists():
    new_directory.mkdir()
# loop through Pokedex
directory = Path(str(image_folder))
for img_jpg in directory.glob("*.jpg"):
    image_jpg = Image.open(img_jpg)
    path_png = new_directory / img_jpg.stem
    # convert images to png
    path_png = path_png.with_suffix(".png")
    # save to the new folder.
    image_jpg.save(path_png)
    print('Image converted')
