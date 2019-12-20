#!/usr/bin/env python
# encoding: utf-8
"""
Effective proxys. Website: http://www.xicidaili.com/nn
Authors: idKevin
Date: 20170717
"""

import urllib2
import time
import random
import xiciProxys           # import user-defined package
import socket
import re


def testProxys(proxys):
    """ Test the proxys. """
    validProxys = []
    Url = "http://ip.chinaz.com/getip.aspx"
    for proxy in proxys:
        try:
            # set proxy
            proxy_handler = urllib2.ProxyHandler({'http':proxy, 'https':proxy})
            opener = urllib2.build_opener(proxy_handler)
            urllib2.install_opener(opener)
            # request website
            response = urllib2.urlopen(Url, timeout=5).read()

            # set filtration condition according website
            if re.findall('{ip:.*?,address:..*?}', response) != []: # remove invalid proxy
                validProxys.append(proxy)
                print "%s\t%s" % (proxy, response)
        except Exception as e:
            # print "%s\t%s" % (proxy, "invalid")
            continue

    return validProxys