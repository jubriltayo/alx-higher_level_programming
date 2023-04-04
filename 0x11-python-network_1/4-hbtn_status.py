#!/usr/bin/python3
"""
This script fetches `https://alx-intranet.hbtn.io/status`
"""
import requests


url = 'https://alx-intranet.hbtn.io/status'
r = requests.get(url)

print("Body response:")
print(f"\t- type: {type(r.text)}")
print(f"\t- content: {r.text}")
