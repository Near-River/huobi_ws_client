#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
import json


def load_db_info():
    import os
    import json

    tempDir = os.path.abspath('.')
    if tempDir.endswith('db_util'):
        deployFilePath = os.path.join(os.path.abspath('../'), 'deploy.json')
    else:
        deployFilePath = os.path.join(tempDir, 'deploy.json')
    DB_Info = dict()
    with open(deployFilePath, encoding='utf-8') as f:
        DB_Info.update(json.load(f))
    return DB_Info


def get_connention():
    DB_Info = load_db_info()
    # Connect to the database
    connection = pymysql.connect(host=DB_Info['host'],
                                 user=DB_Info['user'],
                                 password=DB_Info['password'],
                                 db=DB_Info['database'],
                                 charset=DB_Info['charset'],
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def save_record(tableName, record):
    connection = get_connention()
    try:
        with connection.cursor() as cursor:
            # Insert a new record
            if tableName == 'marketDepthTopShort':
                sql = "INSERT INTO `marketDepthTopShort` (`version`, `symbolId`, `askPrice`, `askAmount`, `bidPrice`, `bidAmount`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (record['version'], record['symbolId'], record['askPrice'], record['askAmount'],
                                     record['bidPrice'], record['bidAmount']))
        # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()
    except Exception as e:
        with open('error.log', 'a', encoding='utf-8') as f:
            f.write(json.dumps(record) + '\n')
    finally:
        connection.close()
