#!/usr/bin/python3
"""
    A Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API to
    display your id
"""

from sys import argv
import requests as req


if __name__ == "__main__":
    """ Takes GitHub credentials & uses the GitHub API to display your id """

    repo, user = argv[1], argv[2]

    # Constructing the GitHub API URL
    url = f"https://api.github.com/repos/{user}/{repo}/commits"

    # Send a GET request to the GitHub API
    request = req.get(url)

    # Parsing the JSON response
    commits = request.json()

    # Displaying commit information
    cmtNum = 10
    try:
        for idx in range(cmtNum):
            cmtCode = commits[idx].get('sha')
            usrName = commits[idx].get('commit').get('author').get('name')
            print(f"{cmtCode}: {usrName}")
    # pass on error
    except Exception:
        pass
