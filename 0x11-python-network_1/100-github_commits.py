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

    # Constructing the GitHub API URL
    url = f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits"

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

    except Exception:
        pass
