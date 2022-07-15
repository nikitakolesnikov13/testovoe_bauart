import shutil
from pathlib import Path

from fastapi import FastAPI, UploadFile
from core.settings import Settings
import uuid
from pydantic import UUID4
import minio
from core.helpers import prepare_data_to_query


settings = Settings()
app = FastAPI(title="File to Table converter service")



@app.post("/import_file/")
async def import_file(file: UploadFile):
    if file.content_type == "text/csv":
        contents = await file.read()
        prepare_data_to_query(file)
        return {"file_ID": UUID4, "import_status": ""}
    else:
        print("все плохо")



@app.post("/groupData")
async def groupData():
    return "group_status"


@app.get("/dropFile")
async def dropFile():
    return "delete_status"

