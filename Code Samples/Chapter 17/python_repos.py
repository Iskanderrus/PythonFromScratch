import requests
from pathlib import Path

# Making an API call and checking the response
token_path = Path('../../../../Documents/github_token.txt')
token = token_path.read_text().strip()


url = "https://api.github.com/search/repositories"
python_request = "?q=language:python+sort:stars+stars:>10000"

python_api_request = url + python_request

headers = {'Authorization': 'token ' + token,
           "Accept": "application/vnd.github+json"}

r = requests.get(url=python_api_request, headers=headers)
print(f"Status: {r.status_code}")

# Convert the response object to a dictionary
response_dicts = r.json()
print(f"Total repositories: {response_dicts['total_count']}")
print(f"Complete results: {not response_dicts['incomplete_results']}")

# Explore information about the repositories
repo_dicts = response_dicts['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Ecamine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)