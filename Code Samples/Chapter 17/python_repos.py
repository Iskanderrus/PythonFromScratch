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
response_dict = r.json()

# Process results
print(response_dict.keys())
