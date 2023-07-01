from fastapi import FastAPI, UploadFile

from invoice import extract_invoice
from to_csv import json_to_csv

app = FastAPI()


@app.get("/")
def read_root():
    return {"Sanity": "Check"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    data = extract_invoice(file.file).replace('\n', '').replace("'", '"')
    json_to_csv(data)

    return {"data": data}
