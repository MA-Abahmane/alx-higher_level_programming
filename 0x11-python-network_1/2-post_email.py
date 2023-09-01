#!/usr/bin/python3
"""
    A Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the
    email as a parameter, and displays the body of
    the response (decoded in utf-8)
"""

from sys import argv
import urllib.request as request
import urllib.parse as parse


if __name__ == "__main__":
    """ displays the value of the X-Request-Id variable """

    url = argv[1]
    dic = {'email': argv[2]}

    # Encode data
    data = parse.urlencode(dic).encode('utf-8')
    # Create POST request
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        details = response.read()
        print(details.decode('utf-8'))
