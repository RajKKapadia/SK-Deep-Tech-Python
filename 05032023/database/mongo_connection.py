import os
from datetime import datetime

from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

MONGODB_URL = os.getenv('MONGODB_URL')

client = MongoClient(MONGODB_URL)
database = client.PythonAPI
users = database.users


def create_mongo_user(user: dict) -> bool:

    user['create_at'] = datetime.now()
    user['is_deletd'] = False

    result = users.insert_one(user)
    return result.acknowledged


def get_mongo_user(email: str) -> None:

    result = users.find_one(
        {'email': email, 'is_deletd': False}, {'_id': False})

    return result

def update_mongo_user(email: str, update: dict) -> None:

    result = users.find_one_and_update(
        filter={
            'email': email
        },
        update={
            '$set': update
        }
    )

    return result