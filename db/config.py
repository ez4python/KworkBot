from os import getenv
from dotenv import load_dotenv

load_dotenv()

import psycopg2


class DB:
    config = {
        "DB_NAME": getenv('DB_NAME'),
        "DB_PORT": getenv('DB_PORT'),
        "DB_HOST": getenv('DB_HOST'),
        "DB_PASSWORD": getenv('DB_PASSWORD'),
        "DB_USER": getenv('DB_USER')
    }
    con = psycopg2.connect(**config)
    cur = con.cursor()

    def insert(self):
        pass

    def select(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass
