"""
订阅火币网实时数据信息，并将行情服务器推送信息保存到数据库中。
"""
import os, sys

sys.path.append(os.path.abspath('./HuoBiApi'))

from HuoBiApi.HuoBiSocketIOClient import WSClient
from HuoBiApi.HuoBiRestClient import RESTClient

if __name__ == '__main__':
    client = WSClient()
    client.subscribe(req_params={  # 推送消息注册
        "msgType": "reqMsgSubscribe",
        "symbolList": {
            # {消息名称:[{"symbolId":数组,"pushType":数组,"period":k线周期数组,"percent":深度百分比数组}]}
            # 可选时间线单位："1min", "5min", "15min", "30min", "60min", "1day", "1week", "1mon", "1year",
            "marketDetail": [
                {"symbolId": "btccny", "pushType": "pushLong"}
            ],
            # "tradeDetail": [
            #     {"symbolId": "btccny", "pushType": "pushLong"}
            # ],
            # "marketDepthTopShort": [
            #     {"symbolId": "btccny", "pushType": "pushLong"}
            # ],
            # "marketDepthTopDiff": [
            #     {"symbolId": "btccny", "pushType": "pushLong"}
            # ],
            # "marketOverview": [
            #     {"symbolId": "btccny", "pushType": "pushLong"}
            # ],
            # "lastKLine": [
            #     {"symbolId": "btccny", "pushType": "pushLong", "period": "1min"},
            #     {"symbolId": "btccny", "pushType": "pushLong", "period": "5min"},
            #     {"symbolId": "btccny", "pushType": "pushLong", "period": "15min"},
            #     {"symbolId": "btccny", "pushType": "pushLong", "period": "30min"},
            #     {"symbolId": "btccny", "pushType": "pushLong", "period": "60min"},
            #     {"symbolId": "btccny", "pushType": "pushLong", "period": "1day"},
            #     {"symbolId": "btccny", "pushType": "pushLong", "period": "1week"},
            #     {"symbolId": "btccny", "pushType": "pushLong", "period": "1mon"},
            #     {"symbolId": "btccny", "pushType": "pushLong", "period": "1year"}
            # ],
            # "lastTimeLine": [
            #     {"symbolId": "btccny", "pushType": "pushLong"},
            # ],
        }
    })

    # client = RESTClient()
    # data = client.req_market_depth(currency='btc', depth=20, market_type='staticmarket')
    # print(data)
