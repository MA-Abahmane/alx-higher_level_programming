#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request as request


if __name__ == "__main__":
    """ fetches https://alx-intranet.hbtn.io/status """

    url = 'https://alx-intranet.hbtn.io/status'

    with request.urlopen(url) as response:
        details = response.read()
        print(details)
