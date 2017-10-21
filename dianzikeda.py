#-*- coding: UTF-8 -*- 

'''
用于模拟登陆电子科大信息门户

引入常规的urllib包   cookielib用于设置cookie    beautifulsoup

'''
import cookielib
import urllib2
import urllib
from bs4 import BeautifulSoup

#获取网页随机动态码
def clt(url):
    response = urllib2.urlopen(url)
    data = response.read()
    soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
    ##print(data.decode())
    link = soup.find_all('input')
    aa = link[2]
    aa=str(aa)
    return aa[38:-3]

try:
    #构造request
    cj = cookielib.CookieJar()
    pro = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(pro)
    urllib2.install_opener(opener)
    
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3637.220 Safari/537.36'
    header = {'User-Agent': user_agent}
    
    un = raw_input('信息门户的用户名:')
    pw = raw_input('信息门户的密码:')
    postdata = urllib.urlencode({
        'username': un,
        'password': pw,
        'lt': clt('http://idas.uestc.edu.cn/authserver/login'),
        'dllt': 'userNamePasswordLogin',
        'execution': 'e1s1',
        '_eventId': 'submit',
        'rmShown': '1'
    })
    
    url = 'http://idas.uestc.edu.cn/authserver/login?service=http%3A%2F%2Fportal.uestc.edu.cn%2F'
    req = urllib2.Request(url, data = postdata, headers=header)
    
    #第一次用于登陆   第二次带着cookie打开页面
    html =  opener.open(req)
    
    html = opener.open('http://eams.uestc.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR')
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

print html.read()
