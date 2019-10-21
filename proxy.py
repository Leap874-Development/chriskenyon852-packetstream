import requests
http_proxy = "http://ugotstyle88:xLTdAXKh595RkvF0_country-UnitedStates@proxy.packetstream.io:31112"
https_proxy = "http://ugotstyle88:xLTdAXKh595RkvF0_country-UnitedStates@proxy.packetstream.io:31112"
url = "https://ifconfig.co/json"

proxyDict = {
    "http" : http_proxy,
    "https" : https_proxy,
}

r = requests.get(url, proxies=proxyDict)
print(r.text)