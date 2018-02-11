import sys
import os

from git import Repo

from feito.github import API
from feito import prospector
from feito import Messages
from feito import Repository


GITHUB_PR_ID = os.environ['GITHUB_PR_ID']
USER_MESSAGE = os.environ['AUTHOR_MESSAGE']
TOKEN = os.environ['TOKEN']

# TODO: Transform this into a cli
def run():
    analysis = prospector.run()
    messages = Messages(analysis).format()
    for message in messages:
        send_commit_message(message)

def send_commit_message(message):
    repo = Repository()
    api = API(USER_MESSAGE, repo.repo_name, token=TOKEN)
    response = api.create_comment_commit(
        body=message['message'],
        commit_id=repo.commit_id,
        path=message['file'],
        position=message['position'],
        pr_id=GITHUB_PR_ID,
    )

    return response

if __name__ == '__main__':
    run()
