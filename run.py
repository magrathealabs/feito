import os

from feito.github import API
from feito import Prospector
from feito import Messages
from feito import Repository

GITHUB_PR_ID = os.getenv('GITHUB_PR_ID')
REPO_USERNAME = os.getenv('REPO_USERNAME')
TOKEN = os.getenv('TOKEN')

repo = Repository()

# TODO: Transform this into a cli
def run():
    analysis = Prospector(repo).run()
    messages = Messages(analysis).commit_format()
    if messages == []:
        return
    for message in messages:
        send_commit_message(message)

def send_commit_message(message):
    api = API(REPO_USERNAME, repo.repo_name, token=TOKEN)

    response = api.create_comment_commit(
        body=message['message'],
        commit_id=repo.last_commit_id,
        path=message['file'],
        position=message['line'],
        pr_id=GITHUB_PR_ID,
    )

    return response

if __name__ == '__main__':
    run()
