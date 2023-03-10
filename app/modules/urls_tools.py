from typing import Union

# Base imports
import string
import random

# Modules imports
from app import db
from config import Config
from app.modules.models import Url, EmptyUrl


def get_all() -> list:
    """Function to get all urls objects"""

    try:
        return Url.query.all()
    except:
        return []


def get_url(url_id: int) -> Union[Url, EmptyUrl]:
    """Function to get url by id"""

    url = Url.quety.get(url_id)

    if url:
        return url
    return EmptyUrl


def get_url_by_short_url(short_url: str) -> Union[Url, EmptyUrl]:
    """Function to get url by short url"""

    url = Url.query.filter_by(short_url=short_url).first()
    if url:
        return url
    return EmptyUrl


def add_url(url: str) -> Union[Url, EmptyUrl]:
    """Function to add url to db"""

    letters = string.digits + string.ascii_letters
    rand_string = ''.join(random.choice(letters) for i in range(Config.SHORT_URL_LENGTH))

    url_obj = Url(url=url, short_url=rand_string)
    try:
        db.session.add(url_obj)
        db.session.commit()
        return url_obj
    except:
        return EmptyUrl


def delete_url(url_id: int) -> bool:
    """Function to delete url"""

    try:
        db.session.delete(get_url(url_id))
        db.session.commit()
        return True
    except:
        return False
