import requests

proxy = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888",
}

r = requests.get("https://ceshiren.com/search/query?term=aaa", proxies=proxy, verify=False)
print(r.text)
