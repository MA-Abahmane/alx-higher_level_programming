#!/usr/bin/python3
"""
    A Python script that takes in a URL and an email
    address, sends a POST request to the passed URL
    with the email as a parameter, and finally
    displays the body of the response.
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    """ sends a POST request to the passed URL """

    url = argv[1]
    email = argv[2]

    response = req.post(url, data={"email": email})

    print(response.text)
