#!/usr/bin/python3
"""
    A Python script that takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user with the
    letter as a parameter.
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    """ POST request to http://0.0.0.0:5000/search_user with the letter as a parameter. """

    url = 'http://0.0.0.0:5000/search_user'

    if (len(argv) == 2):
        letter = {"q": argv[1]}
    else:
        letter = {"q": ""}

    response = req.post(url, data=letter)

    # Check if the response body is properly JSON formatted and not empty
    if response.headers.get('content-type') == 'application/json' and response.json():
        # Display the id and name; [<id>] <name>
        data = response.json()
        id_ = data.get('id')
        name_ = data.get('name')

        print(f"[{id_}] {name_}")
    # Display No result if the JSON is empty
    elif response.headers.get('content-type') == 'application/json':
        print("JSON is empty")
    # Display Not a valid JSON if the JSON is invalid
    else:
        print("Not a valid JSON")
