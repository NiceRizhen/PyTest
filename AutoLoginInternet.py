#-*- coding: UTF-8 -*- 
import urllib
import urllib2
import time
from __builtin__ import raw_input

loginUrl = 'http://192.168.9.8/srun_portal_pc.php?ac_id=1&'


if __name__ == '__main__':
    name =raw_input(unicode('输入用户名：','utf-8').encode('gbk'))
    word = raw_input(unicode('输入密码：','utf-8').encode('gbk'))

    postdata = {
        'action' : 'login',
        'username' : name,
        'password' : word,
        'ac_id' : '1',
        'user_mac' : '',
        'user_ip' : '',
        'nas_ip' : '',
        'save_me' : '0',
        'domain' : '@uestc',
        'ajax' : '1'
        }

    postdata = urllib.urlencode(postdata)

    req = urllib2.Request(loginUrl, postdata)
    while True:
        html = urllib2.urlopen(req).read()
        print html
        if 'login_ok' in html:
            break;
        
        time.sleep(0.1)
        
