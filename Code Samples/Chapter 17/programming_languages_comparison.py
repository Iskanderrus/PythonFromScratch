"""
Script to get actual data from GitHub and make comparison of the programming languages based on the repositories data
"""
import csv
import math
from pathlib import Path

import plotly.graph_objects as go
import requests
from plotly.subplots import make_subplots

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

# Counter to control number of the languages on the list
counter = 0

# Building a figure for subplots
fig = make_subplots(
    rows=math.ceil(len(languages) / 2),
    cols=2,
    shared_yaxes='all',
    subplot_titles=[language.title() for language in languages]
)

# Building plots for each language
for row in range(1, math.ceil(len(languages) / 2) + 1):
    for col in range(1, 3):
        if all_languages_plotting_data:
            if all_languages_plotting_data[0][0]:
                fig.add_trace(go.Bar(
                    x=all_languages_plotting_data[0][0],
                    y=all_languages_plotting_data[0][1],
                    name=f'{languages[counter].title()}'),
                    row=row,
                    col=col)
            counter += 1

            all_languages_plotting_data.remove(all_languages_plotting_data[0])

fig.update_xaxes(tickangle=45)
fig.update_layout(legend_title_text="Programming Languages",
                  title_text=f"Top Repositories for {', '.join(str(i).title() for i in languages)}",
                  xaxis={'automargin': True},
                  yaxis={'automargin': True}
                  )
fig.show()

with open('data/my_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)

#TODO: Make a plot of data
def plotting_data(data):
    fig = make_subplots()

    for data_dict in data:
        for k, v in data_dict.items():
            fig.add_trace(go.Bar(
                x=k,
                y=v))
    fig.show()


plotting_data(data=data)
