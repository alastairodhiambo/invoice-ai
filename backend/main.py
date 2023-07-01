from fastapi import FastAPI, UploadFile

from invoice import extract_invoice

app = FastAPI()


@app.get("/")
def read_root():
    return {"Sanity": "Check"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    data = extract_invoice(file.file)
    return {"data": data}
