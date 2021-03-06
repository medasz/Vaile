#!/usr/bin/env python3
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


from core.methods.tor import session
import time
import re
import socket
import core.lib.mechanize as mechanize
import http.cookiejar
from urllib.parse import urlencode
from re import search
from core.Core.colors import *
from core.variables import tor
br = mechanize.Browser()

# Cookie Jar
cj = http.cookiejar.LWPCookieJar()
br.set_cookiejar(cj)

torproxies = {'http':'socks5h://localhost:9050', 'https':'socks5h://localhost:9050'}
if tor:
    br.set_proxies(torproxies)

# Browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [
    ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

info = "Server Detection module."
searchinfo = "Server Detection module"
properties = {}

def serverdetect(web):
    requests = session()
    #print(R+'\n   ===========================')
    #print(R+'    D E T E C T   S E R V E R')
    #print(R+'   ===========================\n')
    from core.methods.print import posintact
    posintact("detect server") 
    time.sleep(0.4)
    print(GR+' [*] Checking server status...')
    web = web.replace('https://','')
    web = web.replace('http://','')
    try:
        ip_addr = socket.gethostbyname(web)
        print(G+' [+] Server detected online...'+C+color.TR2+C)
        time.sleep(0.5)
        print(O+' [+] Server IP :>'+C+color.TR3+C+G+ip_addr+C+color.TR2+C)
    except:
        print(R+' [-] Server seems down...')

    print(GR+' [*] Trying to identify backend...')
    time.sleep(0.4)
    web = 'http://' + web
    try:
        r = requests.get(web)
        header = r.headers['Server']
        if 'cloudflare' in header:
            print(C+' [+] The website is behind Cloudflare.')
            print(G+' [+] Server : Cloudflare'+C+color.TR2+C)
            time.sleep(0.4)
            print(O+' [+] Use the "Cloudflare" VulnLysis module to try bypassing Clouflare...'+C)

        else:
            print(G+' [+] Server : '+header+C+color.TR2+C)
        try:
            print(O+' [+] Running On :'+C+color.TR3+C+G+ r.headers['X-Powered-By']+C+color.TR2+C)
        except:
            pass
    except:
        print(R+' [-] Failed to identify server. Some error occured!')
        pass

# ===============================================================#
# THIS HAS BEEN MIGRATED TO THE VULNERABILITY ENUMERATION MODULE
# ===============================================================#

#def bypass(domain):

#    print GR+' [*] Trying to get real IP...'
 #   post = urlencode({'cfS': domain})
  #  result = br.open(
#       'http://www.crimeflare.info/cgi-bin/cfsearch.cgi ', post).read()
#
 #   match = search(r' \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', result)
  #  if match:
   #     bypass.ip_addr = match.group().split(' ')[1][:-1]
#       print G+' [+] Cloudflare found misconfigured!'
#       time.sleep(0.4)
#       print GR+' [*] Identifying IP...'
#       time.sleep(0.5)
 #       print G+' [+] Real IP Address : ' + bypass.ip_addr + '\n'
  #  else:
#       print R+' [-] Cloudflare properly configured...'
#       print R+' [-] Unable to find remote IP!\n'
#       pass
#

def attack(web):
    serverdetect(web)