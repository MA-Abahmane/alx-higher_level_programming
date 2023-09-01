#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status
    The body of the response is displayed
"""

from urllib.request import urlopen, Request


if __name__ == "__main__":
    """ fetches https://alx-intranet.hbtn.io/status """

    req = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(req) as response:
        details = response.read()
        print('Body response:')
        print(f"\t- type: {type(details)}\n\t- content: {details}")
        print(f"\t- utf8 content: {details.decode('utf-8')}")
