import json
import mitmproxy
from mitmproxy import http


# rewrite功能


class AD:
    def request(self, flow):
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["name"] = "WuSunny_rewrite"
            data["data"]["items"][0]["quote"]["current"] = "50.12"
            data["data"]["items"][0]["quote"]["percent"] = "-1.09"
            flow.response.text = json.dumps(data)


addons = [
    AD()
]
