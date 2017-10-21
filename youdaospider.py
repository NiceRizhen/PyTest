#-*- coding: UTF-8 -*- 

import urllib
import urllib2
import json

data = {}
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['i'] = '刘晓磊'
data['doctype'] = 'json'
data['client'] = 'fanyideskweb'
data['smartresult'] = 'dict'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

fanyiUrl = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
data = urllib.urlencode(data)

request = urllib2.Request(fanyiUrl, data)
html = urllib2.urlopen(request)


rst = html.read()
rst_dict = json.loads(rst)
print rst_dict['translateResult'][0][0]['tgt']

