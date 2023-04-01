#!/usr/bin/python3
"""
script that takes in a url and an email, sends a POST request
to the url with the email as parameter and displays body of the
response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        page = response.read()

    print(page.decode())
