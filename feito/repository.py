import os
import json

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
        )
        return repo_name.stdout.decode()[:-1]

    @staticmethod
    def commit_id():
        repo = Repo(os.getcwd())
        return repo.head.commit.hexsha
