"""
Script to get actual data from GitHub and make comparison of the programming languages based on the repositories data
"""
import csv
import math

import requests
from pathlib import Path
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

data = []
all_languages_plotting_data = []

languages = [x.strip().lower() for x in input(
    'Enter programming languages to compare, separating by comma?\n').split(',')]

# Making an API call and checking the response
token_path = Path('../../../../Documents/github_token.txt')
token = token_path.read_text().strip()

for language in languages:
    my_dict = dict()
    url = f"https://api.github.com/search/repositories?q=language:{language}+sort:stars+stars:stars>1000"

    headers = {'Authorization': 'token ' + token,
               "Accept": "application/vnd.github+json"}

    r = requests.get(url=url, headers=headers)
    print(f"Status: {r.status_code}")

    # Convert the response object to a dictionary
    response_dicts = r.json()
    my_dict['language'] = language
    my_dict['repos_count'] = response_dicts['total_count']

    # Explore information about the repositories
    repo_dicts = response_dicts['items']
    repo_links, stars, hover_texts, watchers = [], [], [], []

    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])
        watchers.append(repo_dict['watchers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        hover_text = f"{owner}<br />{description}"
        hover_texts.append(hover_text)

    my_dict['stars_count'] = sum(stars)
    my_dict['watchers_count'] = sum(watchers)
    data.append(my_dict)
    all_languages_plotting_data.append([repo_links, stars])

    # try:
    #     fig = px.bar(x=repo_links,
    #                  y=stars,
    #                  hover_name=hover_texts,
    #                  color=stars,
    #                  color_continuous_scale=px.colors.sequential.Plasma,
    #                  labels={'y': 'Number of Stars', 'x': 'Repositories'},
    #                  title=f'Top {language.title()} Repositories in GitHub')
    #
    #     fig.update_traces(hovertemplate=None, marker_opacity=0.6)
    #     fig.update_layout(title_font_size=28,
    #                       xaxis_title_font_size=20,
    #                       yaxis_title_font_size=20,
    #                       )
    # except ValueError:
    #     print(f"Plot for {language} cannot be constructed.")
    # else:
    #     fig.show()
    #     fig.write_html(f'top_{language}_repos_in_github.html')

fig = make_subplots(rows=len(languages), cols=1, shared_yaxes=True)

for x in range(len(languages) + 1):
    try:
        fig.add_trace(go.Bar(x=all_languages_plotting_data[x][0], y=all_languages_plotting_data[x][1]))
    except:
        print('No data available.')

fig.update_layout(height=2500, title_text=f"Top Repositories for {', '.join(str(i).title() for i in languages)}")
fig.show()

with open('data/my_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)
print(data)
