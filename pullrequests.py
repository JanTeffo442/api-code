import requests, json
from requests.auth import HTTPBasicAuth
import os
from os import environ

BASE_URL = 'https://api.github.com'
GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME')
GITHUB_PASSWORD = os.environ.get('GITHUB_PASSWORD')

def prs_between_two_dates(repo_owner:str, repo_name:str, start_date:str, end_date:str):

    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls'
    response = requests.get(url, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_PASSWORD))
    print(response.status_code)
    recent_pulls = response.json()
    return recent_pulls


if __name__ == '__main__':

    print(prs_between_two_dates('Umuzi-org','Jan-Teffo-190-rabbitmq',
    	'2020-02-28T08:30:42Z', '2020-07-20T08:30:50Z'))


