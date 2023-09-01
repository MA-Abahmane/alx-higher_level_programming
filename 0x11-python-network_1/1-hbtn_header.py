#!/usr/bin/python3
"""
    A Python script that takes in a URL, sends a request
    to the URL and displays the value of the X-Request-Id
    variable found in the header of the response
"""

from sys import argv
from urllib.request import urlopen, Request


if __name__ == "__main__":
    """ sends a request to the URL and displays the value of X-Request-Id """

    url = argv[1]

    req = Request(url)

    with urlopen(req) as response:
        details = response.info()

        print(details['X-Request-Id'])
