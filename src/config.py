# -*- coding: utf-8 -*-

import logging
from os import path
from copy import deepcopy

from ndict import ndict


PROJECT_PATH = path.dirname(path.dirname(path.abspath(__file__)))

CONFIG = ndict()
CONFIG.NAME = 'DEFAULT_CONFIG'
CONFIG.DEBUG = True
CONFIG.TESTING = False

CONFIG.LOGGER = ndict()
CONFIG.LOGGER.FORMAT = '%(asctime)s %(filename)s[%(lineno)d] %(name)s: %(message)s'
CONFIG.LOGGER.LEVEL = logging.DEBUG
CONFIG.LOGGER.OUTPUT_DIR = path.join(PROJECT_PATH, 'output')

CONFIG.SQLALCHEMY = ndict()
CONFIG.SQLALCHEMY.URL = r'sqlite:///%s' % path.join(PROJECT_PATH, 'magnolia.sqlite')

CONFIG.MYSQL = ndict()
CONFIG.MYSQL.HOST = '115.28.143.67'
CONFIG.MYSQL.PORT = 3306
CONFIG.MYSQL.USER = 'fd'
CONFIG.MYSQL.PASSWORD = '111111'
CONFIG.MYSQL.DATABASE = 'fddb'

CONFIG.MONGO = ndict()
CONFIG.MONGO.HOST = '115.28.143.67'
CONFIG.MONGO.PORT = 27017

CONFIG.YUNPIAN = ndict()
CONFIG.YUNPIAN.APIKEY = 'cf6905108b06464f106017c3efe12e52'
CONFIG.YUNPIAN.COMPANY = u'喵喵熊'

CONFIG.FANSMESSAGECONFIG = ndict()
CONFIG.FANSMESSAGECONFIG.CURRENT_P2P_COUNT = 30
CONFIG.FANSMESSAGECONFIG.P2P_REMAIN_COUNT = 30
CONFIG.FANSMESSAGECONFIG.NEXT_P2P_COUNT = 30
CONFIG.FANSMESSAGECONFIG.CURRENT_MASS_COUNT = 10
CONFIG.FANSMESSAGECONFIG.MASS_REMAIN_COUNT = 10
CONFIG.FANSMESSAGECONFIG.NEXT_MASS_COUNT = 10

CONFIG.OSS_PREFIX = 'http://img.immbear.com/'

DEVELOPMENT_CONFIG = deepcopy(CONFIG)
DEVELOPMENT_CONFIG.NAME = 'DEVELOPMENT_CONFIG'

TESTINGCONFIG = deepcopy(CONFIG)
TESTINGCONFIG.NAME = 'TESTINGCONFIG'
TESTINGCONFIG.TESTING = True

PRODUCTIONCONFIG = deepcopy(CONFIG)
PRODUCTIONCONFIG.Name = 'PRODUCTIONCONFIG'
PRODUCTIONCONFIG.DEBUG = False
PRODUCTIONCONFIG.LOGGER.LEVEL = logging.INFO

PRODUCTIONCONFIG.MYSQL.HOST = 'localhost'
PRODUCTIONCONFIG.MYSQL.PORT = 3306
PRODUCTIONCONFIG.MYSQL.USER = 'fd'
PRODUCTIONCONFIG.MYSQL.PASSWORD = 'bEijingyinpu_2015'
PRODUCTIONCONFIG.MYSQL.DATABASE = 'fddb'

PRODUCTIONCONFIG.MONGO.HOST = 'mongodb://shopaddress:shopaddress123@112.124.115.140:27017/shop_address'
PRODUCTIONCONFIG.MONGO.PORT = 27017

CONFIG = CONFIG