#!/usr/bin/python3
"""
    A Python script that takes in a URL, sends a request
    to the URL and displays the value of the variable
    X-Request-Id in the response header
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    """ fetches https://alx-intranet.hbtn.io/status """

    url = argv[1]

    response = req.get(url)

    print(response.text)
