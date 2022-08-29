import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    def __init__(self) -> None:
        super().__init__()

    MONGO_URI = os.environ.get('MONGO_URI')

    HARVARD_MUSEUM_API_KEY = os.environ.get('HARVARD_MUSEUM_API_KEY')
        