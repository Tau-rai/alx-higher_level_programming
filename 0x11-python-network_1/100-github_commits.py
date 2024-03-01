#!/usr/bin/python3
"""
This module has a script that takes your Github credentials and
uses the Github API to display my id
"""


import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        repo_owner, repo_name
        )
    req = requests.get(url)
    commits = req.json()

    for commit in commits[:10]:
        print("{}: {}".format(
            commit.get('sha'), commit['commit']['author']['name'])
            )
