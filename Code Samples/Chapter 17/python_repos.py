import requests
from pathlib import Path
import plotly.express as px

# Making an API call and checking the response
token_path = Path('../../../../Documents/github_token.txt')
token = token_path.read_text().strip()

language = input('What programming language are you interested in? ').strip().lower()

url = "https://api.github.com/search/repositories"
python_request = f"?q=language:{language}+sort:stars+stars:>10000"

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
repo_links, stars, hover_texts = [], [], []
print(f"Repositories returned: {len(repo_dicts)}")

print('\nSelected information about each repository: ')
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

fig = px.bar(x=repo_links,
             y=stars,
             hover_name=hover_texts,
             color=stars,
             color_continuous_scale=px.colors.sequential.Plasma,
             labels={'y': 'Number of Stars', 'x': 'Repositories'},
             title=f'Top {language.title()} Repositories in GitHub')

fig.update_traces(hovertemplate=None, marker_opacity=0.6)
fig.update_layout(title_font_size=28,
                  xaxis_title_font_size=20,
                  yaxis_title_font_size=20,
                  )
fig.show()
fig.write_html(f'top_{language}_repos_in_github.html')
