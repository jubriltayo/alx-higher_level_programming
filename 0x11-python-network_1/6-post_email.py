#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import requests
from sys import argv

if __name__ == "__main__":
    param = {'email': argv[2]}

    r = requests.post(argv[1], data=param)
    print(r.text)
