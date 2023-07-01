from PIL import Image
import pytesseract
import glob
import os
import sys

dir = sys.argv[1]  # TODO: Handle when user forgets to input

image_dir = os.path.join(dir, "images")
image_paths = glob.glob(os.path.join(image_dir, "*"))
image_paths.sort()


for image in image_paths:
    text = pytesseract.image_to_string(Image.open(image))
    base = os.path.basename(image)[:-4]
    file_path = os.path.join(dir, "text", base + '.txt')
    with open(file_path, "w") as file:
        file.write(text)
