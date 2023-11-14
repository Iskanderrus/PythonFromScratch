import requests
from pathlib import Path
import plotly.express as px

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
repo_names, stars = [], []
print(f"Repositories returned: {len(repo_dicts)}")

print('\nSelected information about each repository: ')
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

fig = px.bar(x=repo_names,
             y=stars,
             hover_data=[repo_names, stars],
             color=stars,
             #text_auto=True,
             labels={'y':'Number of Stars', 'x': 'Repositories'},
             title='Top Python Repositories in GitHub')

fig.update_traces(hovertemplate=None)
fig.update_layout(hovermode="x",
                  title_font_size=28,
                  xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.write_html('top_python_repos_in_github.html')
