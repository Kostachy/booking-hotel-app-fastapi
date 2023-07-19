from fastapi import APIRouter, UploadFile
import shutil

from app.tasks.app_tasks import process_picture

router = APIRouter(
    prefix='/images',
    tags=['Загразку картинок']
)


@router.post('/hotels')
async def add_hotel_image(name: int, uploading_file: UploadFile):
    img_path = f'app/static/images/{name}.webp'
    with open(img_path, 'wb+') as file_obj:
        shutil.copyfileobj(uploading_file.file, file_obj)
    process_picture.delay(img_path)
