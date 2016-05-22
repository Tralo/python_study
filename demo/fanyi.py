#!/usr/bin/env python
# coding=utf-8
import urllib.request
import urllib.parse
import json
content = input("想要翻译的英文: ")
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionm:Zrom=http://www.youdao.com/"
data = {}
data["type"] = "AUTO"
data["i"] = content
data["doctype"] = "json"
data["xmlVersion"] = "fanyi.web"
data["ue"] = "UTF-8"
data["action"] = "FY_BY_CLICKBUTTON"
data["typoResult"] = "true"
data = urllib.parse.urlencode(data).encode("utf-8")
response = urllib.request.urlopen(url,data)
html = response.read().decode("utf-8")
AAA = json.loads(html)
print("翻译的结果是: " + AAA["translateResult"][0][0]["tgt"])
