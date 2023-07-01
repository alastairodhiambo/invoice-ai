import cohere
import base64
import os
import glob

from dotenv.main import load_dotenv

load_dotenv()

api_key = os.environ.get("COHERE_API_KEY")

# test_pdf_dir = os.path.join("test_set, pdf")
# test_image_dir = os.path.join("test_set", "images")

# test_invoices = glob.glob(os.path.join(test_pdf_dir, "*"))
# test_invoices.sort()

# test_image_list = []
# test_image_paths = []

# test_invoices = glob.glob(os.path.join(test_pdf_dir, "*"))
# test_invoices.sort()


# for test_invoice in test_invoices:
#     base_name = os.path.basename(test_invoice)
#     file_name = base_name.split(".")[0]

#     # Convert first page of uploaded pdf to image
#     image_path = os.path.join(test_image_dir, f"{file_name}.jpg")
#     with open(image_path, "rb") as f:
#         image_content = f.read()
#         encoded = base64.b64encode(image_content).decode()
#         test_image_list.append(f"data:image/jpeg;base64,{encoded}")
#     test_image_paths.append(image_path)
