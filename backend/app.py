from dotenv.main import load_dotenv
from utils import get_vendor_name, parse_data, parse_annotations, construct_prompt
import base64
import cohere
import glob
import os
from PIL import Image
import pytesseract

load_dotenv()

api_key = os.environ.get("COHERE_API_KEY")
co = cohere.Client(api_key)

dir = "test_set"
test_pdf_dir = os.path.join(dir, "pdf")
test_image_dir = os.path.join(dir, "images")
test_invoices = glob.glob(os.path.join(test_pdf_dir, "*"))
test_invoices.sort()

test_image_paths = glob.glob(os.path.join(test_image_dir, "*"))
test_image_paths.sort()


def extract_invoice(idx):
    # Get template name by running image classification
    template = get_vendor_name(test_image_paths[idx])

    # Collect raw text, annotation of training data
    texts = parse_data(template)
    annotations = parse_annotations(template)

    # Collect all fields to extract
    fields = annotations[0].keys()

    # # Collect raw text of the document to predict
    test_text = pytesseract.image_to_string(Image.open(test_image_paths[idx]))

    prompt = construct_prompt(texts, annotations, fields, test_text)
    response = co.generate(
        model="command",
        prompt=prompt,
        max_tokens=400,
    )
    text = response.generations[0].text
    print(text)


# TODO: Change number corresponding to test_set/image file index to see results
extract_invoice(0)
