#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status
"""

from urllib.request import urlopen, Request


if __name__ == "__main__":
    """ fetches https://alx-intranet.hbtn.io/status """

    url = 'https://alx-intranet.hbtn.io/status'

    with urlopen(url) as response:
        details = response.read()
        print('Body response:')
        print(f'\t- type: {type(details)}\n\t- content: {details}\n\t- utf8 content: {details.decode("utf-8")}')
