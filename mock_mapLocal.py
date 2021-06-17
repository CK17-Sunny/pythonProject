import json
from mitmproxy import http


class mock_mapLocal:
    def request(self, flow: http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            with open("C:/Users/lenovo/PycharmProjects/pythonProject3/xueqiu.json", encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(200,  # (optional) status code
                                                       f.read(),  # (optional) content
                                                       {"Content-Type": "text/html"}  # (optional) headers
                                                       )

    def response(self, flow: http.HTTPFlow):
        pass


addons = [
    mock_mapLocal()
]
