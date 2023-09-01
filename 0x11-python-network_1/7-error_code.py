#!/usr/bin/python3
"""
    A Python script that takes in a URL, sends a request
    to the URL and displays the body of the response.
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    """ fetches https://alx-intranet.hbtn.io/status """

    url = argv[1]
    email = argv[2]

    try:
        response = req.get(url)

        print(response.text)

    except response.status_code >= 400:
        print(f"Error code: {response.status_code}")
