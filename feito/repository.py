import os
import subprocess

from feito.filters import Filters


class Repository:

    GIT_DIFF_COMMAND = 'git diff --name-only --diff-filter=ACMR master'

    def __init__(self, repo):
        self.repo = repo
        self.repo_name = self.__repo_name()
        self.last_commit_id = self.__commit_id()

    def __repo_name(self):
        return os.getenv('REPOSITORY_NAME') or self.repo.working_dir.split('/')[-1]

    def __commit_id(self):
        return os.getenv('COMMIT_ID') or self.repo.head.commit.hexsha

    def diff_files(self):
        diff_files = subprocess.run(self.GIT_DIFF_COMMAND, stdout=subprocess.PIPE, shell=True)
        diff_list = diff_files.stdout.decode().split('\n')[:-1]

        filtered_python_files = Filters.filter_python_files(diff_list)

        return " ".join(filtered_python_files)
