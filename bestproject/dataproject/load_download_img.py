from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from pathlib import Path

import io
import os

from PIL import Image

CLIENT_SECRET_FILE = 'web6project.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = service_account.Credentials.from_service_account_file(
    CLIENT_SECRET_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=service)

folder_id = '1RdYoVP5lycHHNtraHrOPz9KkFoagOLIz'

DOWNLOAD_DIR = Path('static/img/')


def download_user_image(path, name):
    file_metadata = {'name': f'{name}', 'parents': [f'{folder_id}']}
    media = MediaFileUpload(path, mimetype='image/jpg')
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    return file.get('id')


def load_user_image(img_id):
    file = service.files().get(fileId=img_id).execute()
    file_extension = os.path.splitext(file.get('name'))
    print(file_extension)

    file_content = service.files().get_media(fileId=img_id).execute()
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    file_name = os.path.join(DOWNLOAD_DIR, file.get('name'))
    with io.BytesIO(file_content) as f:
        with Image.open(f) as img:
            img.save(file_name)

    return True


if __name__ == '__main__':
    img_name_in_google_disk = 'bird.jpg'  # Назва картинки яка юуде на гугл диску
    upload_name_img = 'птах.jpg'  # Назва картинки яка у користувача

    download_path = DOWNLOAD_DIR / upload_name_img  # Тут повинна бути дерикторія користувача до картинки включно
    # з назвою картинки и розширенням картинки

    img_id_ = download_user_image(download_path, img_name_in_google_disk)  # Загрузка картинки на диск: приймає повний
    # локальний шлях до картинки користувача, та нову назву картинки яка буде на диску, повертає id картинки з диску
    print(img_id_)
    get_imd = load_user_image(img_id_)  # Загрузка картинки з гугл диска, приймає id картинки на диску, повертає зображення
    print(get_imd)