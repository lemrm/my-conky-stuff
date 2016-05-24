#!/usr/bin/env python
#-*-coding: utf-8-*-

import urllib2
import re

def get_wan_ip():
    site = urllib2.urlopen("http://checkip.dyndns.org/").read()
    grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
    address = grab[0]
    return address

if __name__ == '__main__':
    print( get_wan_ip() )
