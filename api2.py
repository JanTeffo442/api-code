import requests
from datetime import date

username = 'Umuzi-org'
repo = 'tech-department'


#Repository information with start created_at date and updated_at date
user_data = requests.get(f"https://api.github.com/users/{username}").json()
print(user_data)
print("\n")


#Getting number of contributors
all_contributors = list()
page_count = 1

while True:
    contributors = requests.get(f"https://api.github.com/repos/{username}/{repo}/contributors?page=%d"%page_count)
    if contributors != None and contributors.status_code == 200 and len(contributors.json()) > 0:
        all_contributors = all_contributors + contributors.json()
    else:
        break
    page_count = page_count + 1

count=len(all_contributors)
print(f"Number of contributors is : {count} \n")


#List all pull requests
pull_requests = requests.get(f"https://api.github.com/repos/{username}/{repo}/pulls?id=1")

print(pull_requests.json())

def pull_requests(owner, repo, start_date, end_date):
  pull_requests = requests.get(f"https://api.github.com/repos/{username}/{repo}/pulls?id=1")
  return pull_requests

print(dir(pull_requests("Umuzi-org","tech-department",1-1-2019,16-12-2020)))
print("\n")




