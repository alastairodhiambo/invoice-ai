from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from invoice import extract_invoice
from to_csv import json_to_csv
from text2code import get_coordinates


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Data(BaseModel):
    query: str


@app.get("/")
def read_root():
    return {"Sanity": "Check"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    data = extract_invoice(file.file).replace('\n', '').replace("'", '"')
    json_to_csv(data)

    return {"data": data}


@app.post("/process")
def post_text(data: Data):
    # Call the text2code function to process the input_text
    processed_result = get_coordinates(data.query)
    print(processed_result)
    return processed_result
