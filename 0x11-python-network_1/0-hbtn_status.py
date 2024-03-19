#!/usr/bin/python3
'''A script that fetches status from a http'''
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    data = response.read()
    print(data)
