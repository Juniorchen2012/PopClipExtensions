#!/usr/bin/python  
#-*-coding:utf-8-*- 
import urllib2
import base64
import os
import time
from urllib import urlencode

tNumberOrName=os.getenv('POPCLIP_OPTION_TNUM')
transferPasswd=os.getenv('POPCLIP_OPTION_TPWD')
date=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
tContent = os.getenv('POPCLIP_TEXT')
param = '{"appID":"a5f2e17d63e46ee3321532d1982e4f0b","accessToken":"68376fe9ddedf51383158ac31252f183","tNumberOrName":"%s","transferPasswd":"%s","tContent":"%s"}'%(tNumberOrName,transferPasswd,tContent)
param_base64 = base64.b64encode(param)
data = {
    'time': date,
     'lang': 'en',
	'source':'2001',
	'param':param_base64
}
request = "http://t2u.me/t3/api/open/openTransfer?%s"%urlencode(data)
#print request
content = urllib2.urlopen(request).read()
#print param
#print content