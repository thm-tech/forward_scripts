# -*- coding: utf-8 -*-
import pymongo

from config import CONFIG
from logger import project_logger

client = pymongo.MongoClient(CONFIG.MONGO.HOST, CONFIG.MONGO.PORT)
project_logger.info('Connect Mongo Server Success...')
db = client.shop_address
places = db.places
places.create_index([('local', pymongo.GEOSPHERE)])

MONGO_DATABASE_PLACES = places