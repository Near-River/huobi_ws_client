"""
websocket 收集信息字段含义:
{"version": 1,
    "payload": {
        "version": 1487988746250,
        "bidName": "累计买单",
        "bidTotal": [3.08, 5.354, 5.7627, 6.3181, 6.3567, 8.9497, 8.9597, 10.1502, 11.1502, 11.4488, 11.8468, 19.2824, 20.4319, 20.5289, 20.7289, 22.3233, 24.5916, 24.6251, 24.9667, 25.0527],
        "bidPrice": [7807.33, 7807, 7806, 7805, 7803.08, 7803, 7800.72, 7800, 7791.73, 7791.3, 7791, 7790, 7786.9, 7786.02, 7786.01, 7786, 7785, 7781, 7780, 7778],
        "symbolId": "btccny",
        "askPrice": [7827.87, 7827.96, 7827.97, 7828, 7828.55, 7828.9, 7828.99, 7829, 7830, 7832, 7834.02, 7834.25, 7834.55, 7834.9, 7834.92, 7835, 7838, 7839.6, 7845.8, 7848],
        "bidAmount": [3.08, 2.274, 0.4087, 0.5554, 0.0386, 2.593, 0.01, 1.1905, 1, 0.2986, 0.398, 7.4356, 1.1495, 0.097, 0.2, 1.5944, 2.2683, 0.0335, 0.3416, 0.086],
        "askTotal": [1.5, 2, 8.9815, 11.7982, 12.0976, 13.4357, 27.0984, 27.5361, 31.4845, 31.9845, 31.9995, 32.0145, 32.0295, 36.735, 36.75, 63.7114, 64.7114, 65.2114, 67.2114, 68.2074],
        "askName": "累计卖单",
        "askAmount": [1.5, 0.5, 6.9815, 2.8167, 0.2994, 1.3381, 13.6627, 0.4377, 3.9484, 0.5, 0.015, 0.015, 0.015, 4.7055, 0.015, 26.9614, 1, 0.5, 2, 0.996]
        },
    "symbolId": "btccny",
    "msgType": "marketDepthTopShort"
}
symbolId	    btccny	    交易代码
bidName	    累计买单	 买单文字描述
bidPrice		            买单价格
bidTotal		            累计买单量
bidAmount		            买单量
askName	    累计卖单	卖单文字描述
askPrice		            卖单价格
askTotal		            累计卖单量
askAmount		            卖单量
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
            "marketDepthTopShort": [
                {"symbolId": "btccny", "pushType": "pushLong"}
            ]
        }
    })

    # client = RESTClient()
    # data = client.req_market_depth(currency='btc', depth=20, market_type='staticmarket')
    # print(data)
