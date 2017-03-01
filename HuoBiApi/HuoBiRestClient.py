"""
火币实时top行情获取：REST API 接口调用

指定深度数据条数（1-150条）
    [BTC-CNY] http://api.huobi.com/staticmarket/depth_btc_X.js
    [LTC-CNY] http://api.huobi.com/staticmarket/depth_ltc_X.js
    [BTC-USD] http://api.huobi.com/usdmarket/depth_btc_X.js

X表示返回多少条深度数据，可取值 1-150
"""

import logging
import json
import requests
from time import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

Headers = {
    "Host": "api.huobi.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,en-US;q=0.8,zh;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}


class RESTClient(object):
    global Headers

    def __init__(self):
        self.session = requests.session()
        self.session.headers.update(Headers)

    def req_market_depth(self, depth=20, currency='btc', market_type='undefined'):
        """
        :param depth: 20 default value
        :param currency: btc default value
        :param market_type: undefined default value
        :return:
        """
        data = None
        try:
            if market_type == 'undefined': market_type = 'staticmarket'
            if market_type != 'undefined' and market_type not in ['staticmarket', 'usdmarket']:
                raise NameError
            rest_api = 'http://api.huobi.com/{0}/depth_{1}_{2}.js'.format(market_type, currency, depth)
            while True:
                resp = self.session.get(rest_api)
                if resp.status_code == 200:
                    data = json.loads(resp.text)
                    logger.info("fully information of the return data:")
                    for k, v in data.items():
                        logger.info("\t\t%s: %s" % (k, v))
                    break
        except NameError as e:
            logger.error('Incorrect parameter value.', e)
        else:
            return data


'''
if __name__ == "__main__":
    # [BTC-CNY] http://api.huobi.com/staticmarket/depth_btc_X.js
    # [LTC-CNY] http://api.huobi.com/staticmarket/depth_ltc_X.js
    # [BTC-USD] http://api.huobi.com/usdmarket/depth_btc_X.js
    logger.info('Beginning (current time): %d' % int(time() * 1000))
    client = RESTClient()
    # market_type: 可选值(staticmarket  &  usdmarket)
    data = client.req_market_depth(currency='btc', depth=20, market_type='staticmarket')
    # 返回数据说明：卖:价格:累积量,...       买:价格:累积量...
    logger.info('Ending (current time): %d' % int(time() * 1000))
'''

