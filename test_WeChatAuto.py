import requests


def get_token():
    user_id = "ww3773845c7d04052c"
    user_token = "MSprjNCDrydpqEnTh86komqQXgUs1wnd3fpl1nhthUw"
    r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={user_id}&corpsecret={user_token}")
    return r.json()["access_token"]


class TestContact:
    def setup(self):
        self.token = get_token()

    def test_add(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "test_automation",
            "name": "testName13",
            "mobile": "+86 13800000000",
            "department": [1],
            "gender": "1"
        }
        r = requests.post(url, json=data)
        print(r.json())

    def test_update(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "test_automation",
            "mobile": "13300000000",
            "gender": "2"
        }
        r = requests.post(url, json=data)
        print(r.json())

    def test_delete(self):
        user_id = "test_automation"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}"
        r = requests.get(url)
        print(r.json())

    def test_search(self):
        user_id = "test_automation"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}"
        r = requests.get(url)
        print(r.json())
