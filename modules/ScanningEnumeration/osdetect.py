#!/usr/bin/env python3
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import re
import socket
import http.cookiejar
import subprocess
import time
from re import search
from modules.ScanningEnumeration.getports import scan0x00, getports
from core.Core.colors import *
from modules.ScanningEnumeration.getcensys import getos0x00

info = "This module tries to find out the OS the target is using."
searchinfo = "OS Fingerprinter"
properties = {}

def port0x00(web):

    time.sleep(0.7)
    print(C+' [!] Moving on to the second phase...')
    time.sleep(0.8)
    print(C+' [*] Initiating port scan (TCP+UDP)...')

    try:
        getports(web)
    except Exception as e:
        print(R+' [-] Exception : '+str(e))
    print(GR+' [*] Initiating OS detection response analysis...')
    response = subprocess.check_output(['nmap','-Pn','-O','-sSU','-F','--osscan-guess','-T4', web])
    #print(1)
    if "No OS matches for host".lower() not in str(response.lower()):
        #print(2)
        if 'running:' in str(response.lower()):
            #print(3)
            regex = re.compile("Running:(.*)")
            result = regex.findall(str(response))
            print(C+' [+] OS Running Matched : '+B+result[0].strip())

        if 'os cpe:' in str(response.lower()):
            #print(4)
            regex = re.compile("OS CPE:(.*)")
            result = regex.findall(str(response))
            print(C+' [+] OS CPE Detected : '+B+result[0].strip())

        if 'os details:' in str(response.lower()):
            #print(5)
            regex = re.compile("OS details:(.*)")
            result = regex.findall(str(response))
            print(C+' [+] Operating System Details : '+B+result[0].strip())
        
        if "0 hosts up" in str(response.lower()):
            print(R+' [-] Target seems down...')
    else:
        print(R+' [-] No exact matches for OS via port scan...')

def osdetect(web):
    try:
        time.sleep(0.4)
        #print(R+'\n     ===================================')
        #print(R+'      O S   F I N G E R P R I N T I N G')
        #print(R+'     ===================================\n')
        from core.methods.print import pscan
        pscan("os fingerprinting")
        web = web.replace('http://','')
        web = web.replace('https://','')
        print(GR+' [*] Initialising Module [1]...')
        flag = getos0x00(web)
        print(C+'\n [+] Module [1] Completed!')
        if flag == 0x01:
            q = input(C+' [!] OS Identified!\n [?] Move on to to module [2]? (y/N) :> ')
            if q == 'Y'or q == 'y':
                print(GR+'\n [*] Initialising Module [2]...')
                port0x00(web)
            elif q == 'N' or q == 'n':
                print(C+' [+] Done!')
        elif flag == 0x00:
            print(GR+' [*] Initialising Module [2]...')
            port0x00(web)
        else:
            print(R+' [-] Fuck, something went wrong!')
            print(flag)

    except Exception as e:
        print(R+' [-] Unhandled Exception occured...')
        print(R+' [-] Exception : '+str(e))
    print(G+' [+] OS Fingerprinting Module Completed!'+C+color.TR2+C+'\n')

def attack(web):
    osdetect(web)