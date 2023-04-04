#!/usr/bin/python3
"""
This script fetches from `https://alx-intranet.hbtn.io/status`
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as f:
        html = f.read()
        encoding = html.decode("utf-8")
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {encoding}")