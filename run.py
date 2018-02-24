import os

from git import Repo

from feito.github import API
from feito import Prospector
from feito import Messages
from feito import Repository


PULL_REQUEST_ID = os.getenv('PULL_REQUEST_ID')
USERNAME = os.getenv('USERNAME')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
REPOSITORY_NAME = os.getenv('REPOSITORY_NAME') or Repo(os.getcwd())


repository = Repository(REPOSITORY_NAME)

# TODO: Transform this into a cli
def run():
    analysis = Prospector(repository).run()
    messages = Messages(analysis).commit_format()
    for message in messages:
        send_commit_message(message)

def send_commit_message(message):
    api = API(USERNAME, repository.repo_name, token=OAUTH_TOKEN)

    response = api.create_comment_commit(
        body=message['message'],
        commit_id=repository.last_commit_id,
        path=message['file'],
        position=message['line'],
        pr_id=PULL_REQUEST_ID,
    )

    return response

if __name__ == '__main__':
    run()
