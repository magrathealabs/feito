import os
import json
import subprocess

from git import Repo

from feito import Filters


class Repository:

    def __init__(self):
        self.repo = Repo(os.getcwd())
        self.repo_name = self.__repo_name()
        self.last_commit_id = self.__commit_id()

    def __repo_name(self):
        return os.getenv('REPO_NAME') or self.repo.working_dir.split('/')[-1]

    def __commit_id(self):
        return os.getenv('COMMIT_ID') or self.repo.head.commit.hexsha

    def diff_files(self):
        arg_git_diff = 'git diff --name-only --diff-filter=ACMR master'
        diff_files = subprocess.run(arg_git_diff, stdout=subprocess.PIPE, shell=True)
        diff_list = diff_files.stdout.decode().split('\n')[:-1]

        filtered_python_files = Filters.filter_python_files(diff_list)

        return " ".join(filtered_python_files)
