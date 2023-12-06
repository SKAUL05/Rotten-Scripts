#!/usr/bin/env python3

#to convert it into a script by running sudo chmod +x all_github_repos.py

import requests
import sys
from github import Github
#imports
#pip3/pip install PyGithub is installed to work with the contents of the Github repositories

username = sys.argv[1]
#reading the username as a commandline argument

url = f"https://api.github.com/users/{username}"

user_data = requests.get(url).json()
#to retrieve data contained in the url in json format

def repository_names(user):
    return list(user.get_repos())
#fetching the names of all the repositories

def repository_details(user):
    all_repo_details = []
    repo_names = repository_names(user)
    for repo in repo_names:
        repo_details = {
            'Name': repo.full_name.split('/')[1],
            'Description': repo.description,
            'Created on': repo.created_at,
            'Programming language': repo.language,
            'Forked': f"{str(repo.forks)} time(s)",
        }
        all_repo_details.append(repo_details)
    return(all_repo_details)
#fetching the details of all the repositories

user = Github().get_user(username)

RD = repository_details(user)
#fetching the details of all repositories
#stored as a list of dictionaries

if __name__ == "__main__":
    for content in RD:
        #pprint.pprint(content)
        for title , description in content.items():
            print(title ,":" , description)
        print('\n-------------------------------------------------------------------------------------------------------------------\n')
