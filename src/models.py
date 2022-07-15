import uuid
from pydantic import BaseModel
from enum import Enum, auto


class File(BaseModel):
    minio_url: str
    id: uuid.UUID
    file_name: str


class Details:
    file_type: str = "не правильный формат файлаБ поддерживаются файлы типа .csv"
    file_size: str = "размер файла превышает лимит"


class FailureResponce(BaseModel):
    detail: Details