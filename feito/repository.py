from git import Repo
import subprocess


class Repository:

    def __init__(self):
        self.repo_name = self.repo_name()
        self.last_commit_id = self.commit_id()

    @staticmethod
    def repo_name():
        repo_name = subprocess.run(
          "basename `git rev-parse --show-toplevel`", shell=True, stdout=subprocess.PIPE
        ).stdout
        return json.dumps(repo_name)

    @staticmethod
    def commit_id():
        repo = Repo(os.getcwd())
        return repo.head.commit.hexsha
