from github import Github
import urllib3
import requests

from credentials import USERNAME
from credentials import PASSWORD


g = Github(USERNAME, PASSWORD)

repos = g.get_user().get_repos()

for repo in repos:
    print(repo.name)

