#!/usr/bin/python3
"""
script to send post request to passed url with email and display
body as response
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    response = requests.post(url, data=data)

    print(response.text)
