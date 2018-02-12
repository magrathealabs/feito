import os
import json

from git import Repo
import subprocess


class Repository:

    def __init__(self):
        self.repo = Repo(os.getcwd())
        self.repo_name = self.__repo_name()
        self.last_commit_id = self.__commit_id()

    def __repo_name(self):
        return self.repo.working_dir.split('/')[-1]

    def __commit_id(self):
        return self.repo.head.commit.hexsha
