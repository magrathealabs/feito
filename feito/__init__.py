import os

from feito.github import API
from feito.prospector import Prospector
from feito.messages import Messages
from feito.repository import Repository


PULL_REQUEST_ID = os.getenv('PULL_REQUEST_ID')
REPOSITORY_USERNAME = os.getenv('REPOSITORY_USERNAME')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
REPOSITORY_NAME = os.getenv('REPOSITORY_NAME')


def run():
    repository = Repository(REPOSITORY_NAME)
    analysis_list = Prospector(repository).run()
    messages = Messages(analysis_list).commit_format()
    api = API(REPOSITORY_USERNAME, repository.repo_name, token=OAUTH_TOKEN)
    for message in messages:
        print(api.create_comment_commit(
            body=message['message'],
            commit_id=repository.last_commit_id,
            path=message['file'],
            position=message['line'],
            pr_id=PULL_REQUEST_ID,
        ))
