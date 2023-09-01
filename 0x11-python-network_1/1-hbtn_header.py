#!/usr/bin/python3
"""
    A Python script that takes in a URL, sends a request
    to the URL and displays the value of the X-Request-Id
    variable found in the header of the response
"""

from sys import argv
import urllib.request as request


if __name__ == "__main__":
    """ displays the value of the X-Request-Id variable """

    url = argv[1]

    with request.urlopen(url) as response:
        if ("X-Request-Id" in response.header):
            print(response.header["X-Request-Id"])
