# -*- coding: utf-8 -*-
import random

from lib import MONGO_DATABASE_PLACES
from logger import project_logger


def update_weights_in_mongo():
    project_logger.info('schedule run: undate_weights_in_mongo')
    for i in MONGO_DATABASE_PLACES.find({}):
        shop_id = i['shop_id']
        MONGO_DATABASE_PLACES.update({'shop_id': shop_id}, {'$set': {'weights': random.random() * 100}})


if __name__ == '__main__':
    update_weights_in_mongo()