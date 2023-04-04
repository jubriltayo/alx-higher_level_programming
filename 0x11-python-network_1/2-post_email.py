#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    param = {'email': argv[2]}

    data = parse.urlencode(param).encode('ascii')
    r = request.Request(argv[1], data)
    with request.urlopen(r) as response:
        print(response.read().decode("utf-8"))
