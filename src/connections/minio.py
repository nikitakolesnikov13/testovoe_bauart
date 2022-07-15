from minio import Minio
from minio.error import S3Error

class MinIOConnection:
    def __init__(self, settings):
        self.settings = settings

