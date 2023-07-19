from app.tasks.conf_cel import celery_app
from PIL import Image
from pathlib import Path


@celery_app.task
def process_picture(path: str):
    image_path = Path(path)
    img = Image.open(image_path)
    big_resized_img = img.resize((1000, 500))
    small_resized_img = img.resize((200, 100))
    big_resized_img.save(f'app/static/images/big_resized_img_{image_path.name}')
    small_resized_img.save(f'app/static/images/small_resized_img_{image_path.name}')
