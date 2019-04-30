import requests
import json
import os

namespace = "avattathil"
path = "users"
#root_path = "/orgs/aws-quickstart"
git_branch = "master"
git_api = "https://api.github.com/{}/{}/repos".format(path,namespace)
git_raw = "https://raw.githubusercontent.com/{}".format(namespace)
pkg_cfg = "ci/taskcat.yml"

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

#print(_response)
repo_data = []

while 'next' in _response.links.keys():
    _response=requests.get(_response.links['next']['url'])
#    print (type(_response.json()))
    repo_data.append(_response.json())

for repos in repo_data:
  for repo in repos:
    print(repo['name'])

for repos in repo_data:
  for repo in repos:
    repo_name = repo['name']
    print ("{}/{}/{}/{}".format(git_raw,repo_name,git_branch,pkg_cfg))
    is_pkg = requests.get('{}/{}/{}/{}'.format(git_raw,repo_name,git_branch,pkg_cfg))
    if is_pkg.status_code == 200:
        print('{}\t\t\t[{}]'.format(repo_name , 'PACKAGE_ENABLED'))
    else:
        print('{}\t\t\t[{}]'.format(repo_name , 'PACKAGE_DISABLED'))
