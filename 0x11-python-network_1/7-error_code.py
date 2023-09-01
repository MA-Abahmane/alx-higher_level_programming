#!/usr/bin/python3
"""
    A Python script that takes in a URL, sends a request
    to the URL and displays the body of the response.
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    """ sends a request to the URL """

    url = argv[1]

    response = req.get(url)

    if (response.status_code >= 400):
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
