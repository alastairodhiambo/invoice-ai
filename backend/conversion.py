from pdf2image import convert_from_path

import glob
import os
import sys


#### To run this ####
# In the command line, provide the path from root
# to the parent directory of the pdf and image directories


dir = sys.argv[1] if len(sys.argv) > 1 else "test_set"

pdf_dir = os.path.join(dir, "pdf")
image_dir = os.path.join(dir, "images")

pdfs = glob.glob(os.path.join(pdf_dir, "*"))
pdfs.sort()


def convert_pdf_to_image(pdf_path, image_path):
    pages = convert_from_path(pdf_path)
    pages[0].save(image_path, 'JPEG')


for pdf in pdfs:
    base_name = os.path.basename(pdf)
    file_name = base_name.split(".")[0]

    # Convert first page of uploaded pdf to image
    image_path = os.path.join(image_dir, f"{file_name}.jpg")
    pdf_path = os.path.join(pdf_dir, f"{file_name}.pdf")
    convert_pdf_to_image(pdf_path, image_path)
