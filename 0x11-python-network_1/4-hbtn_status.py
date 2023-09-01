#!/usr/bin/python3
"""
    A Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests as req


if __name__ == "__main__":
    """ fetches https://alx-intranet.hbtn.io/status """

    url = 'https://alx-intranet.hbtn.io/status'

    response = req.get(url)

    print('Body response:')
    print(f'\t- type: {type(response.text)}\n\t- content: {response.text}')
