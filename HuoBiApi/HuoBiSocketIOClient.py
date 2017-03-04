"""
火币SocketIO(websocket)协议接口API：
"""
import logging
import json
import warnings
from time import time
from socketIO_client import SocketIO
from db_util import DBUtils

warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
VALID_PERIOD = {
    "1min", "5min", "15min", "30min", "60min",
    "1day", "1week", "1mon", "1year",
}
VALID_PERCENT = {10, 20, 50, 80, 100}


class WSClient(object):
    """
    Example 1:
    client = WSClient()
    client.subscribe(req_params={
        "msgType": "reqMsgSubscribe",
        "symbolList": {
            "marketDepthTopShort": [
                {"symbolId": "btccny", "pushType": "pushLong"}
            ]
        }
    })
    """

    def __init__(self):
        self._io = SocketIO("hq.huobi.com", 80)
        self.req_data = {
            "version": 1,  # 终端版本
            "requestIndex": 100  # 请求序列号，方便判断多个请求的先后顺序，终端发送的数据，服务端会返回相同的数据
        }

    def _encapsulate_dict(self, dict_params):
        temp_dict = dict()
        if "version" in dict_params: temp_dict["version"] = dict_params["version"]
        if "requestIndex" in dict_params: temp_dict["requestIndex"] = dict_params["requestIndex"]
        return temp_dict

    def _list_2_str(self, lst):
        return ' '.join(list(map(str, lst)))

    def subscribe(self, req_params):  # 推送消息注册
        """
        reqMsgSubscribe该接口提供推送消息注册：
            消息以交易代码加上消息类型为基本单元。消息可以注册多次，以最后一次注册为准。
        """
        try:
            temp_dict = self._encapsulate_dict(req_params)
            temp_dict["msgType"] = "reqMsgSubscribe"  # 消息类型
            # 需要推送的交易代码列表。一个或者多个交易编码。每一个推送请求包括“交易代码，消息类型，推送策略”
            temp_dict["symbolList"] = req_params["symbolList"]
            self.req_data.update(temp_dict)
        except Exception as e:
            logger.error('missing keyword parameter.', e)
        else:
            self._client_run()

    def req_market_depth(self, on_msg, req_params):
        try:
            temp_dict = self._encapsulate_dict(req_params)
            temp_dict["msgType"] = req_params["msgType"]  # 消息类型
            temp_dict["symbolId"] = req_params["symbolId"]  # 交易代码列表
            if not on_msg.endswith('Top'):  # 获取行情深度
                if req_params["percent"] not in VALID_PERCENT:
                    raise ValueError('wrong percent parameter.')
                temp_dict["percent"] = req_params["percent"]  # 行情深度百分比
            self.req_data.update(temp_dict)
        except ValueError as e:
            logger.error('Invalid value setting:', e)
        except Exception as e:
            logger.error('missing keyword parameter.', e)
        else:
            self._client_run()

    def _on_connect(self):
        logger.info("connect")
        self._io.emit("request", self.req_data)  # send request message

    def _on_reconnect(self):
        logger.info("reconnected")

    def _on_disconnect(self):
        logger.info("disconnected")

    def _on_message(self, data):
        logger.info("fully information of the return message:")
        # for k, v in data.items():
        #     logger.info("\t\t%s: %s" % (k, v))
        raw_data = data['payload']
        msgType = data['msgType']
        # with open('record.txt', 'a', encoding='utf-8') as f:
        #     f.write(json.dumps(raw_data) + '\n')
        record = dict()
        if msgType == 'marketDetail':
            record.update(
                {
                    "totalVolume": raw_data["totalVolume"],
                    "turnoverRate": raw_data["turnoverRate"],
                    "level": raw_data["level"],
                    "commissionRatio": raw_data["commissionRatio"],
                    "innerDisc": raw_data["innerDisc"],
                    "volumeRatio": raw_data["volumeRatio"],
                    "turnVolume": raw_data["turnVolume"],
                    "priceLast": raw_data["priceLast"],
                    "symbolId": raw_data["symbolId"],
                    "priceOpen": raw_data["priceOpen"],
                    "updownRatio": raw_data["updownRatio"],
                    "outerDisc": raw_data["outerDisc"],
                    "priceHigh": raw_data["priceHigh"],
                    "updownVolume": raw_data["updownVolume"],
                    "amount": raw_data["amount"],
                    "priceNew": raw_data["priceNew"],
                    "priceLow": raw_data["priceLow"],
                    "poor": raw_data["poor"],
                    "totalAmount": raw_data["totalAmount"],
                    "priceAverage": raw_data["priceAverage"],
                    "trades": json.dumps(raw_data["trades"]),
                    "asks": json.dumps(raw_data["asks"]),
                    "bids": json.dumps(raw_data["bids"])
                }
            )
        elif msgType == 'tradeDetail':
            record.update(
                {
                    "tradeId": self._list_2_str(raw_data["tradeId"]),
                    "topAsks": json.dumps(raw_data["topAsks"]),
                    "amount": self._list_2_str(raw_data["amount"]),
                    "time": self._list_2_str(raw_data["time"]),
                    "price": self._list_2_str(raw_data["price"]),
                    "topBids": json.dumps(raw_data["topBids"]),
                    "symbolId": raw_data["symbolId"],
                    "direction": self._list_2_str(raw_data["direction"]),
                }
            )
        elif msgType == 'marketDepthTopShort':
            record.update({
                'version': raw_data['version'], 'symbolId': raw_data['symbolId'],
                'askPrice': self._list_2_str(raw_data['askPrice']),
                'askAmount': self._list_2_str(raw_data['askAmount']),
                'bidPrice': self._list_2_str(raw_data['bidPrice']),
                'bidAmount': self._list_2_str(raw_data['bidAmount'])
            })
        elif msgType == 'marketDepthTopDiff':
            record.update({
                'version': raw_data['version'], 'symbolId': raw_data['symbolId'],
                'versionOld': raw_data['versionOld'],
                'askDelete': self._list_2_str(raw_data['askDelete']),
                'bidDelete': self._list_2_str(raw_data['bidDelete']),
                'bidInsert': json.dumps(raw_data["bidInsert"]),
                'askInsert': json.dumps(raw_data["askInsert"]),
                'askUpdate': json.dumps(raw_data["askUpdate"]),
                'bidUpdate': json.dumps(raw_data["bidUpdate"])
            })
        elif msgType == 'marketOverview':
            record.update({
                'symbolId': raw_data['symbolId'],
                'priceNew': raw_data['priceNew'],
                'totalAmount': raw_data['totalAmount'],
                'totalVolume': raw_data['totalVolume'],
                'priceOpen': raw_data['priceOpen'],
                'priceHigh': raw_data['priceHigh'],
                'priceBid': raw_data['priceBid'],
                'priceAsk': raw_data['priceAsk'],
                'priceLow': raw_data['priceLow']
            })
        elif msgType == 'lastKLine':
            record.update({
                'symbolId': raw_data['symbolId'],
                'time': int(raw_data['time']),
                'isTemp': int(raw_data['isTemp']) if 'isTemp' in raw_data else None,
                'priceOpen': int(raw_data['priceOpen']),
                'priceLow': raw_data['priceLow'],
                'volume': raw_data['volume'],
                'priceLast': raw_data['priceLast'],
                'priceHigh': raw_data['priceHigh'],
                'amount': raw_data['amount'],
                'period': raw_data['period'],
                'count': int(raw_data['count']),
            })
        elif msgType == 'lastTimeLine':
            record.update({
                'symbolId': raw_data['symbolId'],
                'time': int(raw_data['time']),
                'isTemp': int(raw_data['isTemp']) if 'isTemp' in raw_data else None,
                'amount': int(raw_data['amount']),
                'priceLast': raw_data['priceLast'],
                'volume': raw_data['volume'],
                'count': raw_data['count'],
            })

        DBUtils.save_record(tableName=msgType, record=record)

    def _on_request(self, data):
        logger.info("fully information of the return message(requested):")
        for k, v in data.items():
            logger.info("\t\t%s: %s" % (k, v))

    def _on_error(self, ex):
        logger.error('error: %s' % ex)

    def _client_run(self):
        self._io.on("connect", self._on_connect)
        self._io.on("reconnect", self._on_reconnect)
        self._io.on("message", self._on_message)
        self._io.on("request", self._on_request)
        self._io.on("error", self._on_error)
        self._io.on("disconnect", self._on_disconnect)
        self._io.wait()  # waiting for push server.


'''
if __name__ == "__main__":
    logger.info('Beginning (current time): %d' % int(time() * 1000))
    client = WSClient()
    client.subscribe(req_params={  # 推送消息注册
        "msgType": "reqMsgSubscribe",
        "symbolList": {
            # {消息名称:[{"symbolId":数组,"pushType":数组,"period":k线周期数组,"percent":深度百分比数组}]}
            # 可选时间线单位："1min", "5min", "15min", "30min", "60min", "1day", "1week", "1mon", "1year",
            "marketDepthTopShort": [
                {"symbolId": "btccny", "pushType": "pushLong"}
            ]
        }
    })
    logger.info('Ending (current time): %d' % int(time() * 1000))
    # duplicated code
    # Demo1：reqMarketDepthTop（客户端获取实时行情服务器历史数据 相应的top行情深度 默认150条）
    # client = WSClient()
    # client.req_market_depth(on_msg="reqMarketDepthTop",
    #                         req_params={"msgType": "reqMarketDepthTop", "symbolId": "btccny"})

    # Demo2：reqMarketDepth（客户端获取实时行情服务器历史数据 相应的行情深度）
    # client.req_market_depth(on_msg="reqMarketDepth",
    #                         req_params={"msgType": "reqMarketDepthTop", "symbolId": "btccny", "percent": 10})
'''
