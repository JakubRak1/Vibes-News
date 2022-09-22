import os
import secrets
from vibes import app


def save_picture(form_image) -> str:
    # Function that allow save provided in form_image image in local storage
    random_hex: str = secrets.token_hex(8)
    # Set variable random_hex as string of random created token
    _, f_ext = os.path.splitext(form_image.filename)
    picture_fn: str = random_hex + f_ext
    # Set picture_fn as sum of random_hex and file extension
    picture_path: str = os.path.join(app.root_path, 'static/pics', picture_fn)
    # Set picture_path as sum of app.root_path , 'static/pics' and picture_fn
    form_image.save(picture_path)
    return picture_fn
    # Saving picture on local storage and returns picture_fn