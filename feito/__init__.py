import os

from git import Repo

from feito.github import API
from feito.prospector import Prospector
from feito.messages import Messages
from feito.repository import Repository


PULL_REQUEST_ID = os.getenv('PULL_REQUEST_ID')
REPOSITORY_USERNAME = os.getenv('REPOSITORY_USERNAME')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
REPOSITORY_NAME = os.getenv('REPOSITORY_NAME') or Repo(os.getcwd())


def run():
    repository = Repository(REPOSITORY_NAME)
    analysis = Prospector(repository).run()
    messages = Messages(analysis).commit_format()
    for message in messages:
        api = API(REPOSITORY_USERNAME, repository.repo_name, token=OAUTH_TOKEN)
        api.create_comment_commit(
            body=message['message'],
            commit_id=repository.last_commit_id,
            path=message['file'],
            position=message['line'],
            pr_id=PULL_REQUEST_ID,
        )
