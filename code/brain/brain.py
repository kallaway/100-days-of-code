from flask import Flask
import configparser
from github import Github
import simplejson as json


app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')
git = Github(config['GITHUB']['User'], config['GITHUB']['Password'])

@app.route('/')
def hello_world():
  return 'Hello World version2!'


@app.route('/brain/api/v1.0/logs')
def get_logs():
  for repo in git.get_user().get_repos():
    if repo.name in '100-days-of-code':
      for i in repo.get_commits():
        if i.author.name == config['GITHUB']['DisplayName']:
          for f in i.files:
            if 'log.md' == f.filename:
              print(f.raw_url)

  return 'See Logs'


if __name__ == '__main__':
  app.run(debug=True)
