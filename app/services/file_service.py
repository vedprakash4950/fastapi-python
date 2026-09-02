import os
import uuid

from fastapi import UploadFile


class FileService:

    @staticmethod
    def save_vehicle_image(file: UploadFile) -> str:
        upload_dir = "uploads/vehicles"

        os.makedirs(upload_dir, exist_ok=True)

        extension = os.path.splitext(file.filename)[1]

        filename = f"{uuid.uuid4()}{extension}"

        file_path = os.path.join(upload_dir, filename)

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        return file_path