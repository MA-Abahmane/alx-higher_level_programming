#!/usr/bin/python3
"""
    A Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to
    display your id
"""

from sys import argv
import requests as req
from requests.auth import HTTPBasicAuth as auth


if __name__ == "__main__":
    """ Takes GitHub credentials & uses the GitHub API to display your id """

    user = argv[1]
    token = argv[2]

    authentication = auth(user, token)

    response = req.get("https://api.github.com/user", auth=authentication)

    id_ = response.json().get('id')

    print(id_)