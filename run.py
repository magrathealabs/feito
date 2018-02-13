import os

from feito.github import API
from feito import Prospector
from feito import Messages
from feito import Repository

GITHUB_PR_ID = os.environ['GITHUB_PR_ID']
USER_MESSAGE = os.environ['USER_MESSAGE']
TOKEN = os.environ['TOKEN']
repo = Repository()

# TODO: Transform this into a cli
def run():
    analysis = Prospector(repo).run()
    messages = Messages(analysis).commit_format()
    if messages == []:
        return
    for message in messages:
        print(send_commit_message(message).json())

def send_commit_message(message):
    api = API(USER_MESSAGE, repo.repo_name, token=TOKEN)
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
