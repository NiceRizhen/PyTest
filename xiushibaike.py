#-*- coding: UTF-8 -*- 

import urllib2
import re

baseUrl = 'https://www.qiushibaike.com/'

ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3637.220 Safari/537.36'
header = {'User-Agent' : ua}

try:
    request = urllib2.Request(baseUrl, headers = header)
    html = urllib2.urlopen(request)
    
    content = html.read().decode('utf-8')
    removetag = re.compile('<.*?>')
    removetag2 = re.compile('[.*?]')
    partten = re.compile(r'<div class="content"(.*?)<span>(.*?)</span>', re.S)
    item = re.findall(partten, content)
    for i in item:
        aa = re.sub(removetag, "", i[1]).strip() + '\n'
        print aa
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason