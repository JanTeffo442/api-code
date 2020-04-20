import requests
from datetime import date

pull_requests = requests.get("https://api.github.com/repos/Umuzi-org/tech-department/pulls?id=1")

print(pull_requests.json())

def pull_requests(owner, repo_name, start_date, end_date):
  pull_requests = requests.get(f"https://api.github.com/repos/{owner}/{repo_name}/pulls?id=1")
  return pull_requests

print(dir(pull_requests("Umuzi-org","tech-department",18-3-2020,18-4-2020)))

x = {
  "id" : 1,
  'created_at':2019-2-4,
  'updated_at': 2020-4-27,
  'pushed_at': 2020-4-21,

}


f_date = date(2020, 3, 18)
l_date = date(2020, 4, 18)
pull_requests = l_date - f_date
print(pull_requests.days)