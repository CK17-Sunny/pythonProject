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
            currents = [0, -10.22, 5000]
            percents = [0.002, -0.99, 1000]
            for i in range(len(percents)):
                data["data"]["items"][i]["quote"]["percent"] = percents[i]
            for x in range(len(currents)):
                data["data"]["items"][x]["quote"]["current"] = currents[x]
            flow.response.text = json.dumps(data)


addons = [
    AD()
]
