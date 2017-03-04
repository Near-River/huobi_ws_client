#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

import pymysql
import pymysql.cursors


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
            if tableName == 'marketDetail':
                sql = "INSERT INTO `marketDetail` (`totalVolume`, `turnoverRate`, `commissionRatio`, `innerDisc`, `level`, `volumeRatio`, `turnVolume`, `priceLast`, `priceOpen`, `updownRatio`, `outerDisc`, `priceHigh`, `updownVolume`, `amount`, `totalAmount`, `priceNew`, `priceLow`, `poor`, `priceAverage`, `symbolId`, `trades`, `asks`, `bids`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql,
                               (
                                   record['totalVolume'], record['turnoverRate'], record['commissionRatio'],
                                   record['innerDisc'], record['level'], record['volumeRatio'],
                                   record['turnVolume'], record['priceLast'], record['priceOpen'],
                                   record['updownRatio'], record['outerDisc'], record['priceHigh'],
                                   record['updownVolume'], record['amount'], record['totalAmount'],
                                   record['priceNew'], record['priceLow'], record['poor'],
                                   record['priceAverage'], record['symbolId'], record['trades'],
                                   record['asks'], record['bids']
                               )
                               )
            elif tableName == 'tradeDetail':
                sql = "INSERT INTO `tradeDetail` (`symbolId`, `tradeId`, `amount`, `time`, `price`, `direction`, `topBids`, `topAsks`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql,
                               (
                                   record['symbolId'], record['tradeId'], record['amount'], record['time'],
                                   record['price'], record['direction'], record['topBids'], record['topAsks']
                               )
                               )
            elif tableName == 'marketDepthTopShort':
                sql = "INSERT INTO `marketDepthTopShort` (`version`, `symbolId`, `askPrice`, `askAmount`, `bidPrice`, `bidAmount`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql,
                               (
                                   record['version'], record['symbolId'], record['askPrice'], record['askAmount'],
                                   record['bidPrice'], record['bidAmount']
                               )
                               )
            elif tableName == 'marketDepthTopDiff':
                sql = "INSERT INTO `marketDepthTopDiff` (`version`, `symbolId`, `versionOld`, `askDelete`, `bidDelete`, `askInsert`, `bidInsert`, `askUpdate`, `bidUpdate`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql,
                               (
                                   record['version'], record['symbolId'], record['versionOld'],
                                   record['askDelete'], record['bidDelete'], record['askInsert'],
                                   record['bidInsert'], record['askUpdate'], record['bidUpdate']
                               )
                               )
            elif tableName == 'marketOverview':
                sql = "INSERT INTO `marketOverview` (`symbolId`, `priceNew`, `totalAmount`, `totalVolume`, `priceOpen`, `priceHigh`, `priceBid`, `priceAsk`, `priceLow`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql,
                               (
                                   record['symbolId'], record['priceNew'], record['totalAmount'],
                                   record['totalVolume'], record['priceOpen'], record['priceHigh'],
                                   record['priceBid'], record['priceAsk'], record['priceLow']
                               )
                               )
            elif tableName == 'lastKLine':
                sql = "INSERT INTO `lastKLine` (`symbolId`, `time`, `isTemp`, `priceOpen`, `priceLow`, `volume`, `priceLast`, `priceHigh`, `amount`, `period`, `count`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql,
                               (
                                   record['symbolId'], record['time'], record['isTemp'],
                                   record['priceOpen'], record['priceLow'], record['amount'],
                                   record['priceLast'], record['priceHigh'], record['priceLow'],
                                   record['period'], record['count']
                               )
                               )
            elif tableName == 'lastTimeLine':
                sql = "INSERT INTO `lastTimeLine` (`symbolId`, `time`, `isTemp`, `amount`, `priceLast`, `volume`, `count`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql,
                               (
                                   record['symbolId'], record['time'], record['isTemp'],
                                   record['amount'], record['priceLast'], record['volume'],
                                   record['count']
                               )
                               )
        # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()
    except Exception as e:
        print(e)
        with open('error.log', 'a', encoding='utf-8') as f:
            f.write(json.dumps(record) + '\n')
    finally:
        connection.close()
