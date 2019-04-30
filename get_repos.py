import requests
import json
import os

#git_api = "https://api.github.com/orgs/aws-quickstart/repos"
git_api = "https://api.github.com/users/avattathil/repos"

git_token_file='/Users/circlev/.gittoken'

if os.path.isfile(git_token_file):
  print('Using Auth')
  gtoken = open(git_token_file,'r').read().splitlines()

  headers ={
      "Authorization": 'access token {}'.format(gtoken)
  }
  _response=requests.get(git_api,headers=headers)
else:
  print('No Auth')
  _response = requests.get(git_api)

print(_response)
repo_data = []
while 'next' in _response.links.keys():
    _response=requests.get(_response.links['next']['url'])
    print (type(_response.json()))
    repo_data.append(_response.json())

print(repo_data)

#for repos in repo_data:
#    for repo in repos:
#       print(repo['name'])

