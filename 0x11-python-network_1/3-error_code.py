#!/usr/bin/python3
"""
    A Python script that takes in a URL, sends a request
    to the URL and displays the body of the response
    (decoded in utf-8).
"""

from sys import argv
import urllib.request as request
import urllib.error


if __name__ == "__main__":
    """ sends a request to the URL """

    url = argv[1]

    try:
        with request.urlopen(url) as response:
            details = response.read().decode('utf-8')
            print(details)

    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
