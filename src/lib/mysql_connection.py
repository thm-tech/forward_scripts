# -*- coding: utf-8 -*-
import MySQLdb
import DBUtils.PooledDB
import MySQLdb.cursors

from config import CONFIG
from logger import project_logger


mysql_config = {
    'host': CONFIG.MYSQL.HOST,
    'port': CONFIG.MYSQL.PORT,
    'user': CONFIG.MYSQL.USER,
    'passwd': CONFIG.MYSQL.PASSWORD,
    'db': CONFIG.MYSQL.DATABASE
}

pool = DBUtils.PooledDB.PooledDB(creator=MySQLdb, mincached=1, maxcached=100,
                                 use_unicode=False, charset='utf8', cursorclass=MySQLdb.cursors.DictCursor,
                                 **mysql_config)
project_logger.info('Connect Mysql Server Success...')

MYSQL_CONNECTION = lambda: pool.connection()


def fetchall(sql, params=None):
    conn = MYSQL_CONNECTION()
    cursor = conn.cursor()
    try:
        count = cursor.execute(sql, params) if params else cursor.execute(sql)
        result = cursor.fetchall() if count else []
    except MySQLdb.Error as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return result


def fetchone(sql, params=None):
    conn = MYSQL_CONNECTION()
    cursor = conn.cursor()
    try:
        count = cursor.execute(sql, params) if params else cursor.execute(sql)
        result = cursor.fetchone() if count else []
    except MySQLdb.Error as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return result


def fetchmany(sql, num, params=None):
    conn = MYSQL_CONNECTION()
    cursor = conn.cursor()
    try:
        count = cursor.execute(sql, params) if params else cursor.execute(sql)
        result = cursor.fetchmany(num) if count else []
    except MySQLdb.Error as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return result