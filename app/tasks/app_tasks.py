from pydantic import EmailStr

from app.config import settings
from app.tasks.conf_cel import celery_app
from PIL import Image
from pathlib import Path

from app.tasks.email_templates import create_booking_confirm_template
import smtplib


@celery_app.task
def process_picture(path: str):
    image_path = Path(path)
    img = Image.open(image_path)
    big_resized_img = img.resize((1000, 500))
    small_resized_img = img.resize((200, 100))
    big_resized_img.save(f'app/static/images/big_resized_img_{image_path.name}')
    small_resized_img.save(f'app/static/images/small_resized_img_{image_path.name}')


@celery_app.task
def send_booking_confirm_email(booking: dict, email_to: EmailStr):
    # email_to_mock = settings.SMTP_USER
    msg_content = create_booking_confirm_template(booking, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
